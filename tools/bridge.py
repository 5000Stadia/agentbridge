#!/usr/bin/env python3
"""The bridge — a local page showing the plan the agents are working from,
open for notes on any row, including rows nobody has started.

    python3 design/bridge.py

It reads `design/intention.md` for the spec list and `design/specs/` for what is
in flight, serves that on 127.0.0.1, and appends notes to
`design/comments.jsonl`. It writes nothing else: a note is input, and it becomes
work when the Navigator folds it into its row.

Agents do not need the page running. They use the same file:

    python3 design/bridge.py --row 8              # opening row 8: its spec and every note on it
    python3 design/bridge.py --add --row 8 --author build --text '...'
    python3 design/bridge.py --consume <id>

Python 3.8+, standard library only.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import secrets
import subprocess
import sys
import urllib.parse
import webbrowser
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DEFAULT_PORT = 8787
DEFAULT_COMMENTS = "design/comments.jsonl"
PROJECT_TARGET = "project"


def _git(root: Path, *args: str, timeout: float = 15.0) -> str:
    """Run one git command. Any failure is an empty string, never an exception."""
    try:
        done = subprocess.run(
            ["git", "-C", str(root), *args],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return done.stdout if done.returncode == 0 else ""


def _rows_from_text(text: str) -> list[tuple[str, str, str]]:
    """The spec list as (number, target, done), from any version of intention.md."""
    m = re.search(
        r"^##\s+The spec list\s*$\n(.*?)(?=^##\s|\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not m:
        return []
    out = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = _split_table_row(line)
        if len(cells) < 3:
            continue
        number = cells[0].strip()
        if not number or number == "#" or set(number) <= set("-: "):
            continue
        out.append((number, cells[1].strip(), cells[2].strip()))
    return out


class Row:
    """One line of the spec list."""

    def __init__(self, number: str, target: str, done: str) -> None:
        self.number = number
        self.target = target
        self.done = done
        self.plan_paths: list[Path] = []

    @property
    def in_flight(self) -> bool:
        return bool(self.plan_paths)


class Project:
    """What the design documents say. Re-read on every request."""

    def __init__(self, root: Path, comments_path: Path) -> None:
        self.root = root
        self.comments_path = comments_path
        self.name = root.name
        self.summary = ""
        self.rows: list[Row] = []
        self.next_id = ""
        self.problems: list[str] = []
        self._closed: dict[str, dict] = {}
        self._closed_at_head = None
        self.load()

    # -- what has already passed -----------------------------------------

    def closed_rows(self) -> dict[str, dict]:
        """Rows that have left the spec list, read out of git.

        The method closes a row in one commit that deletes the row from
        `design/intention.md` and its plan from `design/specs/` together, so
        git already knows what passed, when, and in which commit. Nothing here
        is written down a second time, which is why it cannot go stale.
        """
        head = _git(self.root, "rev-parse", "HEAD").strip()
        if not head:
            return {}
        if self._closed_at_head == head:
            return self._closed

        log = _git(
            self.root,
            "log",
            "--reverse",
            "--format=%H\x1f%aI\x1f%s",
            "--",
            "design/intention.md",
        )
        # Every row that ever had a plan written for it. A row is built when a
        # plan for it existed; a row that leaves the list having never had one
        # was dropped before anyone started, and that is the honest difference
        # between finished and abandoned. Asking whether the plan file ever
        # existed survives however it later left — deleted, renamed, or moved.
        planned = set()
        for path in _git(
            self.root,
            "log",
            "--all",
            "--diff-filter=A",
            "--name-only",
            "--format=",
            "--",
            "design/specs/",
        ).splitlines():
            name = path.strip().split("/")[-1]
            if name:
                planned.add(name.split("-", 1)[0])

        closed: dict[str, dict] = {}
        previous: dict[str, tuple[str, str]] = {}
        for line in log.splitlines():
            parts = line.split("\x1f")
            if len(parts) != 3:
                continue
            sha, when, subject = parts
            text = _git(self.root, "show", f"{sha}:design/intention.md")
            if not text.strip():
                # The file did not exist or could not be read at this commit.
                # Absence here is not evidence that anything closed.
                continue
            current = {n: (t, d) for n, t, d in _rows_from_text(text)}
            for number in [n for n in previous if n not in current]:
                target, done = previous[number]
                closed[number] = {
                    "number": number,
                    "target": target,
                    "done": done,
                    "commit": sha,
                    "at": when,
                    "subject": subject,
                    "built": number in planned,
                }
            previous = current

        # A number is never reused, but a row can be re-opened by hand; what is
        # in the list now is the truth, so it is not also closed.
        for row in self.rows:
            closed.pop(row.number, None)
        self._closed = closed
        self._closed_at_head = head
        return closed

    def load(self) -> None:
        self.problems = []
        self.rows = []
        self.summary = ""
        self.next_id = ""

        intention = self.root / "design" / "intention.md"
        if not intention.is_file():
            self.problems.append(
                f"No plan yet: {intention} does not exist. The front door writes it."
            )
            return

        text = intention.read_text(encoding="utf-8", errors="replace")
        self.name = self._read_name(text) or self.root.name
        self.summary = self._read_summary(text)
        self.rows = self._read_rows(text)
        self.next_id = self._read_next_id(text)
        self._attach_plans()

    def _read_name(self, text: str) -> str:
        m = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
        if not m:
            return ""
        return re.split(r"\s+[—-]\s+intention\s*$", m.group(1))[0].strip()

    def _read_summary(self, text: str) -> str:
        m = re.search(
            r"^##\s+What we're making\s*$\n(.*?)(?=^##\s|\Z)",
            text,
            re.MULTILINE | re.DOTALL,
        )
        if not m:
            return ""
        lines = [ln.strip() for ln in m.group(1).strip().splitlines() if ln.strip()]
        return " ".join(lines)

    def _read_next_id(self, text: str) -> str:
        m = re.search(r"\*\*Next ID:\*\*\s*(\S+)", text)
        return m.group(1).strip() if m else ""

    def _read_rows(self, text: str) -> list[Row]:
        if "## The spec list" not in text:
            self.problems.append("design/intention.md has no '## The spec list'.")
            return []
        rows = [Row(n, t, d) for n, t, d in _rows_from_text(text)]
        if not rows:
            self.problems.append(
                "The spec list is empty: every row has passed, or none is written yet."
            )
        return rows

    def _attach_plans(self) -> None:
        specs = self.root / "design" / "specs"
        if not specs.is_dir():
            return
        by_number = {r.number: r for r in self.rows}
        for path in sorted(specs.glob("*.md")):
            row = by_number.get(path.name.split("-", 1)[0])
            if row is not None:
                row.plan_paths.append(path)

    # -- notes ----------------------------------------------------------

    def comments(self) -> list[dict]:
        if not self.comments_path.is_file():
            return []
        merged: dict[str, dict] = {}
        with self.comments_path.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if not isinstance(entry, dict):
                    continue
                cid = str(entry.get("id", ""))
                if not cid:
                    continue
                # A later line for the same id updates it, so marking a note
                # folded in is an append and never a rewrite.
                merged.setdefault(cid, {}).update(entry)
        return sorted(merged.values(), key=lambda e: str(e.get("at", "")))

    def add_comment(self, target: str, author: str, text: str, kind: str) -> dict:
        entry = {
            "id": secrets.token_hex(6),
            "row": target,
            "author": author or "unnamed",
            "kind": kind,
            "text": text,
            "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "consumed": False,
        }
        self._append(entry)
        return entry

    def consume(self, comment_id: str, by: str) -> bool:
        if comment_id not in {str(c.get("id")) for c in self.comments()}:
            return False
        self._append(
            {
                "id": comment_id,
                "consumed": True,
                "consumed_by": by,
                "consumed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            }
        )
        return True

    def _append(self, entry: dict) -> None:
        self.comments_path.parent.mkdir(parents=True, exist_ok=True)
        line = json.dumps(entry, ensure_ascii=False) + "\n"
        # O_APPEND keeps a short write atomic against other appenders, so two
        # agents writing at once cannot interleave inside one line.
        fd = os.open(self.comments_path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
        try:
            os.write(fd, line.encode("utf-8"))
        finally:
            os.close(fd)


def _split_table_row(line: str) -> list[str]:
    """Split one markdown table row on unescaped pipes."""
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    cells: list[str] = []
    buf: list[str] = []
    escaped = False
    for ch in line:
        if escaped:
            buf.append(ch)
            escaped = False
        elif ch == "\\":
            escaped = True
        elif ch == "|":
            cells.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    cells.append("".join(buf))
    return cells


# ------------------------------------------------------------------- the page

CSS = """
:root {
  color-scheme: light dark;
  --bg: #fbfaf8; --card: #fff; --ink: #1a1a19; --muted: #6b6a66;
  --line: #e4e1db; --accent: #2f5d50; --accent-ink: #fff;
  --flag: #8a5a1e; --flag-bg: #fdf3e3; --sunk: #f4f3f0;
  --good: #2d6a3f; --good-bg: #e9f4ec;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #16171a; --card: #1e2024; --ink: #e8e6e2; --muted: #9a9791;
    --line: #2f3238; --accent: #7fb5a2; --accent-ink: #14231e;
    --flag: #d8a55f; --flag-bg: #2b2317; --sunk: #24262b;
    --good: #7fc79a; --good-bg: #1b2a20;
  }
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink);
  font: 15px/1.55 ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif; }
code { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: .9em;
  background: var(--sunk); padding: .1em .35em; border-radius: 4px; }
header { border-bottom: 1px solid var(--line); padding: 20px 24px 16px; }
header .wrap { max-width: 880px; margin: 0 auto; }
header h1 { margin: 0 0 5px; font-size: 20px; letter-spacing: -.01em; }
header p { margin: 0; color: var(--muted); max-width: 72ch; font-size: 14px; }
.counts { margin-top: 11px; display: flex; gap: 18px; flex-wrap: wrap;
  font-size: 13px; color: var(--muted); }
.counts b { color: var(--ink); font-weight: 600; }
main { max-width: 880px; margin: 0 auto; padding: 24px 24px 60px; }
.card { background: var(--card); border: 1px solid var(--line); border-radius: 10px;
  margin-bottom: 18px; overflow: hidden; }
.head { display: flex; gap: 14px; padding: 16px 18px; align-items: baseline; }
.num { flex: none; min-width: 2.1em; text-align: center; font-weight: 650;
  font-variant-numeric: tabular-nums; color: var(--accent); }
.head .body { flex: 1; min-width: 0; }
.target { margin: 0 0 8px; }
.done { margin: 0; padding: 9px 12px; background: var(--sunk); border-radius: 7px;
  font-size: 13.5px; color: var(--muted); }
