# Reassessment — from zero

*Temporary working document. Nothing enters the method from here without earning it against
evidence we actually have.*

## The basic shape, simplest statement

> **A human says what they want, and what "good" means for this project is written where every
> agent can read it. One agent writes the spec and builds. A second agent, wanting the same
> thing, reviews against that intention — the failures a player would hit, and the silent ones
> nobody would notice, including what's missing that "good" implies. The builder addresses what's
> valid and returns, until the review passes. A pass means the work adheres to the human's
> design — that adherence is the whole criteria — so it ships on the pass, and the next spec
> begins. When all the work is done, the final commit ships. The human can look at the live
> thing at any moment; nothing waits on them.**

*Word choice, deliberate: not "adversarial" — the agents share one goal and the opponent is the
defect, not each other. But not soft either: the second agent's contribution to the shared goal
is finding failures, and it cannot make that contribution by agreeing. Rigor is the form its
collaboration takes. It examines what was actually built — never the builder's account of it —
because we proved builders cannot see their own blind spots; that is a fact about minds, not a
suspicion about motives.*

*Silent failure, deliberate: the human may or may not notice what's wrong — the trial's best
catches were failures that looked like normal behavior. So review carries the project's stated
intention of "good" and checks for missed considerations against it, not only for visible
breakage. Absence is a defect class.*

## The review relationship (first earned structure)

The loop: **review happens → the builder reads it → valid concerns get addressed → try again →
repeat until the review passes.** The reviewer names everything it sees each pass, not one thing
at a time.

It runs at exactly two moments:
1. **Right after the spec is written** — evidence: the chord-event catch killed a
   built-broken-while-looking-fine defect before a line of code existed.
2. **Right after the code is fully implemented** — evidence: four consecutive shipping bugs
   passed the builder's own checks and were found only here.

Between those two moments, the builder works alone and in silence.

## The Navigator (second earned structure)

**The Navigator is a program author, not a coordinator.** Its real work is one thing: writing the
vision the other roles execute — granular enough that the builder rarely has to guess and the
reviewer has something specific to measure against. Everything else it does is small by
comparison, and a Navigator spending its effort on coordination instead of authorship has
misunderstood the seat. It appears at five moments and is silent between them:

**It holds that role the whole way through — every moment it acts, it acts by writing the program
more completely.** Nothing it does is coordination wearing an author's coat:

1. **The front door** — writes the program with the human: what they want, what "good" means, and
   the design in granular detail. The largest act of authorship and the one that decides
   everything downstream.
2. **Each handoff** — makes the next section of the program executable: the row a builder can act
   on without guessing, with real coordinates. If it cannot be handed off without explanation,
   the program isn't finished there yet — finish it rather than explain it.
3. **Forks** — the work hit a choice the program does not make. The Navigator makes it, from the
   whole picture, or carries the one question to the human. Either way **the answer is written
   into the program**, in the human's words where they gave them, so that fork is closed forever
   rather than resolved once.
4. **Deadlocks** — builder and reviewer disagree, both demonstrate with artifacts, never argument.
   Almost always the real fault is an ambiguity in the program, so the Navigator's fix is to
   remove the ambiguity, not to pick a winner.
5. **The end** — confirms the shipped thing is the program realised, and that no line of the
   program still describes something the artifact doesn't do.

**It never relays** — builder and reviewer talk directly. **It never narrates** — the program is
its only writing. It reads everything and says almost nothing.

## The intention document (third earned structure)

The front door's product; the yardstick every review measures against. Four sections, one page:
1. **What we're making** — one paragraph, the human's words verbatim where possible. (Translated
   intent steered the trial sideways; quoted intent governed cleanly through every fork.)
2. **What "good" means here** — concrete, checkable qualities, anchored to the most impressive
   real example of the shape when one exists. Review checks what's missing against these words.
3. **What it must never do** — only irreversibility-class harms and product-identity lines.
   Anything that can safely be added later is not founding law.
4. **The spec list** — living; each row one paragraph of current instruction plus what done
   looks like, pointable. History lives in git, never in rows.

Excludes everything else the old Chart carried. Test for any line: would a review ever decide
differently because of it? Single home, changes only through Navigator + human, claims-die rule
applies to it.

## The design blueprint (fourth earned structure)

The intention document is the spine. Beneath it, **for any product with real design space, the
Navigator's front-door work expands into a full design blueprint before implementation** — as
thorough as the product deserves, in the product's own domains, and containing zero process. Not
all projects are games; the sections generalize:

- **What it is and why** — the pitch and the pillars, whatever the domain.
- **How the parts work** — the systems/components/flows, at whatever depth the product has.
- **How it's used** — the interfaces people or machines actually touch.
- **A decision hierarchy** — when constraints conflict, which yields to which. Every fork this
  answers is a human interrupt that never happens.
- **The layering scaffold** — the build order, stated simply: the smallest running whole first,
  then each layer added onto a working thing, each layer with its own testable done. The
  blueprint decides the climb; the build climbs it. This is where simplest-first lives — not as
  a philosophy but as the written sequence, ending in a final end-to-end checklist.
