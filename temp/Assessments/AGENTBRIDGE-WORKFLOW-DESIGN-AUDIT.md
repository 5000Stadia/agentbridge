# AgentBridge Workflow Design Audit

**Date:** 2026-07-29  
**Scope:** `/home/k/Projects/agentbridge` at commit `9450db9`  
**Disposition:** Design audit only; no AgentBridge source files were changed.

## Executive assessment

AgentBridge has a strong governing philosophy. Its best ideas are the separation of human
authority, direction, implementation, and falsification; the private bridge/code repository
boundary; first contact as an intentional challenge to the roadmap; premise-bearing decisions;
and a bounded current-state board backed by cited artifacts.

The current expression is more elaborate than its own principles allow. Its most elegant form
would be:

1. a small constitution;
2. an explicit, receipt-bearing state machine;
3. protocols loaded only when their trigger fires;
4. executable, validated scaffolding; and
5. precise authority, repository, identity, and access boundaries.

The goal should not be to redesign the seats. It should be to make the method smaller on the hot
path, more explicit at handoffs, and mechanically verifiable where prose currently carries the
contract.

## What should be preserved

- **The four-role cognitive separation.** Captain, Navigator, Implementer, and Reviewer address
  genuinely different failure modes.
- **The bridge/code repository split.** Project memory and publishable code have different
  visibility and lifecycle requirements.
- **First contact before elaboration.** Treating the roadmap as a hypothesis is one of the
  method's strongest anti-drift mechanisms.
- **Independent falsification.** The Reviewer attacks both implementation correctness and
  whether the work is still worth doing.
- **The Navigator's translation duty.** Keeping the Captain aware without requiring them to
  read implementation artifacts is essential.
- **Premise-bearing decisions.** “What would change the answer” turns reasoning into something
  the Harness can revisit mechanically.
- **Asymmetric apparatus changes.** Making removal easier than addition is an effective brake
  on process accretion.
- **A bounded current-state projection.** The board should remain a concise operational view,
  while durable detail is addressed by ID.

## Highest-value refinements

### 1. Make the method obey its own context discipline

The deployed `playbook.md` section is approximately 6,655 words. Context cost is flat as the
project grows, but it is not lean: every seat reloads AgentPost installation, naming, wiping,
Chart procedure, release handling, philosophy, and failure history during every session.

That weakens the spirit of the
[four-file onboarding contract](/home/k/Projects/agentbridge/AGENTBRIDGE-BUILD-DIRECTIVE.md:182)
and the
[cited-only context model](/home/k/Projects/agentbridge/AGENTBRIDGE-BUILD-DIRECTIVE.md:335).

Keep `playbook.md` to roughly 100–150 lines:

- authority and invariants;
- reading order;
- the item state machine;
- escalation routes; and
- artifact locations.

Move cold procedures into trigger-loaded files:

- `protocols/chart.md`
- `protocols/item-loop.md`
- `protocols/release.md`
- `protocols/agentpost.md`
- `protocols/apparatus-change.md`

Directives should contain only the differences between seats. They should cite shared invariants
instead of repeating them.

### 2. Replace absolute authority language with a precise authority matrix

The declaration that agents never decide
([lines 202–203](/home/k/Projects/agentbridge/AGENTBRIDGE-BUILD-DIRECTIVE.md:202))
conflicts with the Navigator declining proposals, the Reviewer issuing verdicts, and the
Implementer choosing technical mechanics.

A clearer boundary is:

| Actor | Authority |
|---|---|
| Captain | Mission, bet, roadmap, structural changes, publication policy, and exceptions |
| Navigator | Interpretation, current-state maintenance, coherence findings, and delegated triage |
| Implementer | Technical choices inside a confirmed specification |
| Reviewer | Exact-artifact verdicts and falsification; never product authority |
| Board | Records authority and current state; does not create authority |

Similarly, replace “the board supersedes everything” with field-scoped precedence. A status note
must not be capable of overriding a seat directive or the constitution. Every board section
should name:

- who may edit it;
- what receipt authorizes a change; and
- which source is authoritative for that field.

A Navigator relay should not itself be authority, but a board entry that records a direct
Captain decision with a date and receipt should be durable authority. That distinction is
currently blurred.

### 3. Turn the Loop into an explicit state machine

The prose has two distinct green events—specification green and implementation green—but the
[board flow has only one](/home/k/Projects/agentbridge/AGENTBRIDGE-BUILD-DIRECTIVE.md:1226).
It also omits the Navigator coherence read and Captain push gate.

Use explicit states:

```text
QUEUED
  → SPEC_DRAFT
  → SPEC_REVIEW
  → COHERENCE_CHECK
  → IMPLEMENTING
  → CODE_REVIEW
  → CAPTAIN_GATE
  → ARCHIVED
```

