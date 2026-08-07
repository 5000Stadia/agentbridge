# AgentBridge — Fleet Trial Upstream Findings Ledger

**Source:** independent method monitor `abr`, delivered 2026-08-07 at trial close.
**Board at rest:** `66ffdaf0471bea9c3b5509a92b1e253eaba3b211` · project `fleet` wound down, bet answered.
**Companion to:** the after-action report (artifact) — this is the actionable backlog for the method's next version.

Two entries (E-003, E-035) are **honest tombstones** — no durable finding existed at those numbers, and the auditor preserved the gap rather than invent history to make the sequence look complete. That refusal is itself the method's discipline applied to the audit.

---

## Verdict

**COMPLETE AND ROOT-CAUSED.** Governance correction proved and its controlling mechanism found (E-045). Value demonstrated in specification plus executed falsification. Structural safety proved to require an external enforcement boundary (E-046). The mail-state derivation is DESIGNED and sound, not run. A running artifact was not reached and was **correctly not forced**. Measure honest throughout at `0/4 · 0/N · 0/M`. Fleet code remained the untouched scaffold at `02af6f6`.

**Evidence anchors:** initial spec `bea0687` (295 lines / 3,148 words) → terminal spec (1,098 lines / 12,258 words) across eighteen-plus never-green revisions. E-045 finding `2535196`; ER-012 `03dc83e`; clean build stop `c416f36` and hold `0bc1524`; terminal board `66ffdaf`.

## Three-lens synthesis

1. **Cold-seat execution worked and was valuable.** A cold Navigator booted from the bridge; a cold Reviewer repeatedly found *executable* counterexamples, not stylistic objections; the Navigator refused an authority violation; the Implementer stopped and handed a fork upward. Coldness exposed routing, lifecycle, ownership, and provenance gaps that warm shared context would have concealed.
2. **Context weight was earned only when it closed a real boundary** — startup syscalls, aliases, inherited descriptors, mutation routes, provenance, exact coordinates, current-authority replacement. It was *not* earned when a live contract and its archaeology shared one spec, when normative statements were duplicated, or when apparatus prose named mechanisms that did not exist.
3. **The recurring friction was physical.** A sound sentence did not create a trigger, lock, allocator, staging boundary, atomic handoff, or external privilege boundary. **The next method version should treat every consequential noun as an executable obligation: where does it fire, who owns it, what artifact carries it, and what witness proves it?**

---

## Prioritized backlog

**P0 —** Adopt ER-012 at every revision; externalize safety enforcement; make authority transitions and review handoffs full-SHA, complete-artifact, atomic, and capability-enforced; isolate shared git provenance.

**P1 —** Upstream ER-001/003/004/005/006/009/011; route every obligation into a mandatory trigger/read; adversarially read assignments after shaping; separate current truth from append-only history.

**P2 —** Machine-manifest scaffold files; normalize launch/lifecycle packets; add the Display column; qualify cross-project return routes; lint structured Markdown; scope safety adjectives; reserve immediate mail for blockers.

---

## The ledger

