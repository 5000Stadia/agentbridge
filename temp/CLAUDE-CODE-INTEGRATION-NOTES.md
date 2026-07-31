# AgentBridge × Claude Code — implementation notes

Working notes for consideration, not a proposal to the board. Mechanism details in
`CLAUDE-CODE-REFERENCE.md`; open findings in `AUDIT-OPEN-ITEMS.md`.

**Fetching the docs changed two things I said earlier in conversation.** The blunt push-gate block
needs no script (§3.1), and `SessionStart.watchPaths` + `FileChanged` enables something I did not
know existed and would now rank second (§3.2).

---

## 1. Three constraints that decide the shape

**Runtime neutrality.** `AGENTS.md`/`CLAUDE.md` exist as a pair so Codex seats are first-class,
and the Reviewer is *suggested* to run on a different family — currently OpenAI. **A Claude hook
covers two seats out of three.** A rule that looks enforced but silently skips one seat is worse
than an unenforced rule, because seats will trust it — the method's own *absence reading as
affirmative* failure.

**Two roots, one method.** Navigator roots on `<project>-bridge/`, Implementer and Reviewer on
`<project>/`. `.claude/settings.json` is per-root, so any config would have to be duplicated into
both — two copies of one rule, drifting, which is *stale parallel descriptions*. See §2.

**Hooks are bypassable.** `--safe-mode`, `--bare`, and `disableAllHooks` each turn them off.
They stop drift and accident, not a determined process.

**Therefore:** enforcement that must hold for every seat lives in **git hooks and plain scripts**
(runtime-neutral, also catches the Captain at the keyboard). Claude hooks buy **priming and
ergonomics** — mainly context injection, which git cannot do. Never let a Claude hook be the only
thing standing behind a rule.

---

## 2. Package it as a plugin, not as per-repo settings

AgentPost already proves the pattern on this machine: `hooks/hooks.json` in a plugin, enabled per
project via `.claude/settings.local.json`, wiring four events without touching either repo.

An `agentbridge` plugin would carry hooks, `.claude/agents/`, and any slash commands **once per
machine**, apply from both roots, be versioned, and be adopted the same way AgentPost is —
matching *adopt once per machine* rather than inventing a second idiom. It also keeps the bridge
repo free of runtime-specific config, which preserves neutrality on disk even where behaviour is
Claude-only.

This is the single highest-leverage structural choice here. Everything below assumes it.

---

## 3. Candidates, ranked

### 3.1 The push gate — `permissions.deny` + `pre-push`, not a hook

*Makes real:* **"Nothing reaches the code remote without the Captain's approval."** The method's
hardest rule, currently zero enforcement.

The blunt form needs no script at all:

```json
{ "permissions": { "deny": ["Bash(git push *)"] } }
```

For the conditional form — allow once the gate has passed — a `PreToolUse` hook with
`{"if": "Bash(git push *)"}` returning `permissionDecision: deny`. Two properties from the docs
make this stronger than expected: **each subcommand in a chain is checked** (`npm test && git
push` matches), and **commands inside `$()` and backticks are checked too**. Hard to trip over by
accident.

*But the real enforcement is `pre-push` in the code repo*, because it also covers the Codex
Reviewer, the Captain's own shell, and any `--safe-mode` session. The elegant check uses machinery
the method already mandates — *the code commit pins the bridge commit it implements* — so a
`pre-push` that rejects any commit lacking a valid `Bridge: <sha>` trailer enforces **the pinning
rule and the push gate together**, in ~15 lines.

*Caveat:* `--no-verify` bypasses `pre-push`. Genuinely robust means server-side branch protection.
State the threat model rather than implying more than it delivers.

### 3.2 Live board invalidation — `watchPaths` + `FileChanged` ← the novel one

*Makes real:* **"The board supersedes everything"** and **"re-prime from the board, never from
memory"** — for the duration of a session, not just at its start.

