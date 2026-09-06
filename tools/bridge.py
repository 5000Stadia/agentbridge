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
import sys
import urllib.parse
import webbrowser
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DEFAULT_PORT = 8787
DEFAULT_COMMENTS = "design/comments.jsonl"
PROJECT_TARGET = "project"


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
        self.load()

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
        m = re.search(
            r"^##\s+The spec list\s*$\n(.*?)(?=^##\s|\Z)",
            text,
            re.MULTILINE | re.DOTALL,
        )
        if not m:
            self.problems.append("design/intention.md has no '## The spec list'.")
            return []

        rows: list[Row] = []
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
            rows.append(Row(number, cells[1].strip(), cells[2].strip()))

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
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #16171a; --card: #1e2024; --ink: #e8e6e2; --muted: #9a9791;
    --line: #2f3238; --accent: #7fb5a2; --accent-ink: #14231e;
    --flag: #d8a55f; --flag-bg: #2b2317; --sunk: #24262b;
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


def _when(stamp: str) -> str:
    try:
        dt = datetime.fromisoformat(str(stamp))
    except ValueError:
        return html.escape(str(stamp))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone().strftime("%b %d, %H:%M")


def _note_html(entry: dict) -> str:
    folded = bool(entry.get("consumed"))
    kind = str(entry.get("kind", "note"))
    tag = "" if kind == "human" else f'<span class="tag">{html.escape(kind)}</span>'
    if folded:
        by = html.escape(str(entry.get("consumed_by", "the Navigator")))
        tag += f'<span class="tag">folded in by {by}</span>'
    return (
        f'<div class="note{" folded" if folded else ""}">'
        f'<div class="who"><b>{html.escape(str(entry.get("author", "unnamed")))}</b>'
        f" &middot; {_when(entry.get('at', ''))}{tag}</div>"
        f'<div class="text">{_inline(str(entry.get("text", "")))}</div></div>'
    )


def _form_html(target: str, author: str) -> str:
    return (
        '<form class="add" method="post" action="/note">'
        f'<input type="hidden" name="row" value="{html.escape(target)}">'
        '<textarea name="text" required placeholder="A detail for whoever builds this. '
        'It reaches them before they start."></textarea>'
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
            f"<span>next id <b>{html.escape(project.next_id)}</b></span>"
            if project.next_id
            else ""
        )
        + "</div></div></header><main>"
    )

    for problem in project.problems:
        out.append(f"<div class='problem'>{html.escape(problem)}</div>")

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
            "<section class='card'><div class='head'>"
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
        "<section class='card'><div class='head'><div class='num'>&middot;</div>"
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
    out.append("</section></main>")

    rel = os.path.relpath(project.comments_path, project.root)
    out.append(
        "<footer>Every row here is still to build, in order, and the ones marked in "
        "flight are being built now. A note is input, not work: it becomes work when "
        "the Navigator folds it into its row. A note on a row nobody has started "
        "reaches its builder before it begins, because the seat opening a row reads "
        "that row and everything left on it first. Agents leave notes here too, on "
        "whichever row the thing they found belongs to. Notes live in "
        f"<code>{html.escape(rel)}</code> and are read without this page running."
        "</footer></body></html>"
    )
    return "".join(out)


# -------------------------------------------------------- opening a row (CLI)


def brief(project: Project, number: str) -> int:
    """What a seat reads when it opens a row: the spec, and everything left on it."""
    row = next((r for r in project.rows if r.number == number), None)
    notes = [c for c in project.comments() if str(c.get("row")) == number]

    if row is None:
        if number == PROJECT_TARGET:
            print("The project as a whole")
        else:
            print(f"Row {number} is not in the spec list.")
            print("It has passed and left the list, or it was never written.")
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
        tally += f", {folded} already folded in"
    print(f"  Notes on this row ({tally})")
    print()
    for entry in notes:
        state = "folded in" if entry.get("consumed") else "waiting"
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
        print("  the plan, say why for anything you decline, and mark it folded in:")
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
    ap.add_argument("--consume", metavar="ID", help="mark one note folded in")
    ap.add_argument("--row", default=None, help=f"row number, or '{PROJECT_TARGET}'")
    ap.add_argument("--text", default=None)
    ap.add_argument(
        "--kind",
        default="agent",
        help="who is writing, shown as a tag on the page (default: agent)",
    )
    ap.add_argument("--waiting", action="store_true", help="only notes not folded in")
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
        print(f"folded in: {args.consume}")
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
            state = "folded in" if e.get("consumed") else "waiting"
            print(
                f"[{e.get('id')}] row {e.get('row')} · {e.get('author')} "
                f"({e.get('kind')}) · {e.get('at')} · {state}"
            )
            for line in str(e.get("text", "")).splitlines():
                print(f"    {line}")
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
