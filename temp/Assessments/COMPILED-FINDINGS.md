# AgentBridge — compiled findings, for working through item by item

**Against `bc79ad9`.** Every item from five assessments, woven where they overlap, with each
source named. Nothing here is decided. Each item ends with a blank `**Decision:**` line to fill in
as we go.

## Sources and what each is worth

| Tag | Document | Basis | Evidence class |
|---|---|---|---|
| **[K]** | `ASSESSMENT-kernos.md` | 4 months, 70+ phases, 38 decisions, 5,200+ tests | **Live incidents**, tagged incident/pattern/extrapolation |
| **[PB]** | `FIELD-REPORT-pattern-buffer-2026-07-29.md` | One full day running the loop for real — 3 specs, 4 REDs | **Live incidents**, each citing what earned it |
| **[C]** | `ASSESSMENT-construct.md` | Construct Projector, the exact shape AgentBridge targets | **Live incidents** + fit-test, tagged incident/obs |
| **[WDA]** | `AGENTBRIDGE-WORKFLOW-DESIGN-AUDIT.md` | Design audit of the document | Reasoning from the text |
| **[AB]** | `AUDIT-OPEN-ITEMS.md` | This session's audit + live AgentPost testing | Document analysis + **verified CLI behaviour** |

**Weight incident-grounded claims above reasoning.** Where [K], [PB] or [C] say a rule caught a
real bug, that is stronger evidence than any argument in [WDA] or [AB] — including arguments
against it. Three items below are cases where they disagree; those are marked **⚔ CONFLICT** and
need your call rather than mine.

---

# Triage — added after §1–§2 were worked through

Three refinements collapsed most of what follows, and they compose:

- **One authority model.** *Each seat owns a depth; nothing surprises the depth above it.* Replaced
  a prohibition, a five-row matrix, field-scoped precedence, and a playbook-vs-directive ordering.
- **One escalation rule.** *Would this surprise the level above?* Clarification, fork, reframe and
  detour became routing labels, not four tests. Friction is the second axis; there are two, not a
  growing list.
- **One state machine, no diagram.** Three locations, and *only the Reviewer advances state; the
  Navigator may send it back.*

[PB]'s *workers / shift manager / Captain* framing — which they called a gold mine — is the same
idea as the depth model, so **9.1 is resolved by not doing it**: the mechanism now says what the
metaphor said.

**The governing principle for everything below, from the Captain:** the elegance is inherent in
each role adhering to its directive. Most remaining findings propose machinery to prevent something
that happened once. Rules in the playbook are for what a directive cannot carry — and per [PB],
*every rule that never fires dilutes the ones that must.*

| Disposition | Items | Why |
|---|---|---|
| **Take — they loosen** | 2.5 · 4.3 · 5.1 · 5.2 · 5.3 · 5.4 · 7.2 | Each removes a constraint or a false universal. Roughly a sentence apiece. |
| **Do — one structural** | 4.1 hot path | Four of five sources agree; the item rule-economy most directly demands. |
| **Trim, then take** | 3.1 · 4.2 · 6.2 | Real, but each arrives overbuilt. Keep the incident-backed line, drop the template. |
| **Decide — genuinely open** | 5.5 · 7.1 · 3.2 | No answer follows from the evidence. The Captain's. |
| **Decline** | 2.3 · 6.3 · most of 6.1 | One incident each; the Reviewer's apparatus audit already covers the ground. |

**Order:** loosening batch first — fast, all reduction, and it shrinks what 4.1 has to move. Then
4.1 against a smaller surface. Then the three decisions, which read differently once the method is
lighter.

**Closed so far:** 1.1 (`dc8e7b6`), 1.2 (`0487da9`), 1.3 (`0d005dc`, narrowed `c694dde`/`00b7772`),
2.1 (`53f928b`, consistency `52d6876`), 2.2 (`a8b4af2`), 2.4 (folded into the one rule).

---

# §0 — Confirmed load-bearing. Do not break these while fixing anything else.

Independently validated by live projects. Listed first so that every change below is checked
against them.