| ID | Finding | Upstream fix candidate |
|---|---|---|
| **E-001** | Build-directive parsing is structurally fragile — prose FILE sections, no manifest or expected count. | Generated manifest (paths, counts, hashes/schema) + parser/lint witness that directive and manifest agree. |
| **E-002** | Durable scaffolding precedes the value gate; Fleet spent 18+ never-green revisions while the code repo correctly stayed empty. | Split setup into a minimal reversible Chart bootstrap and a post-value scaffold; require the cheapest falsifier and an explicit value gate before full apparatus. |
| **E-003** | *Tombstone — no durable finding. Gap preserved, not backfilled.* | Reconcile only from Captain-side evidence; never invent or renumber to look complete. |
| **E-004** | Template policy wore the costume of a value (`private by default` populated a cell that should have stayed empty). | State policy in prose; leave the value cell visibly empty until the Captain's exact answer fills it. |
| **E-005** | Launch/readiness/lifecycle/takeover underspecified as one act; Reviewer QUEUED then needed a replacement runtime to ARM. | Every launch packet carries command, root, identity, directive, mailbox, doctor/armed witness, and exact replacement/takeover procedure. |
| **E-006** | Cold Navigator boot passed, but the Seats table lacked the required Display column the boot demanded. | Add Display upstream; keep transport state optional and separate from durable identity. |
| **E-007** | Return routing must be qualified — a bare cross-project seat name can't safely identify the destination. | Include the canonical project-qualified reply route in every cross-project packet and notification. |
| **E-008** | Bare launch and managed relaunch are different operations; a resolvable mailbox can stay unarmed. | Document/emit separate join, attach, resume, relaunch, takeover commands with post-action doctor/armed asserts. |
| **E-009** | Prompt-only protection is bypassable; protected artifacts were mutated by seats whose prose forbade it. | Move ownership/immutability into fail-closed staging/write guards or isolated worktrees; prose is explanation, not enforcement. |
| **E-010** | The cold adversarial map gate paid for itself — caught the "absent means dead" class before code. | Retain the cold map gate; make its exact artifact set and completion witness part of the transition. |
| **E-011** | The board booted cold correctly, then began accumulating history in current-state authority. | Enforce present-tense fields, stable pointers to history, size thresholds, mechanical split rules. |
| **E-012** | An obligation outside a mandatory reading path is a hope — the pre-Reviewer apparatus audit was unreachable. | Every obligation names its trigger, owner, artifact, and required read in an authoritative transition. |
| **E-013** | The method attacked deltas before approval but not owner assignment after; a top-severity sort defect slipped in post-green. | Add an adversarial assignment/readiness gate after owners/reservations are written, before a row is eligible. |
| **E-014** | Roadmap tables were syntactically fragile under live edits; a Markdown table broke the map. | Lint tables at commit, or replace critical rows with schema-validated structured data rendered to Markdown. |
| **E-015** | "Append-only" defined no lifecycle; two seats independently treated filling a placeholder as non-rewriting. | ER-005 — append FINDING and DISPOSITION as separate stable-ID events; no placeholders, supersede don't rewrite. |
| **E-016** | Nonblocking traffic starved the falsification seat; immediate receipts delayed two critical Reviewer transitions. | Default routine traffic to idle; serialize dependent follow-ups behind the verdict; reserve immediate for blockers. |
| **E-017** | Ungreen authority leakage needs a fail-closed third state; a red spec's claim changed the Mission. | ER-001 blocks deliberating specs from changing authority; ER-003 marks falsified authority invalid/unknown with a pointer, freezing dependent use until a replacement greens. |
| **E-018** | Positional rule numbers are unstable identities — inserting a rule made "earned rule 2" name two rules. | Allocate stable ER IDs once; never renumber or reuse; order independent from identity. |
| **E-019** | A live contract and its archaeology can't share one artifact; 1.1.1 grew 295→703 lines carrying red-history. | ER-004 — normative spec + append-only sibling ledger travelling together through review/green/archive. |
| **E-020** | "Read-only forever" was unscoped — subject, boundary, interval, allowed mutations, proof, residual all unstated. | Every safety adjective names subject, boundary, interval, allowed mutations, proof mechanism, residual limits. |
| **E-021** | Shared-worktree provenance silently crossed seat ownership; Navigator commits captured 68 lines of Implementer work. | ER-006 pathspec-only commits + precommit status/owner checks; isolated worktrees/indexes at scale. |
| **E-022** | Cold executable review earned real weight, but the spec bore all of it (18 reds, terminal 1,098 lines). | Preserve executable review; bound the normative artifact via ER-004 and the per-revision value/growth gate. |
| **E-023** | Exact-ID mail handling failed when claiming wasn't part of the start act — a stale unclaimed red was served. | Make exact-ID notification → read → `next --message-id` one workflow; forbid blanket `next` when IDs are supplied. |
| **E-024** | ER-005 initially required an impossible self-SHA (a disposition row can't contain its own commit's hash). | Cite the implementation/evidence commit; let containment identify the record commit; never require self-prediction. |
| **E-025** | Revision 7 showed the value of whole-guard semantic reconciliation over one-sentence patches. | Require a named invariant sweep and one governing count/source before every handoff. |
| **E-026** | Reviewer mutation recurred despite clear role prose — protected artifacts written three times. | Give review a verdict channel + mechanically read-only repo capability; deny direct and transitive protected-tree writes. |
| **E-027** | A mechanism was claimed by naming a wrapper that did not exist (ER-007). | Any mechanism claim ships an executable path and witness output; otherwise tag it DESIGN explicitly. |
| **E-028** | ER-006 prose failed after adoption; a check-authored board edit was swept into a build commit. | Enforce ownership in staging/commit hooks; reject other-seat dirt; isolate index/worktree. |
| **E-029** | Current authority can self-contradict when related artifacts move under separate locks. | Lock the complete authority set for a transition, or compare-and-swap against pinned full SHAs. |
| **E-030** | Mutable-path spec handoff blurred artifact identity; the Reviewer falsified a snapshot the artifact had left. | Atomic full-object handoff for the complete spec+ledger set; explicit writer/reader capability; ownership checks at transition. |
| **E-031** | Protected-tree mutation arrived through a transitive allocator, not the seat's own writes. | Apply capability restriction to the whole subprocess tree and scratch allocation; negative witness per protected root. |
| **E-032** | The ER-006 guard header overclaimed its scope. | Derive mechanism docs from tested behavior; enumerate protected operations and known bypass classes; fail claims closed outside them. |
| **E-033** | Cold Reviewer was a positive control; context should be split, not warmed away. | Retain cold falsification; give it a compact normative bundle; route archaeology by stable pointer only when needed. |
| **E-034** | Navigator correctly refused an authority violation (editing frozen D4) and sent the baton up; the change became D5. | Retain immutable-decision semantics, explicit supersession, and authority-conflicts-move-upward. |
| **E-035** | *Tombstone — no durable finding. Gap preserved.* | Stable ledgers tolerate missing numbers better than invented history. |
| **E-036** | Normative duplication drifted under partial correction — same invariant in multiple sections, third instance. | One canonical source per invariant; citations/projections elsewhere; full-tree consistency sweep. |
| **E-037** | ER-009 achieved its first live behavioral pass — the spec-write lock blocked a protected action. | Carry the guard upstream with both pass and deny witnesses; keep scope exactly stated. |
| **E-038** | Scripted edits recurred without postcondition verification — an append matched no anchor; a gate was written but not wired. | Every scripted mutation asserts expected match count and postcondition, then inspects diff/status before commit. |
| **E-039** | Pre-code proof spiral — no value-order trigger fired during red deliberation; 18+ reds, code repo untouched. | Require the cheapest executable falsifier and a delta-against-roadmap check every revision; stop when proof surface outruns the row. |
| **E-040** | An earned correction lived in mail while canonical authority stayed stale (the oldest law, broken by the Captain). | Accepted governance corrections atomically replace canonical authority before any dependent transition; mail is transport, never state. |
| **E-041** | An immutable pin stayed typed prose and produced bad coordinates (a SHA typed before it exists). | Machine-resolve and validate full 40-hex objects and paths at send time; prohibit manual transcription. |
| **E-042** | Reconciliation appended new current truth without removing the old active truth (E-040's own fix half-landed). | Current-authority replacement is atomic and asserts uniqueness/no superseded active block; append-only is for history only. |
| **E-043** | The shipped handoff preflight overclaimed completion — short SHAs, absent sibling ledger accepted, validation split from delivery. | Full 40-hex IDs; complete spec+ledger validation; clean-tree/path tests; validation+delivery as one atomic act. |
| **E-044** | The prospective E-039 gate passed only qualified — governance corrected, but value delivery still pending. | The gate reports both governance fit *and* delivered-value status; "safe to continue" ≠ "value demonstrated." |
| **E-045** | **CAPSTONE — Root cause.** The only growth checkpoint (hold-the-course) fires downstream of a green a growing spec never reaches. | **ER-012** — every revision compares cumulative scope/evidence against the roadmap row; detour is a broken invariant, not a round count; stop and surface before another revision. |
| **E-046** | **Terminal result.** Executed controls proved the observer can't certify its own safety — 21 opens before empty Python; a hardlink and inherited fd 9 read the denied bytes; the policy could unlink a protected file. | Require an external privilege boundary before runtime (namespace/container/separate uid); prove path rights, aliases, inherited fds, runtime tree, process routes, and mutation routes independently. **Treat non-shipment of the unsafe artifact as a successful first-contact outcome.** |

---

## Disposition (auditor's words)

> The method did not fail because the Reviewer found too much. It failed to ask, during deliberation, whether the growing proof still served the smallest value-bearing row. E-045 is the governance mechanism. E-046 is the product-level result. Together they explain why the correct terminal act was to stop before code, preserve the specification as the deliverable, and require an external enforcer before any future implementation.
