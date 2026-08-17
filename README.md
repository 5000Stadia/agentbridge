# AgentBridge

A method for running software projects with one human and a small number of AI agents — designed
around the failure modes of agent-built software, and refined against real builds.

**The core idea:** a builder cannot examine its own work — its code and its tests come from the
same reading of the spec, so when the reading is wrong they agree with each other. AgentBridge
pairs every build with examination by an agent that does not know what the builder intended, holds
the quality bar in a written design the human sets once, and ships exactly what passed.

## How it works

1. **One design conversation.** The human says what they want, what "good" means, and what must
   never happen. The agent turns that into design documents every other agent reads — including a
   real anchor: the most impressive existing example of the shape, opened and studied, not cited.
2. **Build, examine, ship.** One agent builds each piece; a fresh agent examines what was actually
   built against the written intention — visible failures, silent ones, and what's missing. Work
   ships when it passes, and the loop moves to the next piece.
3. **The human stays light.** Interrupted only for genuine forks and irreversible acts. The running
   product stays current, so a glance at any moment is real.

Three forms, chosen by the shape of the work: **one-shot** (one agent, one pass — used whenever
honestly possible), **solo** (long autonomous runs with spawned critics), **crewed** (standing
seats over [AgentPost](https://github.com/5000Stadia/agentpost) when work runs parallel across a
seam).

## Quickstart

Open a CLI agent (Claude Code, Codex, or similar) in an empty folder and say:

> Read `https://raw.githubusercontent.com/5000Stadia/agentbridge/main/AGENTBRIDGE-BUILD-DIRECTIVE.md`
> and follow it. I want to start a project here.

Have the design conversation. Everything after it runs.

## Status

Evidence-driven: every mechanism traces to something observed in live builds — no speculative
process. If the method gets in your way on a real run, an issue labelled `felt-deviation` is the
most useful thing you can send.

`AGENTBRIDGE-BUILD-DIRECTIVE.md` is the method in full. Earlier versions are at the `v1.0.0` and
`v1.1.0` tags.