| Rule | Confirmed by | The incident |
|---|---|---|
| **"Fixed" names the witness test** | [K] [PB] | [K] an agent self-reported GREEN with a *pristine worktree*, ~96 min lost; fix was `git status --porcelain` grounding "done" in the filesystem. [PB] exercised ~8× in one day; caught a control that passed *pre*-fix and an oracle that passed both ways. **[PB] calls it the most load-bearing rule in the document.** |
| **Instruments get the same scrutiny as code** | [C] [PB] [K] | [C] shipped a green unit never wired; relayed a claimed negative-control not in the tree. [PB] this is what caught a wrong test count. |
| **Pin the suite's executable identities** | [K] [PB] | [K] tool registries drifted 42 dispatched / 27 surfaced / 15 invisible, everything green. [PB] invented an invocation in a worktree; a subprocess test silently loaded a different source tree — reported 1 failure, there were 3. **Nothing went red either time.** |
| **Absent evidence never defaults to the affirmative** | [C] | Their core design bet and the shape of their worst bugs — narrator facts skipping quarantine, a conflicted read silently serving a stale arc. |
| **The board supersedes; a relay cannot amend** | [C] [K] | [C] burned *twice* trusting an optimistic relay before the authoritative message landed. [K] a seat wrote "accepted by the founder" for an authorization never given — caught only by a cross-agent reviewer. |
| **One board, bounded; cite IDs** | [C] [K] [PB] | [K] the analog file grew past its own tooling's read limit and forced mid-task compaction — **unbounded current-state files fail mechanically, not stylistically.** [PB] the project without it had a second authoritative index 20 days stale reading "Open: (none)" with 3 specs live. |
| **The measure counts the bet, never work done** | [K] | Founder rule demoting their own headline number: "5,200+ tests is secondary." Test count looked healthy while invariant coverage was the real question. |
| **Cross-family review** | [K] [C] | [K] Codex reviewer found a real edge-case bug in an improvement the system shipped to itself; YELLOW→YELLOW→GREEN over 2–3 rounds is the *normal* trajectory. [C] `cr` caught real defects. |
| **The push gate** | [C] | **Independently reinvented almost verbatim** as a founder rule, arrived at by correction not design. [C] calls it the strongest confirmation in the document. |
| **Identity comes from the spawn, never the directory** | [K] | Two sibling clones backing two different Discord bots; restarting the wrong one rate-limited the right one. |
| **Two repositories; no scratch in the shareable unit** | [K] | An early run committed spec scratch into the code repo; the bridge split is that rule made structural. |
| **Decisions carry "what would change the answer"** | [K] | Their best-behaving decision record — explicit thresholds that would reopen it, which has since declined repeat proposals *by citation instead of re-argument*. |
| **The seat-vs-subagent test** | [K] | The same cut their whole cohort architecture makes internally. **Independent derivation is the best evidence in that report that it is universal.** |
| **Pause and surface** | [PB] | Stopped a repair mid-flight rather than fixing through; the reviewer later ruled the test they would have edited encoded a deliberate contract. |
| **Map-as-hypothesis** | [C] | Held true even mid-session — an audit found their next big build was smaller than believed and rewrote its scope before a line was written. |

---

# §1 — Factual defects. Fix regardless of everything else.

## 1.1 · The AgentPost release pin may cite a tag that does not exist ⚔ CONFLICT
**Sources:** [K] §1 (incident, mechanically verified) vs **[AB]** (verified on this machine)

[K] checked on 2026-07-28: the directive pins `v1.3.0` and its install URL, but the repository's
newest tag — **local and remote** — is `v1.2.0`. The `curl` would 404 and Muster would halt. [K]
notes the *capability* check passes on their machine, so the capability gate works and only the
version pin is stale, and calls this the directive's own *"a restated value has no update trigger
and will be believed"* failure occurring in its own text.

**But** `agentpost doctor` on this machine reports `PASS package 1.3.0`, and the capability check
passes here too. So either the tag was cut after [K] looked, or the installed package version and
the git tag have diverged.

**This must be resolved by looking, not by reasoning.** If [K] is right, the directive currently
ships a Muster-halting URL.

**Options:** (a) gate on capability alone and describe the release as "install the latest if the
check fails" — [K]'s recommendation, and it removes the restated value entirely; (b) keep a pin
but verify the tag exists and add an expiry/re-test condition; (c) pin an immutable commit or
checksum rather than a mutable tag — [WDA] §8's version.

**Recommendation:** (a), with (c) if a pin is wanted at all. A capability check that already works
makes the version pin pure restatement.

**Decision:**

## 1.2 · `join` with no agent argument is unsafe on a shared root ⚔ CONFLICT
**Sources:** [WDA] §8 vs **[AB]** (verified, but under a condition that hid the problem)

I verified `agentpost join --cli claude` with no positional agent and reported it as accurate —
and wrote *"takes no agent argument — it infers the seat from the root"* into the directive.

[WDA] is right that this is dangerous, and my verification did not test the case that matters:
**Implementer and Reviewer share the project root.** Once two profiles are rooted there, bare
inference is ambiguous and may silently select the workspace default. My test had exactly one
profile on that root. This compounds with the §0 rule *identity comes from the spawn* — which [K]
paid for with two Discord bots.

**Recommendation:** `agentpost join <canonical> --cli <runtime>` explicitly at every seat launch;
bare join only where uniqueness is proven. My directive line needs correcting — it currently
advertises the risky form as the normal one.

**Decision:**

## 1.3 · The Reviewer suggesting fixes collides with "never author what you review"
**Sources:** [AB] §E1, [PB] §2 (incident)

The red protocol you specified has the Reviewer respond with *why + suggestions for resolution*.
The Reviewer directive says under **Never**: *"Author what you will later review."*

[PB] hit exactly this live: *"A reviewer rejected my tiebreak and offered two repairs… I chose,
said so, and asked to be overruled. It was ratified — but it was an architectural decision made by
whoever was typing."*

So the same behaviour is simultaneously the thing you asked for, a violation of a standing rule,
and — per [PB] §2 below (item 2.4) — **the tell that an escalation is needed.**

**Recommendation:** a red may name **direction and constraint**, never supply replacement text.
And per [PB], *the reviewer offering options is itself the signal to escalate*, not a menu for the
Implementer to pick from.

**Decision:**

---

# §2 — Authority and state

## 2.1 · Authority is stated absolutely and practiced conditionally
**Sources:** [WDA] §2, [AB] (playbook-vs-directive precedence undefined)

