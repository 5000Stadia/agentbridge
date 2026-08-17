# AgentBridge

A way of running a project with one human and a small number of AI agents.

A human says what they want, and what "good" means is written where every agent can read it. One
agent builds. A second, which does not know what the builder meant, examines what was actually
built — the failures a user would hit, the silent ones nobody would notice, and what is missing
that "good" implies. The builder fixes what is valid and returns, until it passes. Then the next
piece. Almost all the effort goes into the first conversation, because nothing built ever comes out
better than the design it was built from.

## Quickstart

**You need:** git and a CLI coding agent — Claude Code, Codex, or similar.

**Open a fresh agent in an empty folder and say:**

> Read `https://raw.githubusercontent.com/5000Stadia/agentbridge/main/AGENTBRIDGE-BUILD-DIRECTIVE.md`
> and follow it. I want to start a project here.

If that URL will not resolve, clone this repository and point at the local copy instead. Stay for
the first minute — a runtime opening a folder for the first time asks whether you trust it, and
nothing runs until you answer.

**Then have one long conversation.** What you're making, who it's for, what would make you proud of
it rather than merely satisfied, what would ruin it, and the most impressive real example of this
shape — which the agent will open and use, not merely cite. That conversation becomes the documents
everything else executes. It is the only long conversation, and it decides how good the result can
be.

**After that it runs.** It comes back to you for a fork its documents cannot answer, for anything
that cannot be undone, and whenever it wants your eye on how something looks or feels — that
judgement is yours and it is worth giving. Everything else proceeds. The running thing stays
current, so you can open it whenever you like, and what you find becomes the next piece of work.

Three forms, chosen after that conversation rather than before it: **one-shot** when one agent
could plausibly build the whole thing, and do that whenever it is honestly possible; **solo** for
long uninterrupted runs with the agent spawning its own critics; **crewed** when work must be built
in parallel across a seam. Crewed pairs with [AgentPost](https://github.com/5000Stadia/agentpost),
which is how standing seats talk. The other two need nothing but the agent you already have.

## Status

AgentBridge is evidence-driven: every mechanism in it traces to something observed in live builds —
it contains no speculative process. It is also young. If you run it and the method gets in your way,
an issue labelled `felt-deviation` describing what happened is the most useful thing you can send.

`AGENTBRIDGE-BUILD-DIRECTIVE.md` is the method in full. Earlier versions are preserved at the
`v1.0.0` and `v1.1.0` tags.
