# FIELD REPORT — AgentBridge, from a live run

**From:** `pb` (Pattern Buffer engine seat) · **Date:** 2026-07-29
**Basis:** one full day running the loop for real — three specs, four RED verdicts, one live
downstream consumer, two reviewer-caught defects in my own repairs.

Six changes, highest confidence first. Each cites the incident that earned it. I have made no
edits; this is for the Captain and whoever holds this method to accept, adapt or decline.

Two known gaps are **deliberately excluded** as AgentPost's to fix, per the Captain: reviewer
liveness on a claimed letter, and delivery receipts.

---

## The organising intuition (the Captain's, worth putting in the playbook)

A gold mine. **Implementer and Reviewer are the workers** — they deliberate together before
detonating explosives or carving a fresh wall, and settle the best shape between themselves.
**The Navigator is the shift manager**, answerable for what was done and why, and for the whole
operation's forward movement; work scales back to them when it needs deeper consideration than
two workers should settle. **The Captain** gets anything that risks the mission or changes the
shape of the entire operation.

This makes the tiering intuitive rather than procedural, and it is the frame the rest of this
report assumes.

---

## 1. A verdict states what each finding changes outside this repository

**Add to the Reviewer directive.** One line: *a verdict says what each finding changes for
anyone outside this repository, including "nothing."*

**Add to the board:** a row naming actual consumers and what they have coupled to.

**Why.** A host consumed our atomic-commit surface in production. Every reviewer verdict since
carried an explicit ruling — internal enforcement, or a public-surface move. That let me answer
the consumer in minutes with the reviewer's words verbatim, and correctly *withhold* a notice on
a second track where nothing they touched had moved.

**The rule without the board row is ceremony** — the question gets a shrug. The row without the
rule means nobody is obliged to answer it. Both, or neither.

## 2. Two kick-back heights, with a tell that distinguishes them

The existing clarification/reframe test — *would answering this change the roadmap?* — misses a
middle tier.

- **The spec didn't pin a detail** → back to spec, mechanically, no approval. But **written
  down**, or the spec now describes something the code does not do.
- **The repair has more than one shape, and the shapes differ in what they add to the system**
  → Navigator, *even when the roadmap is untouched*.

**The tell, which is easy to apply:** the reviewer offered options, or you found yourself
choosing.

**Why.** A reviewer rejected my tiebreak and offered two repairs — a canonical composite class,
or rejecting ambiguous rows at the gate. Those have different downstream shapes: one adds a new
gate policy, the other does not. I chose, said so, and asked to be overruled. It was ratified —
but it was an architectural decision made by whoever was typing, which the reframe rule exists
to prevent. The roadmap was untouched, so the existing test waved it through.

## 3. Split the detour rule: growth stops, discovery logs

The cost is not surfacing a detour. It is **stopping work until the Captain rules.**

- **Detour by growth** — an item consuming without completing. **Stop.** Every step was
  individually authorised; only the shape across sessions shows it. The interrupt is the point.
- **Detour by discovery** — something small and unrelated found while passing through. **Log and
  carry to the push gate**, where the Captain is deciding anyway. Nothing hidden; only the
  interrupt deferred.

**Gate for "log and continue"** — the directive's existing skip-review test, unchanged:
*introduces no invariant, crosses no boundary, touches nothing green.* Plus one heuristic: **if
the detour is bigger than the thing it interrupted, stop.**

**Safeguard, because the boundary is self-judged:** the Reviewer sees the diff and may rule
retroactively that a detour should have stopped — the same shape as challenging a decline.

**Why.** Three detours landed in one day: a version constant that had reported the wrong release
for three versions, a stale authoritative index, a publication-hygiene pass. All small, all
verifiable, none touching the roadmap item's shape. Stopping the run three times would have been
ceremony. One of the three — the index — is genuinely borderline, because it changed a document
that claims authority.

## 4. One checked-in invocation, and a count cites it

The directive already says *"pin the suite's executable identities… with one checked-in
invocation."* Extend it: **variants are checked in too — worktree, CI, subprocess isolation —
never improvised.** And **a claim of "N passed" cites the invocation that produced it.**

**Why.** I ran a suite in a git worktree and invented an invocation on the spot, because the
environment did not have one. In-process tests honoured it; a test that spawns a subprocess did
not, and silently loaded a different source tree. Two tests passed that should have failed. I
reported one failure. There were three. The reviewer caught it — and their own verdict was
trustworthy precisely because it named its invocations: *"558 non-stdio, plus the two stdio
tests run separately with the child path pinned."*

Nothing went red. A suite reported a real number about the wrong artifact.

## 5. If a spec queue is adopted: claiming is a move, not a read

A watched folder is a good idea — **the spec's location is its state**, self-describing and
surviving context loss with no board row to go stale. One mechanical requirement makes it safe:

**Claiming is a move.** `ready/` → `active/<seat>/` → `review/` → `archive/`. A read-based pickup
is invisible; a move-based pickup announces itself, and a spec sitting in `active/` with an old
timestamp is a stuck claim visible from `ls`.

Two further notes: binary in-folder/archived cannot express round-trips (a RED'd implementation
belongs in neither), and anything able to write to `ready/` commands implementation.

**Why.** A claim-free queue reproduces the stuck-claim failure in a new substrate. Move-based
claiming turns the filesystem into the liveness signal for free.

## 6. Rule economy — the directive competes with itself

1172 lines, ~15 standing rules, 7 failure modes, 3 seat directives. Agents follow **short
imperatives with a named consequence** far more reliably than long prose, and every rule that
never fires dilutes the ones that must.

The Reviewer already owns this — *"audit the apparatus: rules that never fire, locations nobody
opens, steps routinely skipped. Removal is the easy direction."* Suggest it be run on this
document early, and that new rules land as one imperative plus the incident that earned it,
which is the form the existing "failure modes these rules are receipts for" section already uses
well.

---

## What already worked, unchanged

Reported because knowing what *not* to touch is worth as much:

- **"'Fixed' names the witness test that fails without the change and passes with it."** The most
  load-bearing rule in the document. Exercised ~8 times in a day. It caught two subtleties a
  weaker rule would have missed — a control that passed *pre*-fix, proving a bug was reachable
  only through one path; and an oracle that passed both ways, correctly distinguishing what was
  broken from what was not.
- **"One board; cite IDs."** The project running without it had a second authoritative index
  twenty days stale, still reading "Open: (none)" with three specs live.
- **"Attack instruments as well as code."** This is what caught my wrong test count.
- **Pause and surface.** I stopped a repair mid-flight rather than fixing through, and the
  reviewer later ruled the test I would have edited encoded a deliberate contract.

— `pb`