*"No agent decides"* conflicts with the Navigator declining proposals, the Reviewer issuing
verdicts, and the Implementer choosing technical mechanics. Separately, *"the board supersedes
everything"* is too broad — a status note should not be able to override a seat directive, and
[AB] found nothing orders `playbook.md` against a directive when they disagree.

[WDA] proposes a matrix — Captain: mission, bet, roadmap, structural changes, publication;
Navigator: interpretation, current-state, coherence findings, delegated triage; Implementer:
technical choices inside a confirmed spec; Reviewer: exact-artifact verdicts, never product
authority; Board: records authority, never creates it — plus **field-scoped precedence**, each
board section naming who may edit it, what receipt authorizes a change, and which source is
authoritative.

**Counterweight from §0:** the *relay cannot amend* rule is incident-proven twice over. Whatever
replaces "the board supersedes everything" must keep that property intact. [WDA]'s own distinction
helps: a Navigator relay is not authority; a board entry recording a dated Captain decision with a
receipt is.

**Decision:**

## 2.2 · The Loop is an implicit state machine with unowned transitions
**Sources:** [WDA] §3, [PB] §5 (incident), [AB] §E2

Three convergent observations:

- [WDA]: there are two distinct green events — spec green and implementation green — but the board
  flow had one, and it omitted the coherence read and the push gate. Proposes explicit states with
  every transition defining *who moves it, required evidence, the exact artifact, the failure
  destination, and what permits resumption.*
- [PB]: **"claiming is a move, not a read"** — a read-based pickup is invisible; a move-based one
  announces itself, and a stuck claim is visible from `ls`. Also warns that **binary
  in-folder/archived cannot express round-trips** — a RED'd implementation belongs in neither.
- [AB]: after `bc79ad9`, **three seats can move a spec** (Implementer → `review/`, Reviewer →
  `specs/`, Navigator kicks back, Implementer → `archive/`), so *"only the Reviewer advances
  state"* looks like an invariant but is not one.

**`bc79ad9` already implemented [PB]'s core insight** — the verdict is the move — before that
report was read here. What remains is naming every transition's owner, and deciding the archive
asymmetry (Reviewer archives too, or the asymmetry is written down deliberately).

[PB]'s round-trip warning is unaddressed: where does a RED'd *implementation* live?

**Decision:**

## 2.3 · Authority-bearing files are protected only by prose
**Sources:** [K] §3 (incident)

[K]'s false-founder-acceptance event was a seat amending an authority record. Their deeper fix is
a **constitutional-paths rule**: enumerate the files governing the system's own safety and force
human review on any autonomous edit to them, *because narration-vs-bookkeeping drift is
structural, not malicious.*

AgentBridge's analogs: `playbook.md`, the directives, the board's **Stance** section.

**[K]'s proposed fix is method-consistent and cheap:** the Reviewer's apparatus audit explicitly
diffs those paths, and any bridge commit touching them needs a Captain-confirmed row.

**Decision:**

## 2.4 · The escalation ladder is missing its middle rung
**Sources:** [PB] §2 (incident)

The existing test — *would answering this change the roadmap?* — has only two heights. [PB] found
a third in live use:

- **The spec didn't pin a detail** → back to spec, mechanically, no approval — **but written
  down**, or the spec now describes something the code does not do.
- **The repair has more than one shape, and the shapes differ in what they add to the system** →
  Navigator, **even when the roadmap is untouched.**

**The tell, which is easy to apply: the reviewer offered options, or you found yourself choosing.**

Directly connected to 1.3 — the same reviewer behaviour is the escalation trigger.

**Decision:**

## 2.5 · The detour rule stops work it should only log
**Sources:** [PB] §3 (incident — three detours in one day)

The cost is not surfacing a detour; it is **stopping work until the Captain rules.**

- **Detour by growth** — an item consuming without completing → **stop.** The interrupt is the
  point, since only the shape across sessions reveals it.
- **Detour by discovery** — something small and unrelated found in passing → **log and carry to
  the push gate**, where the Captain is deciding anyway.

Gate for "log and continue" is the directive's *existing* skip-review test — introduces no
invariant, crosses no boundary, touches nothing green — plus **if the detour is bigger than the
thing it interrupted, stop.** Safeguard: the Reviewer sees the diff and may rule retroactively
that a detour should have stopped.

[WDA] converges from the other direction: Navigator declines are *visible triage dispositions
under delegated rules*, not final decisions.

**Decision:**

---

# §3 — Contracts: making "green" mean something

## 3.1 · No minimum spec contract, and no verdict contract
**Sources:** [WDA] §4, [PB] §1 and §4 (incidents)

The method is meticulous about *reviewing* specs and never says what one must contain. [WDA]
proposes: roadmap item and purpose; scope and non-goals; public-surface impact; invariants and
failure policy; acceptance and witness tests; dependencies and migrations; rollback; open
uncertainties; and the four receipts.

Verdicts should name the immutable commit or tree reviewed, tests and adversarial probes run,
unverified areas, must/should/minor, and whether anything changes the public surface.

[PB] adds two from live runs:

- **§1 — a verdict states what each finding changes outside this repository, including "nothing."**
  A host consumed their atomic-commit surface in production; every verdict since carried an
  explicit internal-vs-public ruling, which let them answer a consumer *in the reviewer's words*
  and correctly **withhold** a notice where nothing had moved. Paired with a **board row naming
  actual consumers and what they coupled to** — [PB] is explicit: *"the rule without the board row
  is ceremony; the row without the rule means nobody is obliged to answer it. Both, or neither."*
- **§4 — a claim of "N passed" cites the invocation that produced it**, and invocation variants
  (worktree, CI, subprocess isolation) are checked in too, never improvised. This is the extension
  of a §0 rule, earned by the incident where a suite *reported a real number about the wrong
  artifact*.

**[WDA]'s framing is the summary:** this makes green *a reproducible claim rather than a
conversational state.*

**Decision:** Settled 2026-08-05 by live smoke test — a five-round Implementer/Reviewer
deliberation with `abr` on a deliberately contract-free spec (item 6.2). Result: **deliberation is
the contract for content** — every round demanded done-criteria, edges, and mechanics unprompted,
and each red stated its own green condition; the proposed spec template and spec questions are
**dropped entirely**. What five verdicts never carried was evidence about themselves, so the
residue landed: an **implementation green names the exact commit it examined and says in one line
what it did not** (spec greens need neither — the text is the whole object); the **push gate ships
only the tree the green named**, closing checked-not-kept mechanically; and the [PB] pairing is
**row-triggered** — verdicts rule per-finding external impact only once a consumers row exists,
which happens when the first real consumer does. [PB] §4's invocation rule was found already
covered by the standing suite-identity/denominator rules.

## 3.2 · The two-repository commit transaction is undefined
**Sources:** [WDA] §6

Code commits pin bridge commits, and a "release manifest" is mentioned but never given a location,
owner, trigger or template. The push-gate sequence does not define when the spec is archived, when
each repo commits, or which exact code artifact was approved.

[WDA]'s proposed sequence: Reviewer greens exact tree `C` → Captain approves `C` → bridge archives
the spec and records receipts as commit `B` → the code repo records `B` without changing the
reviewed tree (an annotated pairing tag on `C`) → verify the `C ↔ B` receipt → push.

Also: **the scaffolder makes an initial commit in the bridge only**, leaving the project doormats
uncommitted.

Relevant to [AB]'s parked `pre-push` idea, which depends on exactly this pairing being well-defined.

**Decision:**

---

# §4 — Weight on the hot path

## 4.1 · The always-read layer is too heavy
**Sources:** [WDA] §1 and §8, [AB] §B5 and §E4, [PB] §6, [C] §5

The most-agreed item in the set — four of five sources, from different directions.

- [WDA]: playbook ≈ 6,655 words; every seat reloads AgentPost installation, naming, wiping, Chart
  procedure, release handling, philosophy and failure history **every session**. Cut to ~100–150
  lines; move cold procedure to `protocols/{chart,item-loop,release,agentpost,apparatus-change}.md`,
  read only when a trigger fires. Directives should hold *only the differences between seats*.
- [AB]: measured ~10–11k tokens per Navigator session, **~80% of it the playbook**; and ~90 of the
  AgentPost section's 173 lines are boot-only. (Restructure mapped, deliberately not applied.)
- [PB]: 1,172 lines, ~15 standing rules, 7 failure modes. *"Agents follow short imperatives with a
  named consequence far more reliably than long prose, and every rule that never fires dilutes the
  ones that must."* Suggests running the Reviewer's own apparatus audit on this document early,
  and that new rules land as **one imperative plus the incident that earned it** — the form the
  existing failure-modes section already uses well.
- [C]: names accretion as their actual disease, and calls the bounded board / read-because-cited
  model **the highest-value item in the document for them.**

**Note the irony all four point at:** the method's headline failure mode is *governance outrunning
the governed*, and its own hot path is the largest instance of it.

**Decision:**

## 4.2 · The board is bounded in claim, unbounded in two places
**Sources:** [WDA] §5, [K] (incident), [AB] §E5

[WDA]: `Declined proposals` grows indefinitely and retired-row tombstones accumulate. Also
*"decision values live only here"* contradicts `decisions/` containing what was decided. Proposed
split — **board:** current effective state, open decisions, *currently challengeable* declines;
**`decisions/`:** durable decisions, rejected alternatives, reopen conditions; **roadmap/archive:**
retired pointers and outcomes.

[K] makes this urgent rather than tidy: their analog **exceeded its own tooling's read limit and
forced a mid-task compaction.** Unbounded current-state files fail mechanically.

[AB]: the `In flight` row still asks for a status that `bc79ad9` made the directory's job.

**Decision:**

## 4.3 · The Chart is heavy before the first artifact
**Sources:** [C] §8 (obs), [AB] §B8

[C]: standing up the full Chart — six extractables, measure, founding rules, end-to-end map, seat
question — is *itself* a substantial governance act before any artifact exists. What actually
carried Construct was a lighter subset: CLAUDE.md + persistent memory + AgentPost + the push gate.

- **Option A (their recommendation):** a **minimum viable bridge** entry ramp — board + doormats +
  push gate + one merged implementer/reviewer directive — graduating to the full Chart *when the
  first artifact exists*. The method's own asymmetry argues for starting minimal and earning weight.
