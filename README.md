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

## Deploying it

Point a scaffolding agent at [`AGENTBRIDGE-BUILD-DIRECTIVE.md`](AGENTBRIDGE-BUILD-DIRECTIVE.md).
It creates the workspace — the code repository and a private sibling `<project>-bridge` holding
the board, specs and decisions — wires both, and stops. The next seat to act is a Navigator.

The directive holds the method in full: the playbook, the three seat directives, and the board
and roadmap templates. This README is the door; the directive is the building.