`SessionStart` can return `watchPaths: ["PROJECT-BOARD.md"]`, and `FileChanged` then fires when
that file changes on disk. So a seat mid-session can be told the board moved under it and re-read
before acting.

This addresses a failure the method names but has no mechanism for: *the relay amending reality* —
a directive enforced after its premise died. Today a long Implementer session works from the board
it read at boot, and a Captain decision landing mid-session reaches it only if someone messages it.
This closes that without anyone having to remember.

The bridge is a sibling repo, so the watch path needs `--add-dir` or an absolute path from the
plugin. Worth confirming `watchPaths` accepts paths outside the project root before committing to
it — **unverified**.

### 3.3 `SessionStart` board injection

*Makes real:* **"Re-prime from the board at session start."** The most-repeated instruction in the
playbook, currently pure exhortation.

`SessionStart` → `additionalContext` with the board's contents, matcher `startup|resume|clear|
compact|fork`. Note `compact` and `clear` in that list: a seat that compacts mid-session
re-primes automatically, which is exactly when memory is least trustworthy.

Not additive token cost — the board is a mandatory read anyway; this removes a tool call and
removes the skip.

*Caveat:* it primes Claude seats only. The Codex Reviewer still reads it because its directive says
to. Acceptable, because failure to prime is **visible** — the seat won't know the current item —
unlike the push gate, where failure is silent.

### 3.4 `.claude/agents/` as the home for method subagents

*Makes real:* the seat-vs-subagent test. The playbook says recurring work, deep domains, and
accumulating registers are *"a task subagent with a file to write to"* — which maps one-to-one
onto Claude Code agent definitions, with `description`, `model`, and `tools` in frontmatter.

Right now the test resolves to an abstraction with no landing place. Naming the directory gives
the Navigator somewhere to put the answer. `SubagentStop` could additionally check the file was
actually written.

### 3.5 Status line showing the measure

*Makes real:* **"a number needs nobody to do anything and cannot be unseen."** Today that claim is
aspirational — the measure sits in a file someone has to open.

~10 lines parsing the measure row out of `PROJECT-BOARD.md` puts it permanently on screen. The
most *elegant* item here in proportion to its cost, and the only one that makes an existing claim
literally true rather than adding a new capability.

*Caveat:* `disableAllHooks: true` kills the status line along with hooks.

### 3.6 `bridge-check` on `PostToolUse`

*Makes real:* board bounded, `specs/` holds 0 or 1 files, filenames match `<item>-<slug>.md`, item
numbers never reused.

The script is the valuable half and is runtime-neutral — also usable from `pre-commit` on the
bridge repo. The hook is only what makes it automatic. `PostToolUse` cannot block (exit 2 is
non-blocking there), so it warns; `Stop` can block if that is wanted, and can return
`additionalContext` the seat then acts on.

---

## 4. Do not

- **Move rules into `CLAUDE.md`.** It is auto-loaded, which makes it the most tempting surface and
  the worst one — the playbook already forbids a second authoritative copy of a rule sitting on the
  highest-traffic file. The four-line doormat is already the correct exploitation of this.
- **Use the `prompt` or `agent` hook handler types for gating.** They put an LLM in the enforcement
  path; *instruments get the same scrutiny as code*, and an instrument sharing the reviewed party's
  blind spots is not a check. `command` for anything that gates.
- **Duplicate settings into both roots.** See §2 — that is the parallel-description failure.

---

## 5. Sequencing

The method's first listed failure mode is *governance outrunning the governed* — process revised
sixteen times for a project with no artifacts. Six items of tooling on a method with zero
deployments is that failure exactly.

**Before first contact, build only what fails silently:** 3.1 (an unauthorised push) and 3.3 (a
seat working from stale memory). Both are cheap; neither needs the plugin to exist first.

**After a real deployment**, let the direction audit say which rules actually get skipped, and
build against that evidence. 3.2 is the most interesting candidate and should be verified
(`watchPaths` across repo boundaries) before it is counted on.

3.5 is small enough to do whenever it would be enjoyable rather than justified.