- **Option B:** keep the full Chart, but mark its heavy outputs (`decisions/`, `phases/`, harness
  cadences) **deferred-until-triggered** rather than Chart-exit requirements.
- **Guardrail [C] insists on:** the **measure is non-deferrable** — it is the one cheap anti-drift
  mechanism and exactly what a lite variant would skip.

**Decision:** Broken into four judgements, settled 2026-08-04. (1) **Option B** — no lite mode, no
graduation event; deferral-until-triggered is the rule the method already uses everywhere, plus a
defer-with-residue valve: an extractable the Captain explicitly defers becomes an open-decision
board row. (2) The merged implementer/reviewer directive from [C]'s ramp is **declined** — checks
are never deferred; cross-family review is the most-confirmed rule in the evidence base, and muster
is already cheap. (3) The six extractables stay required — trimming saves less than a tiering rule
costs, and the residue valve covers per-project judgement. (4) The measure stays non-deferrable but
is **`HYPOTHESIS` until first contact**, same convention as the map. Two additions surfaced during
this item: **the bet resolving — proven as much as killed — reopens the Chart** (a satisfied
measure is a dead instrument; live-ops/maintenance is a new bet or a deliberate wind-down), and
**the phase read** — shaping at phase scale: the map is outlined whole but ownerless, and each
phase's rows are re-evaluated and pinned by the Navigator at entry, Captain approving deltas. The
empty Owner column is the enforcement; no new gate.

---

# §5 — Claims of universality that the evidence does not support

## 5.1 · "First contact first" is a domain boundary stated as a law
**Sources:** [C] §6 (incident), [K] (pattern, agrees with the rule)

[C]'s arc/destination layer — *the project's actual contribution* — exists because they
pressure-tested it on paper before any code, by explicit mandate. AgentBridge would read that as
governance outrunning the governed. Their honest reading: **paper-falsification is cheaper than
code for a genuinely novel design surface with no prior art, and more expensive everywhere else.**
They add a caveat against themselves: they *also* accreted badly, so the rule is not wrong — only
its claimed universality.

- **Option A (their recommendation):** redefine first contact as *"the cheapest falsification of
  the core assumption"* — usually a running artifact, **but on-paper (spec + adversarial review to
  green) when the assumption is a design claim no code would test faster."* One sentence in the
  Chart, no new machinery.
- **Option B:** a `paper-falsifiable` tag on roadmap items, parallel to the existing
  *downstream of first contact?* column.

**Decision:**

## 5.2 · Push-gate cadence is a constant that should be an extractable
**Sources:** [K] §3 (incident), [AB] §B4, [C] §1 (validates the gate itself)

The gate is confirmed load-bearing (§0). Its **rigidity** is the finding.

[K] lived both regimes: per-completion check-ins made founder attention the scarce resource and
produced "should I keep going?" pauses costing hours, spawning three rules to kill them
(continue-without-checkpoint-pauses, no-pausing-for-pacing, named autonomous-push criteria — three
triggers require a decision, everything else pushes). Later, for employer-owned repos, they
*reversed* to never-commit-without-explicit-go. **Both regimes are named-trigger cadences chosen
per repo and risk level.**

[K]'s generalization: cadence moves with **trust maturity × Captain bandwidth**. Per-completion is
the right *starting* default, but the directive should say it expects to be renegotiated — *"or
teams will treat the bottleneck as virtue."*

[AB] independently: throughput is bounded by one human and this is never stated as a cost.

**Decision:**

## 5.3 · The bridge's mandatory privacy fights showcase and research missions
**Sources:** [C] §7 (incident)

Construct's design record lives in the **public** code repo on purpose — the project's stated job
is to showcase the substrate, and the design narrative is part of the artifact. An always-private
bridge would hide the very thing being demonstrated.

- **Option A (their recommendation):** decouple *separate repo* (keep — the boundary hygiene is
  real) from *private* (make it the **Captain's per-project call**, exactly as code visibility
  already is). The method's own *no personal material, enforced at write* rule already makes a
  bridge safe to be public.
- **Option B:** for showcase projects, a public bridge doubles as the design-story artifact — a
  feature rather than an exception.
- **Explicitly avoid:** splitting the narrative (public docs in code, private board in bridge) —
  that reintroduces the split-brain the method rightly warns against.

Related: [WDA] §9 asks what "private" even means — unpublished, access-controlled, owner-private on
disk, or all three.

**Decision:**

## 5.5 · The gate governs `push` and nothing else — no policy for merge, PR, tag or release
**Sources:** Captain (this session), [K] §3 (incident), `cx` (a working model, observed live)

**Decide together with 5.2** — that item is *when* the gate fires; this one is *what it covers*.

The push gate names exactly one operation: *nothing reaches the code remote without the Captain's
approval.* The method says nothing about **merging a PR, opening one, cutting a tag, publishing a
release, deleting a branch, or force-pushing** — all of which reach the remote, several of which
are harder to reverse than a push, and none of which the Implementer is told to stop at.

**A working model already exists in this workspace.** `cx`'s release discipline, observed this
session, is exactly the shape this item wants: *reviewed SHA to main → exact-head CI → annotated
tag → GitHub release*, plus a standing refusal — *"I will not place a release tag on an unmerged
draft… publishing therefore needs an explicit user decision."* Named steps, named order, and one
point where a human decides. AgentBridge has no equivalent for any operation.