Side exits:

```text
CLARIFICATION → return to the same state
REFRAME / DETOUR / INVALIDATED PREMISE → PAUSED_FOR_CAPTAIN
```

Every transition should define:

- who moves it;
- required evidence;
- the exact artifact or revision involved;
- the failure destination; and
- what permits resumption.

The board should retain only the current state and receipt IDs. The archived specification
should retain the completed transition receipts.

### 4. Add a minimal specification and verdict contract

The workflow is meticulous about reviewing specifications but never defines the minimum contents
of one. Every live specification should contain:

- roadmap item and purpose;
- scope and non-goals;
- public-surface impact;
- invariants and failure policy;
- acceptance and witness tests;
- dependencies and migrations;
- rollback or recovery;
- open uncertainties; and
- specification-review, coherence, code-review, and gate receipts.

Reviewer verdicts should always name:

- the immutable commit or tree reviewed;
- tests and adversarial probes run;
- unverified areas;
- must-fix, should-fix, and minor findings; and
- whether any finding changes the public surface or only internals.

This makes “green” a reproducible claim rather than a conversational state.

### 5. Make the board genuinely bounded

The board says it holds no history, but `Declined proposals` grows indefinitely
([lines 1236–1241](/home/k/Projects/agentbridge/AGENTBRIDGE-BUILD-DIRECTIVE.md:1236)).
Retired-row tombstones can also accumulate. “Decision values live only here” additionally
conflicts with decision files containing what was decided.

Use this separation:

- **Board:** current effective state, currently open decisions, and currently challengeable
  declines.
- **`decisions/`:** durable decisions, rejected alternatives, and reversibility conditions.
- **Roadmap/archive:** retired-item pointers and historical outcomes.

Default to one active item. Multiple Implementers should require explicitly enabled lanes with
separate ownership and ordering rules. Otherwise “one slot per Implementer” introduces bridge
write races and speculative parallelism that the method otherwise tries to prevent.

For a small project, one active delivery lane plus freely spawned bounded subagents is the more
elegant default.

### 6. Specify the two-repository commit transaction

The current text says code commits pin bridge commits and mentions an undefined release manifest
([lines 305–307](/home/k/Projects/agentbridge/AGENTBRIDGE-BUILD-DIRECTIVE.md:305)).
The push-gate sequence does not precisely define when the specification is archived, when each
repository commits, or which exact code artifact received approval.

Define one reproducible sequence. For example:

1. Reviewer greens exact code commit or tree `C`.
2. Captain approves `C`.
3. Bridge archives the specification and records review/gate receipts; commit `B`.
4. The code repository records `B` without changing the reviewed code tree—for example, an
   annotated pairing tag on `C`.
5. Verify the `C ↔ B` receipt, then push.

Eliminate the release manifest unless it receives a location, owner, trigger, and template.

The scaffolder should also make an initial commit in **both** repositories. At present only the
bridge's first commit is required
([lines 93–94](/home/k/Projects/agentbridge/AGENTBRIDGE-BUILD-DIRECTIVE.md:93)),
leaving the project doormats uncommitted.

### 7. Make scaffolding executable and self-validating

A 1,300-line instruction asking an agent to reproduce embedded files “verbatim” while also
substituting placeholders is fragile. Store the actual template tree in the AgentBridge
repository and provide an idempotent scaffold command.

The scaffolder should ask separately for:

- project name;
- code-repository visibility and remote choice;
- bridge remote choice, with private as the only remote visibility;
- remote owner or organization; and
- local privacy requirements.

Validation should prove:

- two sibling Git roots;
- both initial commits exist;
- bridge visibility and remote choice are recorded;
- no unresolved `<project>` placeholders remain;
- each `AGENTS.md`/`CLAUDE.md` pair is identical;
- no unexpected project files exist;
- slot occupancy means “number of live `*.md` files,” not literal directory emptiness despite
  `.gitkeep`;
- worktrees are clean; and
- required local permissions are present.

The source repository should also test that rendered templates match their source assets and
that every documented location has an owner and trigger.

### 8. Isolate AgentPost as an adapter rather than governance

The version-specific AgentPost section occupies a large part of the always-read playbook. Move
it to `protocols/agentpost.md`; the stable playbook should state only communication invariants.

One concrete repair is required. The example says `join` takes no agent argument
([lines 475–476](/home/k/Projects/agentbridge/AGENTBRIDGE-BUILD-DIRECTIVE.md:475)),
but the installed CLI accepts an optional explicit agent. Explicit identity matters because the
Implementer and Reviewer share the project root
([line 482](/home/k/Projects/agentbridge/AGENTBRIDGE-BUILD-DIRECTIVE.md:482)).
Once both profiles exist, bare root inference can be ambiguous or silently select the workspace
default.