.done b { color: var(--ink); font-weight: 600; }
.badges { margin-top: 10px; display: flex; gap: 8px; flex-wrap: wrap; font-size: 12px; }
.badge { padding: 2px 9px; border-radius: 999px; border: 1px solid var(--line);
  color: var(--muted); }
.badge.flight { background: var(--flag-bg); color: var(--flag); border-color: transparent; }
.badge.has { color: var(--accent); border-color: var(--accent); }
.notes { border-top: 1px solid var(--line); padding: 2px 18px 0; }
.note { padding: 12px 0; border-bottom: 1px solid var(--line); }
.note:last-child { border-bottom: 0; }
.note .who { font-size: 12.5px; color: var(--muted); margin-bottom: 3px; }
.note .who b { color: var(--ink); font-weight: 600; }
.note.folded { opacity: .55; }
.note .text { white-space: pre-wrap; }
.tag { font-size: 11px; text-transform: uppercase; letter-spacing: .04em;
  padding: 1px 6px; border-radius: 4px; background: var(--sunk); margin-left: 6px;
  color: var(--muted); }
form.add { border-top: 1px solid var(--line); padding: 14px 18px;
  display: grid; gap: 10px; grid-template-columns: 1fr auto auto; }
form.add textarea { grid-column: 1 / -1; width: 100%; min-height: 60px;
  resize: vertical; font: inherit; padding: 9px 11px; border-radius: 7px;
  border: 1px solid var(--line); background: var(--bg); color: var(--ink); }
form.add input { font: inherit; padding: 7px 10px; border-radius: 7px; width: 170px;
  border: 1px solid var(--line); background: var(--bg); color: var(--ink); }
form.add button { font: inherit; font-weight: 600; padding: 7px 16px;
  border-radius: 7px; border: 0; background: var(--accent); color: var(--accent-ink);
  cursor: pointer; }
form.add .spacer { grid-column: 1; }
.note .where { font-weight: 600; color: var(--accent); text-decoration: none; }
.card.queue { border-color: var(--accent); }
.badge.completed { background: var(--good-bg); color: var(--good);
  border-color: transparent; font-weight: 600; }