**[K] supplies the evidence for how such a policy matures.** They lived both extremes:
per-completion approval made founder attention the scarce resource and produced "should I keep
going?" pauses costing hours; the fix was **named autonomous-push criteria — three triggers
require a decision, everything else pushes.** Later, for employer-owned repos, they reversed to
never-commit-without-explicit-go. **Both regimes are named-trigger policies chosen per repo and
risk level**, not opposite philosophies.

**So the shape the Captain wants:** start at approval-for-everything, and expect to move to
*auto-approve except X*, where X is a **named list** rather than a judgement call. The list is the
whole design — a gate that says "escalate when it seems important" is not a gate.

Candidate triggers for X, to argue over rather than adopt: anything touching a public surface;
anything the Reviewer flagged as changing behaviour outside the repo (see 3.1); force-push or
history rewrite; tag or release; first push of a new branch; anything touching the
authority-bearing paths in 2.3; a spec that reached revision three.

**Open questions this item has to answer:**
- Which operations are gated at all, and which are simply the Implementer's?
- Is the policy per-repository? [K] ran different regimes for personal and employer repos.
- Where does it live — a board row, so it can move without a structural change? That would make
  the current per-completion default an *extractable with a recorded value*, which is 5.2's answer.
- Who may change it, and does a change need a `decisions/` file? It voids prior practice, so
  probably yes.

**Decision:**

## 5.4 · The measure may not be countable in every domain
**Sources:** [C] (least-confident item), [WDA] smaller refinements, [K] (validates the principle)

[C] is unsure whether a craft-quality domain can have the countable measure the method leans on —
their real distance (fiction quality, genre-shapes proven end-to-end) is **judged, not counted.**

[WDA] proposes the resolution: replace *"the bet implies a number"* with *"the bet implies an
outcome indicator"* — prefer a count with a denominator, but allow a **falsifiable observation
protocol** where forced quantification would create a misleading metric.

[K] confirms the underlying principle is right (count the bet, never the work).

**Decision:**

---

# §6 — Mechanisation

## 6.1 · Nothing in the method is executable or validated
**Sources:** [WDA] §7, [AB] §B1

[AB]: no hook, CI check, lint, schema or script anywhere; several claims assert enforcement that
does not exist — the measure *"needs nobody to do anything"* (it is computed by hand), and
`decisions/` premise triggers *"re-checked mechanically"* (nothing watches them).

[WDA] goes further: a 1,300-line instruction asking an agent to reproduce embedded files
"verbatim" while substituting placeholders is **fragile**. Store a real template tree and provide
an idempotent scaffold command that validates: two sibling git roots; both initial commits;
visibility and remote recorded; **no unresolved `<project>` placeholders**; each AGENTS/CLAUDE pair
identical; no unexpected project files; **slot occupancy means "number of live `*.md`", not literal
directory emptiness despite `.gitkeep`**; clean worktrees.

That `.gitkeep` catch bites the new `review/` and `specs/` slots directly.

Both converge on a small checkable script; [WDA] wants the scaffolder itself replaced.

**Decision:**

## 6.2 · "Blocked is announced" assumes the blocked seat is alive
**Sources:** [K] §3 (incident), [PB] §5

[K]'s actual blockages were **silent deaths**: an improvement attempt dead ~2 hours before anyone
noticed; a review subagent that reliably hangs past 5 minutes; background handoffs that never
return. Their fixes were mechanical — a stall monitor at 720s, every poller capped at ~10 min and
re-armed.

**The key observation: AgentPost's ARMED proves the *notifier* is live, not the *turn*.** [AB]
verified ARMED end-to-end this session, which does not touch this at all.

[K]: the structure needs one mechanical liveness trigger it owns — a stall threshold on the
in-flight spec's last status movement — *because the seat that most needs to announce is the one
that cannot.* [K] flags the right shape as their biggest guess.

[PB] supplies half the answer for free: with move-based claiming, **a spec sitting in a claimed
location with an old timestamp is a stuck claim visible from `ls`.**

**Decision:**

## 6.3 · The apparatus audit checks rules that never fire, not rules that misfire
**Sources:** [K] §3 (incident)

[K]'s abuse-escalation ladder blocked the system's **own internal sender**, silently
short-circuiting every autonomous plan step until someone noticed uniform 22-byte responses.

*"A rule firing on an unanticipated subject is the more expensive failure."* One line added to the
audit's checklist.

**Decision:**

---

# §7 — Where the sources disagree

## 7.1 · One spec slot: liberating or serializing? ⚔ CONFLICT
**Sources:** [K] §4 (extrapolation) vs [WDA] §5

- [K]: *"`specs/` as a single slot serializes the heartbeat."* They ran approved **multi-spec
  batches end-to-end productively**, and predict this is the first structural change a productive
  project proposes. Flagged as extrapolation, and as one of their two biggest guesses.
- [WDA]: default to **one active item**; multiple Implementers should require explicitly enabled
  lanes with separate ownership and ordering, *otherwise "one slot per Implementer" introduces
  bridge write races and speculative parallelism the method otherwise tries to prevent.* For a
  small project: one delivery lane plus freely spawned bounded subagents.

