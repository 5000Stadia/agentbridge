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

## Quickstart

**You need:** git, Python 3.11+, and a CLI coding agent — Claude Code, Codex, or similar. Nothing
else; the crew installs its own tooling.

**1. Open a fresh agent in an empty folder and say:**

> Read `https://raw.githubusercontent.com/5000Stadia/agentbridge/main/AGENTBRIDGE-BUILD-DIRECTIVE.md`
> and follow it. You are the Navigator. The project is called *<your project>*.

If that URL does not resolve — a private fork, no network — clone this repository and point at the
local `AGENTBRIDGE-BUILD-DIRECTIVE.md` instead. **Stay for the first minute:** a runtime opening a
folder for the first time asks whether you trust it, and nothing runs until you answer.

**2. Answer six questions, once.** Display name, a dot-free slug, where to put it, whether either
repository gets a remote, the default branch, and the crew — which runtime and model each seat
runs on, proposed to you from what it finds installed. It builds two sibling repositories — your code,
and a private `-bridge` holding the board, specs and decisions — installs and wires AgentPost, and
takes a mailbox. **This is the only seat you ever start by hand.**

**3. Have the Chart conversation.** This is the one long conversation, and the only part that is
really yours: what you're making, what would make it not worth doing, and **the first target** — the
smallest version that proves the idea, anchored to the most impressive real example of that shape.
Direction, not the whole design; everything else is layered on later.

**4. Say "go" when it asks for the crew.** The Navigator launches the Implementer and Reviewer
itself — on different model families where you have them, so the reviewer doesn't share the
builder's blind spots. You decide they exist; you don't type the commands.

**5. Then watch.** Specs get written, attacked, and built; work fans out to parallel subagents, each
with its own critic; and the loop runs on its own. It comes back to you at the **push gate** with a
plain-English summary of what shipped-ready work exists. Whether that is a yes/no each time is
yours: during the Chart you choose the push cadence — confirm each push, push automatically once
you approve a target, or hold everything until a named milestone — and either way the report of
what went out always reaches you.

**From then on it's one question at a time.** Answer a fork, set the next target, and — if you
chose to confirm each — approve a push.

*How a seat launches and takes its mailbox is runtime-specific — some launchers bind identity at
start, others join just after. Remote Control, where a runtime supports it, is enabled separately
once the seat is up, and then it's reachable from your phone.*

The directive holds the method in full: the playbook, the three seat directives, three
trigger-loaded protocols, and the board and roadmap templates. This README is the door; the
directive is the building.
