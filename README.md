# AgentBridge

A working structure for a project run by one human and a small number of agent seats.

**The Captain** is the human, and the Captain decides. **The Navigator** holds the chart —
mission, roadmap, coherence, validity — and never holds the wheel. **The Implementer** writes
specs and code, and is the project's heartbeat. **The Reviewer** falsifies: the work, and
whether it is still the right work.

Captain and Navigator are the thinking channel; Implementer and Reviewer are the doing channel.
That split is the authority boundary.

AgentBridge pairs with [AgentPost](https://github.com/5000Stadia/agentpost), which is how the
seats talk. AgentBridge is how they are organised.

## What you need

- **A CLI agent runtime** — Claude Code, Codex, or any agent that reads `AGENTS.md`/`CLAUDE.md`.
  Two runtimes from different model families is better: the Reviewer is suggested to run on a
  different family than the Implementer, so it does not share the Implementer's blind spots.
- **git**, and **Python 3.11+** for [AgentPost](https://github.com/5000Stadia/agentpost)
  (Node 22+ only if a seat runs under Codex's managed adapter). You do not install AgentPost
  yourself — seats capability-check and install it during their own boot.

## Setup

1. **Get the directive.** Clone this repository, or download the single file
   [`AGENTBRIDGE-BUILD-DIRECTIVE.md`](AGENTBRIDGE-BUILD-DIRECTIVE.md) — it is the whole method.

2. **Scaffold.** Start a fresh agent session and tell it:
   *read `AGENTBRIDGE-BUILD-DIRECTIVE.md` and follow it.*
   It will confirm five inputs with you before touching the filesystem — project display name,
   a dot-free slug, the workspace parent directory, each repository's remote and visibility,
   and the default branch — then create two sibling repositories: `<project>/` for code and
   `<project>-bridge/` for the board, specs and decisions. It commits both, reports the tree,
   and stops. It makes no design decisions.

   *This is deliberately not the Navigator.* A seat's identity comes from its spawn, and the
   Navigator's home — the bridge — does not exist until this step finishes. The scaffolder is a
   disposable seat that builds the world and hands off; the Navigator then boots cold into it,
   the same way every one of its future sessions will.

3. **Spawn the Navigator.** Per the scaffolder's handoff line, start a new agent session pointed
   at `<project>-bridge/boot.md`. It wires AgentPost, registers its seat, verifies it is
   receiving live, and instantiates the board.

4. **Run the Chart.** The one long conversation, you and the Navigator: mission, the bet, the
   audience, falsifiers, non-negotiables, the first-contact artifact, the roadmap, and the
   operating values. It ends at a stated exit condition — not when the conversation runs out —
   and `boot.md` deletes itself as the receipt that setup is done.

5. **Muster the doing seats.** The Navigator hands you one spawn packet per seat — launch
   command, directive path, mailbox. You start the Implementer and Reviewer as separate CLI
   processes; only the human starts seats.

6. **The loop runs.** The Reviewer red-teams the map, the first phase read pins owners, and the
   Implementer takes the first item. From here the structure drives itself: specs deliberated to
   green, implementations reviewed to green, and **nothing reaches your code remote without your
   approval at the push gate** — that approval is the only standing demand on your attention.

The directive holds the method in full: the playbook, the three seat directives, four
trigger-loaded protocols, and the board and roadmap templates. This README is the door; the
directive is the building.