Both agree the current text is under-specified. They disagree on the default.

**Decision:**

## 7.2 · Scope versus enforcement
**Sources:** [WDA] §9

*"Pointing a seat at a folder is its permission"* describes **intended scope, not a security
boundary** — a local process can typically read sibling directories regardless of cwd. [WDA]:
rename the field to **intended scope**, and if confidentiality or write isolation is genuinely
required, use real enforcement (sandbox rules, OS permissions, separate worktrees or accounts,
scoped credentials, a denying tool boundary).

Listed here because it interacts with 5.3 — what "private" means — and because [AB] made the same
class of error about hooks (they stop accidents, not determined processes).

**Decision:**

---

# §8 — Smaller items

| # | Item | Sources |
|---|---|---|
| 8.1 | **Method provenance and upgrade path.** Record the AgentBridge base commit, local apparatus decisions, AgentPost capability receipt, and last-reviewed upstream revision. Upgrades become three-way reviews preserving intentional local decisions. Divergence is expected but unrecorded. | [WDA] §10 |
| 8.2 | **Two files named `boot.md` with opposite lifetimes.** The project one deletes; a seat one would not. Rename the seat file (`directives/spawn.md`). Principle worth stating once: *a file deletes itself when its trigger can only fire once.* | [AB] §E3 |
| 8.3 | **Cross-spec correctness has no owner**, and *"read only what is cited"* holds only if roadmap rows actually cite what they need — [K] found spec execution always needed standing architecture context beyond the one row, so the rule gets *quietly violated rather than obeyed*. | [AB] §B2, [K] §4 |
| 8.4 | **Signing every message duplicates AgentPost's `From` header.** Trust the header; use exact Message-ID claims and replies as the workflow receipt. | [WDA] §8 |
| 8.5 | **"Nothing personal" versus the board asking for the Captain's own name.** Prefer a Captain-chosen display name; prohibit secrets explicitly. | [WDA] smaller, [AB] |
| 8.6 | **Timebox prior-art research in the Chart** so "locate the bet" cannot delay first contact indefinitely — and name who does it, since no seat is equipped or assigned. | [WDA] smaller, [AB] §B7 |
| 8.7 | **Keep the metaphors, pair each with an operational definition.** Chart/Muster/Loop/Harness are memorable and should not carry contract details by implication. | [WDA] smaller |
| 8.8 | **The four doormat files must stay identical with nothing syncing them** — an equality check in the validation script. | [AB] §B6, [WDA] §7 |
| 8.9 | **AgentPost has no degraded mode.** Muster *stops* if the release is unavailable. One paragraph naming a hand-relay fallback removes the only hard external stop. | [AB] §B3 |
| 8.10 | **The `send` defect is unreported**, and twelve existing boxes remain on the legacy address form. | [AB] §C1–C2 |
| 8.11 | **"Every seat reads four things"** is now five with `boot.md`. | [AB] §E5 |

---

# §9 — One addition, not a fix

## 9.1 · The organising intuition belongs in the playbook
**Source:** [PB], attributing it to the Captain

> **Implementer and Reviewer are the workers** — they deliberate together before detonating
> explosives or carving a fresh wall, and settle the best shape between themselves. **The Navigator
> is the shift manager**, answerable for what was done and why, and for the operation's forward
> movement; work scales back to them when it needs deeper consideration than two workers should
> settle. **The Captain** gets anything that risks the mission or changes the shape of the entire
> operation.

[PB] calls this *"a gold mine"* and says it **makes the tiering intuitive rather than procedural** —
and assumes it as the frame for their entire report. It is also the natural home for the missing
middle rung in 2.4.

**Decision:**

---

# §10 — From working sessions, in no assessment

Ideas and verified facts that came out of this session rather than any of the five documents.
Marked **[done]** where already committed, **[staged]** where mapped but deliberately unapplied,
and **[idea]** where nothing exists yet.

## 10.1 · A file deletes itself when its trigger can only fire once **[done + staged]**

`boot.md` **[done, `bc79ad9`]** holds the project's one-time setup and is deleted at the Chart's
exit. The property that makes it more than tidying: **its presence means setup is unfinished, its
absence is the receipt that it finished** — state carried by the filesystem rather than asserted
on the board. It also removed ~10 lines from the Navigator directive that were re-read every
session to describe work that happens once.

The **seat-level spawn file** **[staged]** is the same shape with the opposite lifetime: seat setup
fires again for every new instance, seat type, and machine, so it must persist. It would absorb
the AgentPost wiring — which is also the largest cold block on the hot path (see 4.1, where ~90 of
173 lines are boot-only).

**The general rule is worth stating once and applying beyond these two files:** anything whose
trigger fires exactly once should be deletable, and its deletion is the receipt. See 8.2 for the
naming collision this creates.

## 10.2 · The location is the status; hand off by path **[done]**

`bc79ad9` made the Reviewer's green *be* the move from `review/` to `specs/`. Two generalizations
came out of it that outlive the specific change:

- **Never restate in the board a status the directory already gives.** Applying it deleted most of
  the old `PROPOSED → DRAFT → DELIBERATION → CONFIRMED → …` flow, leaving only what the filesystem
  cannot show. This is the same economy as *cite, never restate*, applied to state instead of
  values.