- **Budgets** — the measurable targets the domain cares about (speed, size, cost, accuracy).
- **Out of scope, and risks** — named boundaries, anticipated failure modes.
- Exact values welcome, always with the license: *change it if it makes the product better.*

The blueprint front-loads **decisions, not scope** — phases still build simplest-first and layer.
What's pre-decided is how conflicts resolve and what done means: exactly the things the trial
paid human interrupts to decide mid-flight. Depth scales with the product: a small tool needs
only the one-page spine; a rich product is where this document earns the Navigator its seat.
Thoroughness lives here, in the product — never in process.

## The working practices (fifth earned structure — the complete list)

The process side, whole. Each one sentence, each earned at least twice, each aimed at the work:

1. **A check only counts if it can fail** — delete the thing it guards once and watch it go red.
2. **When a change makes a sentence false, the sentence dies in the same change** — the product
   never lies about itself.
3. **The live thing stays current and the human is always welcome on it** — nothing waits on
   them, but their two sentences have beaten entire harnesses, twice.
4. **Disagreement is settled by demonstration** — a run, a measurement, a counterexample.
   Never by argument.
5. **Communicate tersely** — clear, concise, effective; silence until done; questions out loud
   the moment they block.
6. **Self-check against the definition, not in the abstract**: does this change what ships, was
   it the cheapest way, do the claims match the artifacts — answers only as KEEP, CUT, or
   CHANGE ONE THING.

And the first line of the whole method, before any of it: **if one strong agent could plausibly
one-shot this, do that — build, then fresh eyes on the result, then a human touch. Run the full
shape only when size, stakes, or parallelism genuinely demand it.**

## THE CENTRAL CLAIM (Captain, after seeing both exemplars)

**Two things have proven value: the three roles working in harmony, and an exhaustive unified
vision. They are not two ideas — they are machine and program.** The roles are the machine; the
vision document is the program it runs. This is why the gauntlet worked solo: with a program that
complete, the machine can be one agent.

**Granularity of vision produces harmony of implementation**, and the mechanism is concrete: every
ambiguity left in the vision becomes a fork discovered at implementation time, where it fragments
interpretation, interrupts the human, and costs rounds. In the trial, EVERY human interrupt was
an ambiguity in the vision, never a failure of the roles — board size versus density, the rotation
constraint triangle, presets that looked identical, the phone size boundary. Each was a decision
the vision had not made. Detail spent up front is forks that never happen.

So: **the vision is written to granular, near-implementation depth — a unified specification
approaching a program — while the build still climbs it in layers.** Exhaustive about decisions,
staged about construction. Two guards keep this from becoming its own disease:
- **Exhaustive about the PRODUCT only.** The same page count spent on process is the failure this
  whole reassessment exists to correct.
- **Every specific carries a licence**: exact values, and *change it if that makes the product
  better, and say why*. Detail must not foreclose a better answer the builder can see and the
  writer could not.

## Outside evidence: the three-breath gauntlet (refinements, not additions)

A 60k-line game built in three ~8h uninterrupted runs, exemplary outcome, no crew. What it
confirms and recalibrates:

- **The front door validated externally**: human + AI talked about what he loves → the AI wrote
  the masterful brief. The blueprint is a conversation's product, not a template's.
- **The breath cadence**: silent runs punctuated by a real human playtest, whose findings become
  the next breath's brief. The human is the event *between* breaths, never inside one.
- **The living blueprint**: the builder wrote ~8.5k lines of design/architecture docs *for
  itself*, to hand off across its own context boundaries. Context capacity is answered by the
  builder keeping its documents current as part of the work — fresh sessions board from
  documents, not memory.
- **The gauntlet clause**: the solo form of review is an explicit loop-until-the-bar instruction
  in the brief itself. With that clause, a between-breath human, and self-handoff docs, solo
  scales far higher than we guessed — the route-away threshold moves up accordingly. Budgeted
  compute substitutes for orchestration.
- **The anchor binds only when performed**: the gauntlet's termination is a BLIND side-by-side
  comparison against the reference, per item — the comparison must actually happen, and blind
  strips self-favoring bias. (Our trial's anchor was cited seven times and opened zero — a
  reference that is not compared is decoration.) In any form of the method: reviewing against
  an anchor means putting both on the table and saying which is better, blind where possible.
- **Per-item critic loops inside the breath**: each area gets a spawned fresh-context critic
  looping until the bar — independent eyes without a standing seat. And the brief's coverage
  ends with "anything you could think of": enumeration is delegated, so the named list never
  caps the ambition.

That's the whole engine. Everything else that has ever been in AgentBridge is a candidate
addition to this, and starts at zero.

## The bar for adding anything

An addition earns its place only if:
- we watched its absence cost something real in the product, at least twice, OR
- it prevents an irreversible harm (publish, delete, spend), where once is enough.

One incident = a note here, not an addition. Aphorisms are banned; additions are written as
what a seat does, in plain words.

## Candidates (empty until earned)

*(nothing yet — build up from the conversation)*