Prefer:

- explicit canonical identity at every seat launch;
- `agentpost join <canonical> --cli <runtime>` for shared roots;
- bare join only after uniqueness is proven;
- capability checks plus an immutable installer commit/checksum, rather than relying only on a
  mutable release tag;
- exact Message-ID claims and replies as the workflow receipt; and
- trusting AgentPost's `From` header instead of manually signing every AgentPost message.

Version-specific workarounds should carry an expiry condition and be re-tested on upgrade.

### 9. Distinguish intended scope from enforced access

“Pointing a seat at a folder is its permission”
([lines 700–701](/home/k/Projects/agentbridge/AGENTBRIDGE-BUILD-DIRECTIVE.md:700))
describes intended scope, not a security boundary. A local process can commonly read sibling
directories regardless of its working directory.

Rename the workspace-map field to **intended scope**. If confidentiality or write isolation is
required, use actual enforcement:

- sandbox rules;
- OS permissions;
- separate worktrees or accounts;
- scoped credentials; or
- a tool boundary that denies access.

The bridge's “private” claim should likewise define whether it means unpublished, access
controlled, owner-private on disk, or all three.

### 10. Add method provenance and an upgrade path

AgentBridge expects deployed projects to diverge, correctly, but it does not record the method
revision from which they diverged or explain how upstream fixes should be adopted without
overwriting local structural decisions.

Record on the board:

- AgentBridge base commit;
- local apparatus decisions;
- AgentPost capability/release receipt; and
- last reviewed upstream method revision.

Method upgrades should be three-way reviews:

1. compare the deployed base with the new upstream revision;
2. preserve intentional local decisions;
3. treat upstream changes as structural proposals; and
4. update the recorded base only after Captain approval.

## Smaller refinements

- Replace “the bet implies a number” with “the bet implies an outcome indicator.” Prefer a
  count with a denominator, but allow a falsifiable observation protocol where forced
  quantification would create a misleading metric.
- Timebox prior-art research during Chart so “locate the bet” cannot delay first contact
  indefinitely.
- Treat Navigator declines as visible triage dispositions under delegated rules, not final
  project decisions. The Captain may always override them.
- Define how bridge writes are serialized. The simplest stock rule is one active item and one
  current bridge writer at each handoff.
- Clarify “nothing personal.” The board currently asks for the Captain's own name. Prefer a
  Captain-chosen display name and explicitly prohibit secrets and unnecessary personal data.
- Keep the metaphors—Chart, Muster, Loop, Harness—but pair each with a precise operational
  definition. The names are memorable; they should not carry contract details by implication.

## Recommended target shape

```text
<project>-bridge/
├── AGENTS.md
├── CLAUDE.md
├── playbook.md                 # small constitution and state machine
├── PROJECT-BOARD.md            # bounded current projection
├── directives/
│   ├── navigator.md            # seat-specific delta only
│   ├── implementer.md
│   └── reviewer.md
├── protocols/
│   ├── chart.md                # read only during Chart/reframe
│   ├── item-loop.md            # read when taking or resuming an item
│   ├── release.md              # read at Captain gate
│   ├── agentpost.md            # read at setup/troubleshooting
│   └── apparatus-change.md     # read for structural proposals
├── roadmap.md
├── specs/                      # zero or one live *.md by default
├── archive/
└── decisions/
```

Always read:

1. `playbook.md`
2. `PROJECT-BOARD.md`
3. the seat's directive
4. the live specification, if that seat is acting on it

Everything else is read only when the board, directive, or current transition cites it.

## Recommended implementation order

### Pass 1 — Correctness

1. Define the authority matrix and field ownership.
2. Replace the status list with the explicit state machine.
3. Specify the exact code/bridge pairing transaction.
4. Correct shared-root AgentPost identity and join instructions.
5. Replace the permission claim with scope-versus-enforcement language.

### Pass 2 — Compression

1. Reduce `playbook.md` to the always-needed constitution.
2. Extract trigger-loaded protocols.
3. Remove duplicated rules from directives.
4. Make the board genuinely bounded.
5. Default to one active item and one delivery lane.

### Pass 3 — Execution

1. Add a real template tree and idempotent scaffolder.
2. Add structural validation and rendering tests.
3. Commit both scaffolded repositories.
4. Record method provenance and define the upgrade workflow.

## Bottom line

If only three changes are made, they should be:

1. **Explicit authority and transition ownership.**
2. **A small hot-path playbook with trigger-loaded protocols.**
3. **Executable, validated scaffolding and repository pairing.**

Those changes would make AgentBridge feel less like governance documentation and more like a
small, dependable operating system for agent work, without losing its central intentions or
distinctive voice.