- **Hand off by path, never by content.** Folded into the existing *cite, never restate* rule
  rather than added as a new one — the cheapest way to add a rule is to widen one that already
  exists.

Note the convergence: [PB] §5 proposed move-based claiming independently, from a live run, before
that report was read here.

## 10.3 · Runtime hooks: the portable form is script-as-contract, hook-as-trigger **[idea, pinned]**

Both Claude Code and Codex have lifecycle hooks with near-identical shape — Codex uses
`[[hooks.PreToolUse]]` with a sibling `hooks.json`, `/hooks` to inspect, and plugin-bundled hooks.
So hooks are not inherently a platform dependency, **but a hook-enforced rule covers only the seats
whose runtime has them**, and a rule that looks enforced while silently skipping one seat is worse
than an unenforced rule.

**The split that keeps it neutral:** enforcement lives in **git hooks and plain scripts** — they
fire for every runtime and for the Captain at the keyboard — and runtime hooks are a **thin trigger**
that runs the same script earlier. The script is the contract; the hook is convenience.

Pinned at the Captain's direction. Detail in `../CLAUDE-CODE-INTEGRATION-NOTES.md`.

## 10.4 · Live board invalidation **[idea, pinned — the most interesting one]**

Claude Code's `SessionStart` can return `watchPaths`, and `FileChanged` then fires when a watched
file changes on disk. Pointed at `PROJECT-BOARD.md`, that means **a seat mid-session is told the
board moved under it.**

This addresses a failure the method names and has no mechanism for — *the relay amending reality*,
a directive enforced after its premise died. Today a long Implementer session works from the board
it read at boot, and a Captain decision landing mid-session reaches it only if someone messages it.

Unverified: whether `watchPaths` accepts paths outside the project root, which the sibling-bridge
layout requires. Platform-specific, so subject to 10.3.

## 10.5 · The measure on the status line **[idea]**

The playbook claims the measure *"needs nobody to do anything and cannot be unseen."* Today it sits
in a file someone must open. ~10 lines parsing the measure row onto a status line makes the claim
literally true rather than aspirational — the only item here that makes an existing claim true
instead of adding capability. Cheap enough to do whenever it's enjoyable rather than justified.

## 10.6 · Subagents have a native home in both runtimes **[idea]**

The playbook says recurring work, deep domains and accumulating registers are *"a task subagent
with a file to write to."* Claude Code's `.claude/agents/*.md` (and Codex's equivalent) is exactly
that, with model and tool scoping in frontmatter. Right now the seat-vs-subagent test resolves to
an abstraction with nowhere to put the answer.

## 10.7 · Config packaging solves the two-roots problem **[idea]**

The Navigator roots on the bridge; Implementer and Reviewer root on the project. Per-root config
means two copies of one rule, drifting — the *stale parallel descriptions* failure. **A plugin
carries hooks, agents and commands once per machine and applies from both roots**, versioned and
adopted the same way AgentPost already is on this machine. It also keeps runtime-specific config
out of the bridge repo entirely, preserving neutrality on disk even where behaviour is not.

## 10.8 · One `pre-push` check enforces two rules at once **[idea]**

The method already requires that *the code commit pins the bridge commit it implements.* A
`pre-push` hook rejecting any commit without a valid `Bridge: <sha>` trailer therefore enforces
**the pinning rule and the push gate together**, in ~15 lines, for every runtime and for the
Captain's own shell. Depends on 3.2 defining the pairing precisely. Honest limit: `--no-verify`
bypasses it, so genuinely robust means server-side branch protection.

## 10.9 · Verified AgentPost mechanics — moved to their own reference **[done]**

Everything established this session about install, registration and naming derivation, join and
identity precedence, arming, addressing, inbox lifecycle and wipe now lives in
**`../AGENTPOST-REFERENCE.md`**, with each fact marked as run-here, answered-by-`cx`, or untested.

It ends with a **deploy-a-new-seat sequence** and a **re-test-after-upgrade list**, since these are
behaviours AgentBridge depends on and none is guarded by a test we own.

Two facts from it bear directly on items above: the `join` default-precedence trap (1.2, now
fixed) and the `send` address inversion (8.10, still unreported).

## 10.10 · Claude Code ships no manual **[done]**

Unlike Codex, there is no self-documenting `.md` on disk — only `claude --help`, in-session
`/help`, and the online docs. `../CLAUDE-CODE-REFERENCE.md` assembles one, with provenance marked
per source so verified-locally is distinguishable from fetched. Worth knowing that its hook surface
moves between releases (`DirectoryAdded` landed one version before the installed build), so it
should be re-fetched rather than trusted after an update.

---

# Working order

Suggested sequence, not a decision:

1. **§1** — factual defects. 1.1 and 1.2 could halt or misidentify a real deployment.
2. **§2** — authority and state, since §3 and §6 both depend on transitions having owners.
3. **§3** — contracts, which turn green into a claim.
4. **§4** — weight, once the above tells us what genuinely belongs on the hot path. Doing 4.1
   first risks cutting something §2/§3 turns out to need.
5. **§5** — universality, which are mostly one-sentence edits with disproportionate effect.
6. **§6** — mechanisation, last, because it encodes whatever the earlier sections settle.
7. **§7–§9** — as they come up.