.badge.mono { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
details.passed { margin-top: 34px; }
details.passed > summary { cursor: pointer; font-weight: 600; padding: 10px 0 16px;
  color: var(--muted); list-style: none; }
details.passed > summary::-webkit-details-marker { display: none; }
details.passed > summary::before { content: "▸ "; }
details.passed[open] > summary::before { content: "▾ "; }
details.passed > summary:hover { color: var(--ink); }
.card.gone .num { color: var(--muted); }
.empty { color: var(--muted); font-size: 13.5px; padding: 12px 0; }
.problem { background: var(--flag-bg); color: var(--flag); padding: 12px 16px;
  border-radius: 8px; margin-bottom: 18px; }
footer { max-width: 880px; margin: 0 auto; padding: 0 24px 60px;
  color: var(--muted); font-size: 13px; max-width: 72ch; }
@media (max-width: 620px) {
  form.add { grid-template-columns: 1fr; }
  form.add input { width: 100%; }
  .head { flex-direction: column; gap: 6px; }
  .num { text-align: left; }
}
"""


def _inline(text: str) -> str:
    """Escape, then honour the little markdown a spec row actually uses."""
    out = html.escape(text)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", out)
    return out


def _numeric(number: str) -> tuple:
    return (0, int(number)) if number.isdigit() else (1, number)


def _day(stamp: str) -> str:
    try:
        dt = datetime.fromisoformat(str(stamp))
    except ValueError:
        return html.escape(str(stamp)[:10])
    return dt.astimezone().strftime("%b %d")


def _when(stamp: str) -> str:
    try:
        dt = datetime.fromisoformat(str(stamp))
    except ValueError:
        return html.escape(str(stamp))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone().strftime("%b %d, %H:%M")


def _note_html(entry: dict, target_label: str = "") -> str:
    folded = bool(entry.get("consumed"))
    kind = str(entry.get("kind", "note"))
    tag = "" if kind == "human" else f'<span class="tag">{html.escape(kind)}</span>'
    if folded:
        by = html.escape(str(entry.get("consumed_by", "the Navigator")))
        tag += f'<span class="tag">reviewed by {by}</span>'
    where = ""
    if target_label:
        anchor = html.escape(str(entry.get("row", "")))
        where = (
            f'<a class="where" href="#row-{anchor}">{html.escape(target_label)}</a>'
            " &middot; "
        )
    return (
        f'<div class="note{" folded" if folded else ""}">'
        f'<div class="who">{where}'
        f'<b>{html.escape(str(entry.get("author", "unnamed")))}</b>'
        f" &middot; {_when(entry.get('at', ''))}{tag}</div>"
        f'<div class="text">{_inline(str(entry.get("text", "")))}</div></div>'
    )


def _form_html(target: str, author: str, placeholder: str = "") -> str:
    placeholder = placeholder or (
        "A detail for whoever builds this. It reaches them before they start."
    )
    return (
        '<form class="add" method="post" action="/note">'
        f'<input type="hidden" name="row" value="{html.escape(target)}">'
        f'<textarea name="text" required placeholder="{html.escape(placeholder)}">'
        "</textarea>"
        '<span class="spacer"></span>'
        f'<input name="author" value="{html.escape(author)}" placeholder="your name" '
        'aria-label="your name">'
        "<button>Add a note</button></form>"
    )


def render(project: Project, author: str) -> str:
    project.load()
    by_target: dict[str, list[dict]] = {}
    for entry in project.comments():
        by_target.setdefault(str(entry.get("row", "")), []).append(entry)

    waiting_total = sum(
        1 for group in by_target.values() for n in group if not n.get("consumed")
    )
    in_flight = [r for r in project.rows if r.in_flight]
    closed = project.closed_rows()

    out = [
        "<!doctype html><html><head><meta charset='utf-8'>",
        "<meta name='viewport' content='width=device-width, initial-scale=1'>",
        f"<title>{html.escape(project.name)} &mdash; the plan</title>",
        f"<style>{CSS}</style></head><body><header><div class='wrap'>",
        f"<h1>{html.escape(project.name)}</h1>",
    ]
    if project.summary:
        out.append(f"<p>{_inline(project.summary)}</p>")
    out.append(
        "<div class='counts'>"
        f"<span><b>{len(project.rows)}</b> rows open</span>"
        f"<span><b>{len(in_flight)}</b> in flight</span>"
        f"<span><b>{waiting_total}</b> notes waiting</span>"
        + (
            f"<span><b>{len(closed)}</b> completed</span>" if closed else ""
        )
        + (
            f"<span>next id <b>{html.escape(project.next_id)}</b></span>"
            if project.next_id
            else ""
        )
        + "</div></div></header><main>"
    )

    for problem in project.problems:
        out.append(f"<div class='problem'>{html.escape(problem)}</div>")

    known = {r.number for r in project.rows} | {PROJECT_TARGET}
    gone = sorted(
        (t for t in by_target if t not in known),
        key=lambda t: (0, int(t)) if t.isdigit() else (1, t),
    )

    def label_for(target: str) -> str:
        if target == PROJECT_TARGET:
            return "the project"
        if target in closed:
            return f"row {target}, completed"
        return f"row {target}"

    # Everything nobody has reviewed, oldest first, whatever row it sits on —
    # including rows that have already passed and left the list. This is the
    # queue a seat reads before it takes new work.
    queue = [
        n
        for group in by_target.values()
        for n in group
        if not n.get("consumed")
    ]
    queue.sort(key=lambda n: str(n.get("at", "")))
    if queue:
        out.append(
            "<section class='card queue'><div class='head'>"
            "<div class='num'>&bull;</div><div class='body'>"
            f"<p class='target'><b>Notes to read</b> &mdash; {len(queue)} waiting</p>"
            "<p class='done'>Every note nobody has reviewed yet, oldest first, "
            "whatever it is attached to &mdash; including rows that have already "
            "passed. A seat reads these before it takes new work.</p>"
            "</div></div><div class='notes'>"
        )
        out.extend(
            _note_html(n, label_for(str(n.get("row", "")))) for n in queue
        )
        out.append("</div></section>")

    for row in project.rows:
        notes = by_target.get(row.number, [])
        waiting = sum(1 for n in notes if not n.get("consumed"))
        badges = []
        if row.plan_paths:
            for plan in row.plan_paths:
                badges.append(
                    "<span class='badge flight'>in flight &middot; "
                    f"{html.escape(plan.name)}</span>"
                )
        else:
            badges.append("<span class='badge'>not started</span>")
        if waiting:
            badges.append(
                f"<span class='badge has'>{waiting} note"
                f"{'s' if waiting > 1 else ''} waiting</span>"
            )
        out.append(
            f"<section class='card' id='row-{html.escape(row.number)}'>"
            "<div class='head'>"
            f"<div class='num'>{html.escape(row.number)}</div><div class='body'>"
            f"<p class='target'>{_inline(row.target)}</p>"
            f"<p class='done'><b>Done:</b> {_inline(row.done)}</p>"
            f"<div class='badges'>{''.join(badges)}</div></div></div>"
        )
        if notes:
            out.append("<div class='notes'>")
            out.extend(_note_html(n) for n in notes)
            out.append("</div>")
        out.append(_form_html(row.number, author))
        out.append("</section>")

    general = by_target.get(PROJECT_TARGET, [])
    out.append(
        f"<section class='card' id='row-{PROJECT_TARGET}'><div class='head'>"
        "<div class='num'>&middot;</div>"
        "<div class='body'><p class='target'><b>The project as a whole</b></p>"
        "<p class='done'>For anything with no row yet: a shape you want later, a "
        "worry, something you would rather we did differently. The Navigator turns "
        "these into rows.</p></div></div>"
    )
    if general:
        out.append("<div class='notes'>")
        out.extend(_note_html(n) for n in general)
        out.append("</div>")
    out.append(_form_html(PROJECT_TARGET, author))
    out.append("</section>")

    def note_block(target: str, placeholder: str = "") -> str:
        notes = by_target.get(target, [])
        block = ""
        if notes:
            block += "<div class='notes'>"
            block += "".join(_note_html(n) for n in notes)
            block += "</div>"
        return block + _form_html(target, author, placeholder)

    # Targets with notes that are not rows and that git has never seen close.
    for target in [t for t in gone if t not in closed]:
        waiting = sum(1 for n in by_target[target] if not n.get("consumed"))
        badges = ["<span class='badge'>not in the spec list</span>"]
        if waiting:
            badges.append(
                f"<span class='badge has'>{waiting} note"
                f"{'s' if waiting > 1 else ''} waiting</span>"
            )
        out.append(
            f"<section class='card gone' id='row-{html.escape(target)}'>"
            "<div class='head'>"
            f"<div class='num'>{html.escape(target)}</div><div class='body'>"
            f"<p class='target'><b>Row {html.escape(target)}</b></p>"
            "<p class='done'>This row is not in the spec list and git has no "
            "record of it closing. Its notes stay here and stay readable, and a "
            "new one still reaches whoever reads the queue.</p>"
            f"<div class='badges'>{''.join(badges)}</div></div></div>"
            + note_block(target)
            + "</section>"
        )

    # What has already passed, read out of git rather than written down again.
    if closed:
        order = sorted(
            closed.values(),
            key=lambda e: (e.get("at", ""), _numeric(e["number"])),
            reverse=True,
        )
        pending = sum(
            1
            for e in order
            for n in by_target.get(e["number"], [])
            if not n.get("consumed")
        )
        head = f"Completed &mdash; {len(order)} row{'s' if len(order) > 1 else ''}"
        if pending:
            head += (
                f", {pending} note{'s' if pending > 1 else ''} waiting on finished work"
            )
        out.append(
            f"<details class='passed'{' open' if pending else ''}>"
            f"<summary>{head}</summary>"
        )
        for entry in order:
            number = entry["number"]
            waiting = sum(
                1 for n in by_target.get(number, []) if not n.get("consumed")
            )
            badges = [
                "<span class='badge completed'>"
                + ("completed" if entry["built"] else "dropped unbuilt")
                + f" &middot; {_day(entry['at'])}</span>",
                f"<span class='badge mono'>{html.escape(entry['commit'][:7])}</span>",
            ]
            if waiting:
                badges.append(
                    f"<span class='badge has'>{waiting} note"
                    f"{'s' if waiting > 1 else ''} waiting</span>"
                )
            out.append(
                f"<section class='card' id='row-{html.escape(number)}'>"
                "<div class='head'>"
                f"<div class='num'>{html.escape(number)}</div><div class='body'>"
                f"<p class='target'>{_inline(entry['target'])}</p>"
                f"<p class='done'><b>Done:</b> {_inline(entry['done'])}</p>"
                f"<div class='badges'>{''.join(badges)}</div></div></div>"
                + note_block(
                    number,
                    "A second thought on work that is already done. It waits in the "
                    "queue like any other note, and is read before the next row "
                    "opens.",
                )
                + "</section>"
            )
        out.append("</details>")

    out.append("</main>")

    rel = os.path.relpath(project.comments_path, project.root)
    out.append(
        "<footer>Every row here is still to build, in order, and the ones marked in "
        "flight are being built now. A note is input, not work: it becomes work when "
        "the Navigator folds it into its row. A note on a row nobody has started "
        "reaches its builder before it begins, because the seat opening a row reads "
        "that row and everything left on it first. Agents leave notes here too, on "
        "whichever row the thing they found belongs to. A note on work that has "
        "already passed is not lost and not filtered out: it waits in the queue like "
        "any other, because finished is not the same as settled. Reviewing a note "
        "may accept it, decline it with a reason, or defer it. Notes live in "
        f"<code>{html.escape(rel)}</code> and are read without this page running; "
        "opening this page reviews nothing."
        "</footer></body></html>"
    )
    return "".join(out)


# -------------------------------------------------------- opening a row (CLI)


def brief(project: Project, number: str) -> int:
    """What a seat reads when it opens a row: the spec, and everything left on it."""
    row = next((r for r in project.rows if r.number == number), None)
    notes = [c for c in project.comments() if str(c.get("row")) == number]

    closed = project.closed_rows().get(number)
    if row is None and closed is not None:
        state = "completed" if closed["built"] else "dropped unbuilt"
        print(
            f"Row {number} — {state} {_day(closed['at'])}, commit "
            f"{closed['commit'][:7]} ({closed['subject']})"
        )
        print()
        print("  What it was")
        for line in _wrap(closed["target"]):
            print(f"    {line}")
        print()
        print("  Done")
        for line in _wrap(closed["done"]):
            print(f"    {line}")
        print()
    elif row is None:
        if number == PROJECT_TARGET:
            print("The project as a whole")
        else:
            print(f"Row {number} is not in the spec list, and git has no record")
            print("of it closing. It was never written, or it predates this history.")
            if not notes:
                return 1
            print()
    else:
        if row.plan_paths:
            plans = ", ".join(
                os.path.relpath(p, project.root) for p in row.plan_paths
            )
            state = f"in flight ({plans})"
        else:
            state = "not started"
        print(f"Row {row.number} — {state}")
        print()
        print("  What to build now")
        for line in _wrap(row.target):
            print(f"    {line}")
        print()
        print("  Done")
        for line in _wrap(row.done):
            print(f"    {line}")
        print()

    waiting = [n for n in notes if not n.get("consumed")]
    folded = len(notes) - len(waiting)
    if not notes:
        print("  No notes on this row.")
        return 0

    tally = f"{len(waiting)} waiting"
    if folded:
        tally += f", {folded} already reviewed"
    print(f"  Notes on this row ({tally})")
    print()
    for entry in notes:
        state = "reviewed" if entry.get("consumed") else "waiting"
        print(
            f"  [{entry.get('id')}] {entry.get('author')} "
            f"({entry.get('kind')}) · {entry.get('at')} · {state}"
        )
        for line in str(entry.get("text", "")).splitlines():
            for part in _wrap(line):
                print(f"      {part}")
        print()
    if waiting:
        print("  Waiting notes are input, not instructions. Fold what is right into")
        print("  the plan; say why for anything you decline or defer. Either way,")
        print("  mark exactly the ids you actually read:")
        print(f"    python3 {os.path.basename(__file__)} --consume <id>")
    return 0


def _wrap(text: str, width: int = 88) -> list[str]:
    words = text.split()
    if not words:
        return [""]
    lines, line = [], words[0]
    for word in words[1:]:
        if len(line) + 1 + len(word) > width:
            lines.append(line)
            line = word
        else:
            line += " " + word
    lines.append(line)
    return lines


# ----------------------------------------------------------------- the server


class Handler(BaseHTTPRequestHandler):
    project: Project
    author: str
    server_version = "bridge"

    def log_message(self, fmt: str, *args) -> None:  # quiet
        pass

    def _send(self, code: int, body: bytes) -> None:
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if urllib.parse.urlparse(self.path).path not in ("/", "/index.html"):
            self._send(404, b"not here")
            return
        self._send(200, render(self.project, self.author).encode("utf-8"))

    def do_POST(self) -> None:
        if urllib.parse.urlparse(self.path).path != "/note":
            self._send(404, b"not here")
            return
        length = int(self.headers.get("Content-Length") or 0)
        if length > 64 * 1024:
            self._send(413, b"too long")
            return
        fields = urllib.parse.parse_qs(
            self.rfile.read(length).decode("utf-8", errors="replace")
        )
        text = fields.get("text", [""])[0].strip()
        target = fields.get("row", [PROJECT_TARGET])[0].strip() or PROJECT_TARGET
        author = fields.get("author", [""])[0].strip() or self.author
        if text:
            self.project.add_comment(target, author, text, "human")
            Handler.author = author
        # Post, redirect, get — so a refresh never repeats the note.
        self.send_response(303)
        self.send_header("Location", "/")
        self.send_header("Content-Length", "0")
        self.end_headers()


def serve(project: Project, port: int, author: str, open_browser: bool) -> None:
    Handler.project = project
    Handler.author = author
    httpd = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = f"http://127.0.0.1:{httpd.server_address[1]}/"
    print(f"{project.name} — the plan")
    print(f"  {url}")
    print(f"  notes: {project.comments_path}")
    print("  ctrl-c to stop")
    if open_browser:
        try:
            webbrowser.open(url)
        except Exception:
            pass
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
    finally:
        httpd.server_close()


# -------------------------------------------------------------------- the CLI


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(
        prog="bridge",
        description="Serve this project's plan as a page anyone may add notes to, "
        "or read and write those notes from the command line. With --row and no "
        "other mode, print that row's spec and every note left on it — what a seat "
        "reads when the row opens.",
    )
    ap.add_argument("project", nargs="?", default=".", help="project root (default: .)")
    ap.add_argument("--port", type=int, default=DEFAULT_PORT)
    ap.add_argument(
        "--comments",
        default=None,
        help=f"note file, relative to the project (default: {DEFAULT_COMMENTS})",
    )
    ap.add_argument("--author", default=os.environ.get("USER", "human"))
    ap.add_argument("--open", action="store_true", help="open a browser too")
    ap.add_argument("--add", action="store_true", help="append one note and exit")
    ap.add_argument("--list", action="store_true", help="print notes and exit")
    ap.add_argument("--consume", metavar="ID", help="mark one note reviewed")
    ap.add_argument("--row", default=None, help=f"row number, or '{PROJECT_TARGET}'")
    ap.add_argument("--text", default=None)
    ap.add_argument(
        "--kind",
        default="agent",
        help="who is writing, shown as a tag on the page (default: agent)",
    )
    ap.add_argument(
        "--waiting",
        action="store_true",
        help="the queue: every note nobody has reviewed, oldest first, whatever row "
        "it is on. Alone, it is the read a seat does before taking new work.",
    )
    ap.add_argument("--json", action="store_true", help="machine-readable --list")
    args = ap.parse_args(argv)

    root = Path(args.project).expanduser().resolve()
    if not root.is_dir():
        print(f"bridge: no such directory: {root}", file=sys.stderr)
        return 2
    project = Project(root, root / (args.comments or DEFAULT_COMMENTS))

    if args.add:
        if not args.text:
            print("bridge: --add needs --text", file=sys.stderr)
            return 2
        entry = project.add_comment(
            args.row or PROJECT_TARGET, args.author, args.text, args.kind
        )
        print(entry["id"])
        return 0

    if args.consume:
        if not project.consume(args.consume, args.author):
            print(f"bridge: no note {args.consume}", file=sys.stderr)
            return 1
        print(f"reviewed: {args.consume}")
        return 0

    if args.list:
        entries = project.comments()
        if args.row:
            entries = [e for e in entries if str(e.get("row")) == args.row]
        if args.waiting:
            entries = [e for e in entries if not e.get("consumed")]
        if args.json:
            print(json.dumps(entries, ensure_ascii=False, indent=2))
            return 0
        if not entries:
            print("no notes")
            return 0
        for e in entries:
            state = "reviewed" if e.get("consumed") else "waiting"
            print(
                f"[{e.get('id')}] row {e.get('row')} · {e.get('author')} "
                f"({e.get('kind')}) · {e.get('at')} · {state}"
            )
            for line in str(e.get("text", "")).splitlines():
                print(f"    {line}")
        return 0

    if args.waiting and not (args.list or args.row):
        # --waiting alone is the read a seat does before it takes new work:
        # everything unreviewed, oldest first, whatever row it sits on —
        # including rows that have passed and left the spec list.
        queue = [e for e in project.comments() if not e.get("consumed")]
        if args.json:
            print(json.dumps(queue, ensure_ascii=False, indent=2))
            return 0
        if not queue:
            print("no notes waiting")
            return 0
        print(f"{len(queue)} note{'s' if len(queue) > 1 else ''} waiting, oldest first")
        print()
        live = {r.number for r in project.rows}
        closed = project.closed_rows()
        for e in queue:
            target = str(e.get("row", ""))
            where = "the project" if target == PROJECT_TARGET else f"row {target}"
            if target in closed:
                entry = closed[target]
                state = "completed" if entry["built"] else "dropped unbuilt"
                where += f" ({state} {_day(entry['at'])}, {entry['commit'][:7]})"
            elif target not in live and target != PROJECT_TARGET:
                where += " (not in the spec list)"
            print(
                f"  [{e.get('id')}] {where} · {e.get('author')} "
                f"({e.get('kind')}) · {e.get('at')}"
            )
            for line in str(e.get("text", "")).splitlines():
                for part in _wrap(line):
                    print(f"      {part}")
            print()
        print("  Mark exactly the ids you read:")
        print(f"    python3 {os.path.basename(__file__)} --consume <id>")
        return 0

    if args.row:
        # --row with no other mode is the read a seat does when the row opens.
        for problem in project.problems:
            print(f"bridge: {problem}", file=sys.stderr)
        return brief(project, args.row)

    for problem in project.problems:
        print(f"bridge: {problem}", file=sys.stderr)
    serve(project, args.port, args.author, args.open)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
