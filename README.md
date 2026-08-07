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
> and scaffold a project called *<your project>*.

**2. Answer five questions, once.** Display name, a dot-free slug, where to put it, whether either
repository gets a remote, and the default branch. It builds two sibling repositories — your code,
and a private `-bridge` holding the board, specs and decisions — commits both, and stops.

**3. Start the Navigator.** The scaffolder hands you one line to run. It installs and wires
AgentPost, takes a mailbox, and comes back to you.

**4. Have the Chart conversation.** This is the one long conversation, and the only part that is
really yours: what you're making, what would make it not worth doing, and **the first target** — the
smallest version that proves the idea, anchored to the most impressive real example of that shape.
Direction, not the whole design; everything else is layered on later.

**5. Say "go" when it asks for the crew.** The Navigator launches the Implementer and Reviewer
itself — on different model families where you have them, so the reviewer doesn't share the
builder's blind spots. You decide they exist; you don't type the commands.

**6. Then watch.** Specs get written, attacked, and built; work fans out to parallel subagents, each
with its own critic; and the loop runs on its own. It comes back to you at the **push gate** — a
plain-English summary and a yes/no — and nothing reaches your remote without that yes.

**From then on it's one question at a time.** Approve a push, answer a fork, set the next target.

*Every seat comes up reachable from your phone, so you can watch or steer any of them from
anywhere.*

The directive holds the method in full: the playbook, the three seat directives, three
trigger-loaded protocols, and the board and roadmap templates. This README is the door; the
directive is the building.
