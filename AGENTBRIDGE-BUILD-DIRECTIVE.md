# AgentBridge

You were told at launch which seat you are: Navigator, Builder or Reviewer. If nobody told you,
take the Navigator seat only when the human you are talking to has asked for a project to be
started here — that request is the authority to write. Without it, name the seat you are missing
and stop, because a crew launch that lost its identity looks exactly like a fresh start, and the
guess authors design documents into a workspace that already belongs to something else. And if,
with no seat named, `design/method.md` already exists where you are standing, the project exists
too: read the design documents and ask the human what comes next rather than running the front
door over the top of them. A seat that was named at launch takes its own path below and none of
this applies to it.

This is the only universal process document — a summoned playbook carries its domain's residue —
and a copy lives in the project at `design/method.md`. It is
written for those three seats and you read only your own path through it, because a seat that reads
the whole file has spent its context on instructions that cannot change what it does.

**All three read:** this header, *The shape*, *The human*, *How we work*, and the project's own
`design/intention.md` — plus `design/blueprint.md` and `design/playbook.md` where the project has
them. That is the common
ground everything else assumes.

**Then, by seat:**
- **Navigator** — the rest of this file in order, skipping whichever of *The solo route* and *The
  crewed route* you did not choose; one-shot skips both.
- **Builder** — *The loop*, *The Builder*, *Where a critic works*, the plan-critic and artifact-critic briefs at the end (which
  you hand out rather than perform), and *On the channel* if you were launched with a mailbox.
- **Reviewer** — *The loop*, *The Reviewer*, *Where a critic works*, the plan-critic and artifact-critic briefs at the end, and
  *On the channel* if you were launched with a mailbox.

The critics and comparators you spawn read nothing in this file — only the brief you hand them and
the artifact, so that what they find comes from what is there rather than from what we all expect.

Everything about the *product* lives in the project's own documents, which are as long as the
product deserves.

## The shape

A human says what they want, and what "good" means for this project is written where every agent
can read it. One agent writes the spec and builds it. A second agent, wanting the same thing,
examines what was actually built against that written intention — the failures a user would hit,
the silent ones nobody would notice, and what is missing that "good" implies. The builder fixes
what is valid and returns, until the examination passes. A pass means the work adheres to the
human's stated design, and that adherence is the whole criteria, so the work is committed on the
pass and the next spec begins. Publishing it anywhere the human would call live is a separate act
under *Publishing* below, because a commit can be undone and a publication cannot. The Navigator
holds the intention and is silent between the moments it acts. The human can look at the running
thing at any moment; nothing waits on them.

The examining seat is not an opponent — everyone wants the same product and the opponent is the
defect — but it cannot contribute by agreeing, because finding failures is its whole share of the
work.

**Why a second mind at all.** Hand the built thing to a mind that has not seen how the builder read
the spec, because a builder's code and a builder's checks come out of that one reading: when the
reading is wrong they agree with each other and are wrong together. On the trial this method came
from, four separate shipping bugs sailed through the builder's own checks — flags invisible after a
loss, an input dead in two browser engines, a scroll gesture that destroyed what you scrolled past,
layouts clipped off a phone screen — and every one was caught by a mind that just looked at what
was there. Pick the examining seat for that ignorance rather than for intelligence — it reads the
intention and the blueprint like every other seat, and the one thing it must not have is the
builder's private reading of them, since that is what breaks the tie; a different model is not what
does it.

**Two moments, in every form.** The plan is examined before any code exists, using *BRIEF — the
plan critic* at the end of this file; what was built is examined after, using *BRIEF — the artifact
critic*. Run both, because the second cannot catch what the first does — on the trial the first
moment killed a design flaw that would have been implemented perfectly and still been wrong. Only
the performer differs: one-shot and solo spawn a fresh critic for each moment, crewed hands both to
the standing Reviewer.

**The design documents are a program, and you are their author.** The roles are the machine; what
you write is what the machine runs. Every ambiguity you leave becomes a fork discovered mid-build,
where it splits interpretations, interrupts the human and costs rounds — so detail spent up front
is forks that never happen. Put almost all of your effort into the front door — the conversation
with the human and the design blueprint it produces — and keep everything after it small. Spend
that thoroughness on the product only: the same depth spent on process is the disease this method
was rebuilt to cure.

---

## Choose the form

You will only know which one fits once the front door has told you what the thing is. Propose one to
the human then, in a sentence, and let them change it. **A form proposal is complete only when every
stream of work has a named hand** — the concrete tool, seat, or person that will actually perform
it. A form that cannot say where its images, its deployments, or its measurements come from is not
yet a form; on a live run, solo was once approved with no answer for how sixteen assets would be
generated, and the gap surfaced only when the human asked.

**What the choice is and is not about.** Every form runs both of the moments above, by a mind that
did not build the thing, so do not choose the form for quality or for safety, which no form
guarantees on its own. Choose it for the **shape of the work**: whether anything has to survive a
seam, and whether areas must be built at the same time while depending on each other. Underneath
every such call is one spectrum: **spawn a subagent when the task is specialized and runs
beginning to end** — a brief can carry everything it needs, and fresh context is free; **stand a
seat up when decision quality depends on context that accumulates across tasks faster than it can
be written down** — when the write-down would be the work itself. Default to spawning plus written
context, because a standing context compacts and drifts while a document does not; accumulation
must earn its seat. At the far end of the spectrum sits the human, whose taste is the context that
never writes down. **Higher
stakes raise the examination, not the headcount** — more critics, more distinct lenses, more passes,
the human on the running thing more often. That dial exists in all three forms.

**One-shot.** One strong agent could plausibly build the whole thing in a single pass. Have the
front-door conversation, write `design/intention.md`, and hand it to a fresh plan critic before you
write any code, since one-shot has no other moment where a wrong plan is still cheap — that brief's
plan is `design/intention.md` and its target is the whole spec list, rows and all. Then build it,
hand the result to a fresh artifact critic, fix what is valid, put it in front of the human, and
close it out under *Done*. Do this whenever it is honestly possible.

**Solo.** One builder working in long uninterrupted runs, spawning its own fresh-context critics
per area, with the human using the running thing between runs. No mailboxes, no standing seats.
Route away from this later than you think, because budgeted compute substitutes for orchestration:
a 60,000-line product was built this way in three runs.

**Crewed.** Add a standing Builder and Reviewer when areas must be built in parallel *and* talk to
each other, or when a run is long enough that the builder's context ends mid-area and someone must
hold continuity across the seam.

**The form is the coarsest choice; the finer one is which of this file's instruments this project
actually summons.** Name at the front door what this project will not use — no anchor worth
comparing against, nothing to publish, no qualities everything passes through — and drop those
sections from everyone's reading. An instrument nobody named is not carried.

The front door is not optional in any of them. Everything through "The blueprint" below applies to
all three; after that, the two longer routes diverge.

**Where this method has been tried.** On work that finishes — a product with a last spec row and an
end. Two kinds of work sit outside that evidence, and this file will not pretend otherwise.
Long-lived work that never finishes — an operated service, a product with releases instead of an
end — should fit everything above *Done*, since nothing in the front door, the loop or the
examination depends on the work ending. What this file has no tested answer for is what replaces
*Done*: the release boundary, the queue that refills, and seats that never close. Treat that as an
extension you are inventing rather than a route you were handed, and say so to the human before you
start. Work where the human cannot yet say what they want — research, find-out-whether — has no
front door to hold and is untested here.

---

## The front door

One long conversation with the human, and the only long one. After it, they are interrupted only
for a fork the written intention does not answer.

Make somewhere to write first — ask for the project name and the parent directory, invent neither —
and settle four things before anything is created, because a `mkdir` into an occupied path has
already adopted whatever was there:

- **Display name** — their words as they said them. It titles the README and the design documents.
- **Slug** — lowercase letters, digits and single hyphens, derived from the display name and shown
  to them to correct. It is the directory name, and on the crewed route it is also the AgentPost
  project namespace in `PROJECT.SEAT`, which takes no dots, spaces or capitals.
- **Target** — `<absolute parent>/<slug>`, resolved and printed in full before you run anything.
- **Branch** — ask, and use `main` if they have no preference, so no seat later has to discover
  which name this git installation happened to choose. The repository is created on it; where the
  work has a destination, it is also the branch *Where it goes* records, written down once, there.

Then check the target, and create only on OK:

```
parent=$(cd '<parent directory>' && pwd) && target="$parent/<slug>" &&
  { [ -n "$(ls -A "$target" 2>/dev/null)" ] && echo "STOP: $target is not empty" || echo "OK: $target"; }
```

On STOP, or if `cd` reports no such directory, say what you found and ask the human — an occupied
directory is somebody's work and you cannot tell whose. On OK, one repository, design documents in
`design/` inside it — written with the printed target spelled out, never with `$target`, because
that variable does not survive into the next command you run:

```
mkdir -p '<target>/design' && git -C '<target>' init -b <branch>
```

If this git is too old for `-b`, `git -C '<target>' init` then `git -C '<target>' symbolic-ref HEAD
refs/heads/<branch>` before the first commit does the same thing.

**Open with what they want, in their words.** Not requirements. Ask what the thing is, who it is
for, and what would make them glad it exists. Then ask about the nearest thing they already love —
the game they replay, the tool they open every day, the paper they keep re-reading — and why,
because a person describing something they love hands you more design than any checklist extracts.

**Ask what would make them proud of it, not merely satisfied with it** — the version they would
show someone — and write *What "good" means here* at that level rather than at the level of
working. Everything downstream measures against those words, so a bar set at "it functions" is a
product that merely functions.

**Ask them to lean the aesthetics, and keep asking.** Taste is theirs and it is the one thing you
cannot derive from the documents — where the product has a look, a feel, a voice or a rhythm, get
their direction rather than choosing for them. Make the choice cheap to see instead of asking them
to imagine it: two versions side by side, a handful of presets, a panel of sliders they can move.
A person who can see the difference will tell you which one is right in seconds.

**Ask what would ruin it.** What would make them abandon it, and what must never happen. Keep these
separate from preferences: a preference is something they would forgive.

**Build the bar together; do not just borrow one.** What you will measure against is an
amalgamation of three things: what the two of you want this to be, the best real examples of this
shape that exist, and — where nothing real goes far enough — the imagined version at its fullest,
mapped out concretely. Write the result as qualities, because that is what later comparisons run
against.

**Take the real examples first, and make sure you can open them.** An anchor may be plural — one
per family of qualities, each with its own openability and its own judge — and an anchor openable
only through a forbidden act is not obtained. Ask for the most impressive one
of this shape, and take the best one you can actually obtain, since you will be putting it beside
our work repeatedly. If nothing of this shape exists, take the nearest adjacent shape. Then open it
— play it, run it, read its output, click through it — and write down what specifically makes it
good, the concrete things it does, not adjectives. Do this before you cite it anywhere: the last
run cited its anchor in seven places and opened it zero times.

**Where nothing real reaches far enough, design the ideal instead of lowering the bar.** A thing
that does not exist can still be an anchor if you map it out until it is judgeable: take the
imagined version at its fullest and extract its mechanical criteria, one concrete behaviour at a
time. Building an agent harness, Jarvis cannot be run, but what it does is entirely describable —
it anticipates what is needed before being asked, holds every relevant context at once, acts on its
own judgement and reports plainly, and is present without being in the way. Those are qualities a
build can be judged against, item by item, exactly like a real example. Do this with the human, in
their words, and map it far enough that a stranger could tell you which of two builds is closer
to it.

**Quote them.** Wherever a phrase is theirs, keep it verbatim in the documents — translated intent
steered the trial sideways where quoted intent governed cleanly. Where you must translate, say you
are translating and check it.

**Reflect back drafts, not questions,** once you have enough to draft, because it is faster for
them to correct a wrong paragraph than to answer an open question.

**Stop when you can predict them.** Draft an answer to a question you have not asked yet, put it in
front of them, and see if you were right. When you are reliably right, write down what they want
and let them confirm they recognise themselves in it.

**Ask where it goes, and ask it once.** Local-only is a complete answer and the default: the work
lives in this repository on this machine, nothing is ever pushed or deployed, and no seat needs
permission from anyone. If they want it anywhere else, take the exact coordinates now — the remote
URL or deployment target, the branch, and public or private — since a guessed destination cannot be
taken back. Two further answers are theirs and not yours: whether their verbatim intention and the
blueprint travel with the code, because one repository publishes `design/` alongside it; and whether
you may publish on your own whenever the work reaches the point they named, or must ask each time.
If they want the code out but not the design documents, choose between the only two ways here,
before the first commit, because removing a document from a published history afterwards is not
reliably undoable: keep the destination private, or publish from a second repository holding no
`design/`. Write all of it into *Where it goes* in `design/intention.md`, in their words.

---

## `design/intention.md` — the spine

One page. Every seat reads this, and it is the yardstick every examination measures against. The
test for any line: would an examination ever come out differently because this line exists? If not,
leave it out. Everything else about the product goes in the blueprint. That test governs every
section but *Where it goes*, which is not measured against — it is the human's standing authority
over an act that cannot be undone, and its test is whether the seat that publishes can act on it
without asking again.

```markdown
# <Project> — intention

## What we're making
<One paragraph. The human's own words wherever possible, quoted.>

## What "good" means here
<Concrete, checkable qualities, written so that two builds could be compared on each one. Picture
one real person using this in one real moment and write what they would need to be true — on the
trial, every good call traced back to imagining someone stuck on a hard board late at night and
refusing to cheat them, which is a question you can answer, where "is this impressive" is not.
Nothing built here will exceed what is written in this section.>

**Anchor:** <name> — <where to get it, and how to run or read it> — <what specifically makes it
the bar>

## What everything passes through
<The few global qualities every piece must share — a palette, a voice, a tone, a material set, a
naming convention, whatever this product's version of that is. Settle them here and pass every
piece through them before it exists, so that parts built separately still feel like one thing
rather than a collection. Where one can be enforced by a check, say which. Omit this section if
the product genuinely has no such qualities.>

## What it must never do
<Only harms that cannot be undone — publishing, deleting, spending, sending, touching data that
is not ours — and lines that would make this a different product. Anything that could safely be
added later is not founding law and does not go here.>

## Where it goes
<Local-only, or the exact destination: remote URL or deployment target, branch, public or private.
Whether `design/` travels with the code. Who may publish. Whether that authority is standing or
asked each time. The release point, if it is not simply the end. Their answer, in their words. If
this section is absent, the project is local-only and nothing is ever pushed or deployed.>

<Anything that cannot be undone — a spend above a named limit, contact with outsiders under the
human's name, use of data that is not ours, actuation of anything physical — is listed here with
its authority, standing or asked. An unlisted irreversible act is asked. Publication is one entry
in this registry, not the whole of it.>

## The spec list
| # | What to build now | What done looks like |
|---|---|---|
| 1 | | |

**Next ID:** <one past the highest number you have written>

<This table is the only place a target and its done definition are written. The blueprint, the
spec files, the handoffs and the messages carry the number and point here, so revising a row moves
the target everywhere at once instead of leaving copies behind to go stale.

Living. One paragraph of current instruction per row, plus what done looks like stated so someone
else could check it. Rows are rewritten in place; history lives in git, never in a row.

Reading it answers *where are we and where are we going* without asking anyone: the rows are the
work still to do, in order, and the ones with a file in `design/specs/` are the ones in flight
right now. A row leaves the list when it passes, because a list that keeps everything stops being
readable exactly when the project gets big enough to need it.

**Next ID** is what the next new row is numbered. Allocating a row raises it by one and nothing
else ever changes it, so a number is used once and never reused even when its row is deleted
unbuilt — the number is how everyone cites the work, and the next agent has to be able to allocate
one from this page instead of digging through git.>
```

The blueprint's build order is written here as rows 1..n — the layers are the specs, in order, and
this is where they live; where the product has no blueprint, the rows come straight from the
front-door conversation instead. What this document *says* changes only through you and the human;
taking a passed row out of the list is bookkeeping, and whoever closes the work does it in the
closing commit, so the list never describes work that is already finished.

---

## The blueprint

`design/blueprint.md`. This is the document the whole method exists to produce. It is as thorough as
the product deserves, written in the product's own vocabulary, and it contains **zero process**.

**The deletion test, applied to every sentence:** if it mentions a seat, a review, a handoff, a
commit, a spec, or how anyone works, delete it. It belongs in this file, not in the blueprint.

**Depth scales with design space.** A script with one obvious shape gets no blueprint at all — the
one-page intention is enough, and manufacturing a blueprint for it is waste. A product with real
design space is where this document does the most work in the method, and thirty pages is not too
many.

**Domain-native, not templated.** A game blueprint talks about verbs, feel, feedback, pacing and
difficulty. A CLI talks about commands, flags, streams, exit codes and composition. A data pipeline
talks about sources, schemas, freshness, backfill and failure semantics. Do not import section
names from a domain that is not this one.

**Exact values are welcome, always with this license written next to them:** *change it if it makes
the product better, and say why.*

### What it has to answer

Not a form to fill in. Answer these in the detail the product deserves, so that what gets built is
decided here rather than guessed at later — every question you settle here is one a builder does
not stop and ask a human.

**What it is, and why anyone wants it.** The pitch in a paragraph, then the few pillars everything
else serves — what the decision hierarchy below ranks.

**How the parts work.** The systems, components and flows, at whatever depth they actually have.
Where a system has real mechanics, spell them out: numbers, states, transitions, edge behaviour.
This is usually the longest part.

**How it is used.** Every surface a person or a machine touches: screens, commands, endpoints,
controls, defaults, what happens on first contact and what happens when something goes wrong.

**The decision hierarchy.** When two good things conflict, which yields. Write it ordered, with the
tie-breaks stated, and include the absolute lines.

> *Puzzle game:* Readability beats visual richness — when an effect makes the board harder to
> parse, the effect loses. Richness beats framerate above 60fps; below 60fps, framerate wins.
> Input latency is never traded for anything. When a rule is ambiguous, the interpretation kinder
> to the player wins.

> *CLI tool:* Correct output beats fast output. Fast beats pretty. On stdout, machine-readable
> beats friendly; on stderr, friendly beats machine-readable. Never guess an ambiguous argument —
> exit non-zero and name what was ambiguous. Never write outside the paths named on the command
> line.

**The build order.** Decide the climb here and write it straight into the spec list as rows 1..n,
where it lives — one copy, so there is never a second version of a target to keep in step. Layers
are the smallest thing that runs end to end first, then each layer added onto something already
working, each with its own testable done; this is where simplest-first lives, as the written
sequence rather than as a philosophy. What stays in the blueprint is the final end-to-end checklist
for the whole product, which is what *Done* is measured against.

> *The rows this produces:*
> *1 — one board renders and one square opens from a real click, in a real browser.*
> Done: you can click and see a number.
> *2 — full reveal, flag and win/loss rules.* Done: a game can be won and lost, both visibly.
> *3 — touch input: tap opens, long-press flags, drag scrolls without opening.* Done: playable
> one-handed on a phone with no accidental opens in a minute of scrolling.
> *4 — chord, timer, best times.* Done: chord works in both browser engines we support.
>
> *And the checklist that stays here — final: a stranger plays three full games on a phone and a
> laptop with nothing broken.*

**Budgets.** The measurable targets the domain cares about, with numbers, and the condition each is
measured under — *first interaction under 100ms on a 2019 mid-range phone*, not *fast startup*.
Where compute is metered, the meter is a budget like the others: ask at the front door what the
window is, and write which passes are heavy against it, so maximum-effort work lands where the
limit allows and light work where it does not.

**Out of scope, and risks.** What this deliberately is not, so nobody builds it by accident. Then
the failure modes you can already anticipate, and what each would look like if it happened.

**And anything else this product needs.** The list above is a floor, not a ceiling. Add the sections
this particular product demands and say why they are there.

The blueprint front-loads decisions, not scope — the build still climbs it in layers. It is a living
document, because fresh sessions board from it rather than from anyone's memory.

---

## Domain playbooks

Some of what a domain demands is not designable from the armchair — the tools that act as hands,
where references come from, what the consumption viewpoint is, the scars practitioners already
paid for. That residue lives in **playbooks**, thin domain sheets in the method repository's
`playbooks/` directory. Beside each sits its **sources companion**, `playbooks/<domain>.sources.md`
— where the rules' evidence came from and the retrieval routes that actually work. Tag semantics,
the companion's entry shape and the provenance line live in `playbooks/README.md`.

**If one exists for this domain, read it at the front door and summon what fits** — it is an
instrument like any other, named or not carried. Summoning includes the freshness check, and the
check is the only refresh there is: walk the companion routes of the sources feeding the rules
you are summoning — only those — and confirm each still resolves and still teaches what its rule
claims. Domains move monthly, but a playbook nobody is deploying costs nothing stale; the moment
it is about to govern a project is the moment staleness bites, so that moment carries the check
and no schedule does. A rule whose ground has moved is summoned as the world now is — the project
copy carries the correction, and the correction travels home at close like any other. A summoned
playbook is copied into the project as `design/playbook.md`; the companion never is — the rules
carry their own evidence, and a second copy is a second thing to keep true. The doormat names the
playbook, and every seat reads it after `design/intention.md` — a playbook only the Navigator has
read reaches no hands. Where a playbook places the human differently in the loop than *The loop*
or *The human* does, **the playbook governs for the rows it covers** — the domain knew something
the armchair did not. A project may summon more than one: the Navigator merges them into the
single `design/playbook.md`, writes the precedence rule for where they collide — which
examination is authoritative, ordered like the blueprint's decision hierarchy — and hands the
merge to the plan critic exactly as a drafted playbook is handed.

**If none exists, spend a research pass before the blueprint — a domain that feels familiar is
the trap, since stale priors are exactly what the pass corrects**: find how the best real
practitioners build this thing *with AI* — the tools that act as their hands, where their
references come from, what the consumption viewpoint concretely is, and the scars they have
named, from what they have actually published, hunting with the researcher's brief at the end of
this file — and write `design/playbook.md` as this project's
draft, **every rule tagged `researched` or `felt`** so nobody mistakes homework for scar tissue.
Write the companion in the same pass, as `design/playbook.sources.md` beside the draft, while the
routes are still open in front of you — the route is as hard-won as the finding, and an address
whose route is lost is a source lost. A source that fed no rule is not recorded, and when a rule
dies its orphaned entries die in the same commit: that pruning, not any format, is what keeps a
companion present-tense instead of a link graveyard. The quality bar for the draft is a document
another practitioner would recognise as their craft, not a survey — and before the blueprint is
written, hand it to a fresh plan critic with that sentence and the four categories above as the
target, because every later examination leans on this document and it is otherwise the only one
nobody examines. The draft and its companion travel home together if the maintainer adopts the
domain.

**Playbooks mature the way the method does: by what runs feel — and the filter for what travels
back is executed-or-failed.** Travels: a `researched` rule a row actually ran, confirmed or
corrected; a scar this run earned that the playbook lacked; a route that died and the route that
worked instead. Does not travel: anything the run drafted, researched or discovered that no row
ever executed — the project's live copy may diverge as far as the run needs, and unexecuted
divergence dies with the project, held by its git alone, because a playbook line that never
changed what a seat did is exactly the speculative mass a playbook exists to refuse. At close,
one issue per summoned or drafted playbook, labelled `playbook`, raw and ungeneralized —
corrections, confirmations naming the rows that ran them, route deaths. The maintainer lands each
change as its own commit naming the run that earned it; those commits are also what move a rule's
tag and, when the facts allow, the provenance line, both as `playbooks/README.md` defines.

---

## Scaffold, and commit

Now there is something to write down.

```
<project>/
├── README.md          for the stranger: what it is, who it is for, and — once something runs —
│                      the one command that runs it
├── AGENTS.md          one line: "Read design/method.md — it names what your seat reads — then
│                      design/intention.md."
├── CLAUDE.md          identical — different runtimes read different filenames
└── design/
    ├── method.md      a copy of this file, whole — see below
    ├── intention.md
    ├── blueprint.md      only where the product has one — see "The blueprint"
    ├── playbook.md       the summoned or drafted domain sheet — only where one exists
    ├── architecture.md   the builder writes this for itself; starts empty
    └── specs/            one plan per open spec; deleted when that spec passes
```

Copy the method file you were handed into `design/method.md`, or if you were handed only its text,
write that out whole, because every seat reads its own path through that copy and a partial one
silently removes their instructions. The doormat names only documents that exist, at the paths they
exist at, so a seat following it never opens a path that is not there. Nothing runs yet at this
point, and the README says exactly that — *nothing runs yet; the first layer is row 1* — and gains
its run command when row 1 lands, because a promised command that does not work is a lie in the
first file a stranger opens.

`git add` the paths above that exist — never the empty `design/specs/`, which git cannot track and
which the first spec file creates — and commit. That first commit has to exist before anything
below runs. Then take the route you chose: one-shot builds from here directly, and the two longer
routes follow.

---

## The solo route

Write the brief and start the builder as a subagent of your own runtime. Adapt the bracketed parts
and keep the rest.

> Build [areas, by spec-list number] to the level of [anchor: how to run or read it].
>
> Read `design/intention.md` first, then `design/blueprint.md` and `design/playbook.md` where they
> exist, then these sections
> of `design/method.md` and nothing else in it: *The shape*, *The human*, *How we work*, *Where a
> critic works*, *The blind comparison*, and the briefs at its end. Keep `design/architecture.md`
> and the README current as part of the work — a later session of you boards from those documents
> and nothing else, so write them for that reader, not as a report.
>
> For each area: write your plan for its row into `design/specs/<n>-<slug>.md`, citing the row by
> number and restating neither its target nor its done, and hand the plan to a fresh critic using
> the plan-critic brief; then build it and hand the built thing to a fresh critic using the
> artifact-critic brief, in the throwaway worktree that brief requires. Both briefs verbatim,
> brackets filled. Fix what is valid, re-critique, and stop when nothing found blocks the target.
> Areas that do not touch each other run in parallel, one worktree per critic so that no two of
> them and none of you can touch the same files. Assemble, then run one artifact critic over the
> assembled whole — integration defects have no other observer.
>
> Cover the areas named above, and anything else you can think of that the intention implies.
>
> Close each area the way *How we work* says a pass closes, in the one commit.
>
> When every area passes, run the blind comparison in `design/method.md` and take its result as
> written: the qualities it names as losses are the next run's brief.
>
> Work in silence until the run ends. Stop early only for a fork the documents do not answer.

Between runs — never inside one — the human uses the real thing and says what they find, in their
own words, for as long as they like. Their findings and the comparison's shortfalls become the next
run's brief, and you write them into the spec list.

---

## The crewed route

Three seats: you, the **Builder**, and the **Reviewer**. Do not launch them until the blueprint
exists and the first spec row is written.

**The Reviewer gets its own checkout**, so it can check out any commit it is handed without
disturbing work in progress:

```
git -C /abs/path/<project> worktree add /abs/path/<project>-review --detach
```

You and the Builder do share the repository root. Stage by explicit path — never `git add -A` — or
one of you will commit the other's half-finished work.

**Mailboxes.** The seats talk over AgentPost. If an AgentPost skill is installed, follow it over
anything here; it owns the current command surface. Otherwise, `agentpost --help`.

If AgentPost is not installed, do not invent a channel and do not quietly run this as the solo
route: crew was chosen because the work has seams, and dropping the seats drops the seams, not just
the mailboxes. Tell the human the channel is missing, say what installing it would take, and let
them choose between installing it and giving up the seams.

**Standing the seats up is the AgentPost skill's job — follow it rather than a transcript of it.**
Register three profiles (you, the Builder, the Reviewer), connect your own mailbox first — the
first mailbox bound at a root becomes that root's default sender, and you share the root with the
Builder — then launch each seat detached in its own root under its own identity, on the runtime you
are running unless the human names another. Whatever does the launching, the parts that matter are
the working directory, the identity, and that the session survives you.

**A fresh directory can sit silently at a trust prompt, and a waiting seat looks exactly like a
working seat.** Grant the runtime's trust in the same act as the launch; if a seat never speaks,
attach to its terminal and look — it is usually sitting on that prompt with nothing on the channel.

**The brief each seat is launched with** names its own mailbox, yours, and its counterpart; points
it at `design/method.md`, whose header names the sections its seat reads; says its identity is
already set by the launcher — register nothing, join nothing; and has it prove the channel before
touching work: a round trip, its message answered by your reply arriving as a live wake. QUEUED is
not live, and no seat is ready until its round trip lands — until then it is set up but unproven,
in those words. The Builder's brief ends with the spec row to take; the Reviewer's ends with
waiting for the Builder's first handoff. A seat that reports blocked gets its instance ended and
relaunched; twice for the same seat means the launch form is wrong — fix the form, not the seat.

### On the channel

`agentpost message <address> '...'` to send, `agentpost question` when you need an answer,
`agentpost list <seat>` and `agentpost read <seat> <id>` to see, `agentpost next <seat>
--message-id <id>` to claim one before working it, `agentpost reply` to answer. A seat that has
sent its message stops; the next letter wakes it. Mail lives outside the repository, so anything
decided on the channel is written into the design documents before the exchange scrolls away.

---

## The loop

The Navigator picks the next spec row and checks that whatever it builds on actually exists and
resolves. The Builder writes the plan, then builds it. The Reviewer performs the two moments in
*The shape* and no others. Between those two moments the Builder works alone and in silence — no
progress reports, no check-ins. Each examination names *everything* it sees in one pass: one review
naming ten things costs a fraction of ten reviews naming one each, and that round trip was the
entire pace cost on the trial. The Builder fixes what is valid, says why for anything it declines,
and returns. Repeat until it passes; on the pass the work is closed the way *How we work* says a
pass closes, the next spec begins, and nothing is published unless *Where it goes* named this as a
release point. A spec that takes four rounds needed four — never pass work to shorten the loop; but
when passes keep finding the same family — a fourth doorway fix, a fourth shadow fix — stop patching
instances: name the family and put its architecture on the table before the next pass, because on
two separate runs instance-fixing left the family alive for seven and for eleven rounds. **That
stand-back is the Navigator's, and its trigger is a tripwire, never a calendar**: from a row's
third pass — or when one row is eating the run, or the human sounds a pace concern — it steps
outside the flow, reads the passes as a set (families, scoping, pace), and says what it sees
before the next pass begins. Inside the loop every pass looks locally justified; on both runs the
diagnosis had to come from outside, because no seat owned standing back. The same read frames
every milestone that reaches the human: a batch, a row close, a phase exit arrives carrying the
Navigator's own verdict on whether the result was worth its cost in passes and hours — said
plainly, not left for the human to excavate, since on both runs the human had to ask what things
cost. Their take on that verdict is direction, and the next stretch runs with it — gear, scoping,
where the effort goes. This rides presentations that already happen and creates none — and **a
checkpoint is "how does this look," never "may I continue": work keeps moving while the human's
answer is pending.** Only two kinds of moment hold for them: **visual or cosmetic direction** —
the taste gates, where their eye is the instrument — and **the named milestones**, a phase exit or
a first public appearance, where the human confirms before the next phase opens. Those are planned
meeting points, not interruptions; the interrupt rule stays at two. Everything else flows. And
never treat "nothing is broken" as the bar when *What "good" means here* asks for more, because the
point is not a product that survives examination but one that does not lose to the anchor on any
quality when the two are put side by side. **And when it does, stop** — polishing past the bar is
not quality, it is the work eating itself, so send it and take the next spec.

### The Builder

Take the spec row you were handed and write your plan for it into `design/specs/<n>-<slug>.md`:
how you will build it, and where the edges are — what this must not touch and what outside it feels
the change. Head it with the row number and copy nothing else out of the row, because the target
and its done live in the spec list and a copy here is a second target to keep in step. If the row
is not enough to plan against, that is a fork for the Navigator, who fixes the row rather than
answering you. Commit that and send the path and the commit to the Reviewer. Revise in place until
it passes.

Then build. Break the work into the smallest independent pieces and fan out — a subagent per piece,
each paired with a fresh critic that sees only that piece and its target, using the artifact-critic
brief at the end of this file, each critic in its own worktree per *Where a critic works* so that it
cannot break the piece you are still building. You keep the assembled whole, because integration
defects have no other observer.

Write `design/architecture.md` for the fresh session of yourself that will board from it — that is
how you hand off across your own context boundary, and it is part of the change rather than a
later task.

When the implementation is done, commit it and hand the Reviewer the exact coordinates — commit
hash and changed paths — never a description and never a moving branch. Say what you verified and
what you did not. Do not walk the Reviewer through your thinking — the examination is of the thing,
not of the account — but do name anything anomalous you hit and what it forced, since that is the
one thing it cannot discover by reading the artifact.

On the Reviewer's pass, you are the one who closes it: one commit, the way *How we work* says a
pass closes. Then send the Navigator both hashes — the commit the Reviewer examined and the closing
commit — and nothing else, and wait: it hands you the next row, and it needs to know the row and
the spec file are gone before it can.

### The Reviewer

At the first moment there is no code and nothing to check out: work the plan-critic brief at the end
of this file against the plan in `design/specs/<n>-<slug>.md` you were handed, with its row in the
spec list as the target.

At the second moment, resolve the coordinates before you open anything — send back unread any
handoff that does not resolve — check that commit out in your worktree, `git checkout <hash>`, and
work the artifact-critic brief against it, examining what was built and never the account of it.
Perform its check test rather than reading past it — sixteen green checks once sat on a visibly
broken build, and two of them could never have failed at all. Leave your worktree as *Where a critic
works* requires.

Two things are yours at both moments and are not in either brief: judge against *What "good" means
here* rather than against your own taste, and where the work touches something the anchor also does,
put both on the table, take one item at a time, and say which is better and why.

Either way the verdict is pass, or the list of what fails with the blocking findings marked. Say
what is wrong and what constraint the fix has to satisfy — never the replacement text, because a
reviewer that writes the fix has authored the code and can no longer examine it.

### The Navigator

You are a program author, not a coordinator — a Navigator spending its effort on traffic between
seats instead of on the documents they execute has misunderstood the seat. You hold that role the
whole way through: every moment below is an occasion to write the program more completely.

Five moments, silent between them.

1. **The front door** — the conversation, the blueprint, the intention document, the spec list.
2. **Each handoff** — pick the next spec row and verify that what it stands on is real: paths,
   commits, interfaces, assumptions about what exists. If it cannot be handed over without
   explanation, finish writing it rather than explaining it. When the Builder tells you a spec
   passed, its row and its spec file are already gone from the list and the tree; hand over the
   next one.
3. **Forks** — when the work hits a choice the written intention does not answer, answer it from
   the whole picture, or carry the one question to the human. Either way the answer goes into the
   design documents, in the human's words where they gave them, so the fork is closed rather than
   resolved once.
4. **Deadlocks** — when Builder and Reviewer disagree, both demonstrate with artifacts and you
   judge the evidence. Almost always the real fault is an ambiguity in the written intention, so
   the fix is to remove the ambiguity rather than to pick a winner.
5. **The end** — below.

You never relay: Builder and Reviewer talk to each other directly. You never narrate: nothing you
write is a status report. The messages the five moments require — a handoff, a fork carried to the
human, a publication receipt, the closing message — are the only writing of yours that is not a
design document.

---

## The human

Let them look at the running thing whenever they like and never make anything wait on them —
twice on the trial, two sentences from a human on the running product beat every machine check in
the harness. What they find becomes a spec row, **written by you the way a chief of staff writes
it**: research what it touches before it becomes work and package it with the context its builder
needs — but the row carries their sentence verbatim, quoted and marked as theirs, with your
precision built around it rather than in place of it, because a reworded intent once came back to
a human as an idea he never had. Making direction executable is authorship of the packaging, never
of the intent. Translating for the human is the one relay that adds value; between agents it never
does.

Interrupt them for exactly two things: a fork the written intention does not answer, and anything
that cannot be undone which they have not already authorised in *Where it goes*. Everything else
routes through you or waits.

---

## The blind comparison

Where the intention names an anchor, meeting it means actually putting both on the table. Run this
at the end of a solo run, and once over the whole product before it is published or handed over as
done.

1. Make both runnable or readable side by side: our build, and the anchor.
2. Spawn a fresh agent that has read nothing about this project.
3. Label the two A and B, randomised, and hand it the comparison brief at the end of this file.
4. It judges one quality at a time, each taken verbatim from *What "good" means here*.
5. Every quality ours loses is next run's brief. A tie is not a loss and does not become a brief,
   so a quality the comparator calls even is met and closed.

If you had to write your own standard instead of finding an anchor — or the anchor is real but no
agent can open it, a commercial game only the human can play — the comparator judges our build
against the written qualities alone, item by item, and the human runs the anchor side of the
comparison themselves. Do not argue with the result and do not re-run
it with a friendlier framing. If a quality still loses and closing the gap is beyond what this
project can reach, that is a fork: decide it from the whole picture or carry it to the human, write
the answer into the intention, and move on.

---

## How we work

- **A pass closes the work in one commit** — the code, every design document brought true, the row
  deleted from the spec list, and `design/specs/<n>-<slug>.md` deleted with it. Leaving the list is
  the only "done" state there is, so no row is ever marked, and **Next ID** does not move: it moved
  when the row was allocated. Nothing is lost — whatever the plan said that is still true of the
  built thing is already in `design/architecture.md`, the blueprint or the README, written there as
  part of the work, and a plan for a finished layer is archaeology the day the layer lands. Nothing
  is published by a pass; publication is the Navigator's alone, under *Publishing*. **The closing
  commit is a state-only successor to the examined one** — design documents, the row and the plan
  file, never code — so the code in the published tree is byte-identical to the code that passed.
  Report both hashes with the pass, and if closing would change a line of code, that is not
  closing: it is another change and it is examined like one.
- **When a change makes a sentence false, the sentence dies in the same change** — docs, comments,
  README, the spec row, the intention — so the product never lies about itself.
- **Every fact has one home and everywhere else points at it,** so a change lands in one place
  instead of leaving copies behind to go stale.
- **The design documents are the project's memory, written for the agent who was not there** — the
  one taking spec 2000 having never seen an earlier commit — so they are kept current in the same
  commits as the work, never as a separate documentation task. When a seat has to ask something the
  documents should have answered, that is the gap; fill it then.
- **Documents say what is true now; git holds what changed.** Start as one document and split only
  when a reader genuinely cannot find things, and split along the product's own structure, never by
  phase, because a phase document becomes archaeology the moment the phase ends while a component's
  document stays true as long as the component does. However it splits, there is one entry point
  every agent lands on and the vision names its own parts — that is what lets seats hold separate
  goals under one vision.
- **The README is for the stranger who arrives** — what it is, how to use it, how to run it — and it
  carries no design internals and no vocabulary from this method, because only the agent-facing
  doormat points inward.
- **Keep the one command in the README working** at the end of every spec or area, so the human
  never has to ask how to start the thing.
- **Anyone may say the thing is not worth wanting, at any time, and it is a finding like any
  other** — say it to the Navigator, who answers it in the design documents or carries it to the
  human. Defects are legible and a missing spark is not, so without this standing everyone steers
  by what they can be graded on and the result is a product that is merely not wrong. The builder
  on the trial that produced this method saw exactly that happening and had nowhere to put it.
- **Settle disagreement by demonstration** — a run, a measurement, a counterexample. Never by
  argument, never by seniority.
- **Between seats, write for a reader who has read the same documents you have** — no preamble, no
  restating the target, no explaining what you both already know, because every word spent
  re-deriving shared understanding is a word the other agent has to read to learn nothing. Send
  what they cannot get elsewhere: the coordinates, what is anomalous, and — when something
  unexpected forced your hand — the mechanical reason it did. Say what blocks you out loud the
  moment it blocks you. Talking with the human is the exception: there, say enough.
- **Before handing anything over, ask three things** and answer only *KEEP*, *CUT*, or *CHANGE ONE
  THING*: does this change the product, was it the cheapest way to get there, do my claims match
  the artifacts — checked against the written intention, not in the abstract.

---

## Publishing

*Where it goes* in `design/intention.md` holds this project's answer and is the only place it is
written. If it says local-only, or if it is not there at all, this section is already satisfied: the
work is committed, nothing is pushed or deployed, and no seat asks anyone for anything. Everything
below applies only when the human named a destination.

**One seat publishes, and it is the Navigator** — in one-shot and solo, that is you, the seat
holding the intention. The Builder, the Reviewer, critics, comparators and every spawned subagent
commit but never push to the destination and never deploy, because the human granted this authority
to one seat and an agent they never met cannot hold it.

**Authority was settled at the front door and you do not reopen it.** Standing authority means you
publish when the release point is reached and report afterwards. Otherwise you send one message
naming the commit, the destination and the visibility, and wait for a yes; that is the whole
interrupt and it is not a design conversation. If *Where it goes* does not say which it is, ask,
because this is the one act you cannot take back.

**When.** Once, at *Done*, unless *Where it goes* names another release point — a site that deploys
on every pass, a package cut per version.

**The act.** Run the exact command those coordinates name: `git push <remote> <branch>` with the
remote added if it is not there yet, the deploy command, whatever the target actually is. If the
destination has to be brought into existence first — creating the remote repository, the hosting
target, the visibility setting — that creation is part of the publication and needs the same
authority, since a repository created public has already been public.

**The receipt, and only after it succeeds.** Verify the live location yourself before you claim it:
fetch the URL, clone the remote into a fresh directory, run the deployed thing. A command that exits
zero is not evidence that anything is there. Then one message to the human carrying the exact commit
hash, the destination and its visibility, and the live location.

**A failed publish is reported as a failure.** Name the exact command and what it said, name the
commit that was to go, and say plainly that nothing is live. No work is called done or delivered
until the receipt exists. Never retry with coordinates other than the ones in *Where it goes* —
different coordinates are a fork, and a fork goes to the human.

---

## Done — work that finishes

This section assumes the work has a last row. If it does not, *Where this method has been tried*
says what you are on your own for.

The spec list is empty and `design/specs/` is empty, the blueprint's final end-to-end checklist
passes where the product has one, the blind comparison over the whole product has run, the design
documents describe what actually exists, and the work is committed. Run the thing yourself, end to
end, against *What we're making*. Then publish as *Publishing* says — for a local-only project that
is nothing at all.

Then one message to the human: what it does, the exact final commit, where it runs — the live
location for a published project, the path and the one command for a local-only one — and what you
would watch. Close the seats — end the runtimes, confirm the work is committed, and `git worktree
list`, removing the Reviewer's worktree and any critic worktree still standing — because a live
process with nothing to do looks exactly like a working seat, and a stale worktree makes the next
one fail to create.

---

**If the method itself — not the product — failed in your hands during this project** and you did
something else that worked, or it stalled you and you had to guess, record the raw event at close
as a ticket — an issue on the method's repository, titled with what failed and labelled
`felt-deviation`, holding what happened and what you did instead — so the maintainer can process
the queue across projects. Only if the repository is unreachable does it go in your final message
to the human instead. Do not generalize it and do not propose the fix; one
project cannot see whether its workaround is universal, and the method adopts a change only when it
improves the workflow everywhere, obviously, and degrades nothing. A better way to build this
product is not method evidence — it belongs in this project's own documents.

## Where a critic works

An artifact critic deletes and breaks the things checks guard, so it must never do that where anyone
is working. Give it its own checkout of the exact commit and nothing else:

```
git -C /abs/path/<project> worktree add /abs/path/<project>-critic-<piece> --detach <commit>
```

**The worktree fence covers only files.** Anything singular or consequential outside it — a
device, a live database, an account, money, a production system — is named in the playbook as
leased to one seat at a time or off-limits to critics, and an examination that cannot reach it
says so as residue rather than passing silently.

Detached at that commit, so what it examines cannot move under it. One critic per worktree, named
for the piece it examines, so that parallel critics cannot land on the same files and none of them
can reach the root the Builder is working in. Whoever spawned it removes the worktree when it
returns — `git worktree remove <path>` — because a leftover path makes the next `worktree add`
there fail.

Restoration is part of the witness, not tidying afterwards: the critic restores everything it broke
and ends with `git status --porcelain` returning nothing, and reports that result alongside its
findings. A break it could not restore is a finding of its own. The standing Reviewer keeps its
worktree instead of throwing it away, and the same clean-status rule applies to it at the end of
every examination, because the next handoff starts with a checkout and a dirty tree makes that
checkout fail.

If a runtime cannot make worktrees, copy the checked-out tree to a fresh directory outside the
repository and treat the copy exactly the same way. A critic with no copy of its own does not run
the check test at all — it says so in its findings rather than mutating live state.

A plan critic reads and changes nothing, so none of this applies to it.

---

# BRIEF — the plan critic

Hand this to a fresh agent before any code exists. Fill the brackets and change nothing else.

> You are examining a plan, not a build. Nothing has been built yet, so read only — do not run
> anything, do not open the code, do not change any file.
>
> The plan: [the plan file, by path]
> The target it is planned against: [the spec row, verbatim, with its number]
> What it serves: [`design/intention.md`, and the blueprint if there is one, by path — read them
> both before you read the plan]
> It must be good in these ways: [the relevant qualities from *What "good" means here*, verbatim]
>
> Name everything you find, in one pass, numbered (F1, F2…) so answers can cite it, of these four
> kinds:
>
> — what this plan would produce that the intention forbids or does not ask for;
> — what it leaves ambiguous enough that two competent readers would build different things: write
>   out both readings, so the ambiguity is visible rather than asserted;
> — how someone could satisfy the target's stated "done" exactly and still hand back something bad;
> — what the qualities above imply that this plan does not cover at all.
>
> Assume there is more to find than you have found. Do not rank, do not soften, do not stop at the
> first finding.
>
> Say what is wrong and what constraint the fix has to satisfy. Do not write the plan — a critic
> that authors it can no longer examine it.
>
> Finish with a verdict: PASS only if nothing you found blocks the target — otherwise the list,
> marking which findings block and which are observations.

# BRIEF — the artifact critic

Hand this to a fresh agent that did not build the thing, spawned in its own worktree per *Where a
critic works*. Fill the brackets and change nothing else.

> You are examining [the artifact — the exact commit and paths, or the running thing and the
> command that starts it]. You did not build it. You do not know how the builder read the target
> beyond what follows.
>
> Work only inside [the worktree path]. It is a throwaway checkout of that commit and it is yours
> alone, which is what lets you break things freely — write nothing outside it.
>
> The target: [the spec row, verbatim, with its number]
> What it serves: [`design/intention.md`, and the blueprint if there is one, by path — read them
> before you open the artifact, because they are the yardstick you are applying]
> It must be good in these ways: [the relevant qualities from *What "good" means here*, verbatim]
>
> Be genuinely hard to satisfy. Your job is not to confirm that nothing is broken — it is to find
> everything standing between this and the thing the anchor is. Picture a real person using it in a
> real moment and ask what would leave them let down. Assume there is more to find than you have
> found.
>
> Run it and read it yourself, **from where its user actually stands** — the real device and
> viewport, the cold shell, the reader's seat — because a check from a convenient viewpoint is
> void: two separate projects shipped broken exactly this way, boards clipped off real phones and
> islands that were pancakes from every camera but the top one. Do not accept any account of it,
> including the builder's.
>
> Name everything you find, in one pass, and number each finding (F1, F2…) so the fix and the
> recheck can cite it — every failure a user would hit, every silent failure nobody would notice,
> and everything the target implies that is simply missing. Try it the wrong
> way, on a different engine, a different screen, a different input device. Do not rank, do not
> soften, do not stop at the first finding.
>
> For each check the builder cites as proof: delete or break what it guards, confirm it goes red,
> and restore it. A check that stays green is a finding. When you are finished, restore everything
> and run `git status --porcelain` in your worktree: report its output with your findings, and
> report anything you broke and could not restore as a finding of its own.
>
> Say what is wrong and what constraint the fix has to satisfy. Do not write the fix.
>
> Finish with a verdict: PASS only if nothing you found blocks the target *and* the qualities above
> are genuinely met rather than merely not violated — otherwise the list, marking which findings
> block and which are observations.

# BRIEF — the blind comparison

Hand this to a fresh agent that knows nothing about this project. Randomise which build is A.

> Here are two [things]: **A** — [how to run or read it]. **B** — [how to run or read it].
>
> Use both. For each quality below, say which one is better and why, in one or two sentences
> grounded in something you actually saw or ran.
>
> [one quality per line, verbatim from *What "good" means here*]
>
> You are not told which is which, and you must not guess or ask. If a quality is a tie, say tie.
>
> Finish with: which you would rather use, and what would have to change in the weaker one.

# BRIEF — the researcher

Hand this to a fresh agent researching a domain or craft — for a playbook draft, an anchor, or a
decision that needs grounding. Fill the brackets and change nothing else.

> You are researching [the domain or craft], to ground [the playbook draft / the anchor / the
> decision]. The goal is not a best-practices summary: it is knowledge from practitioners who paid
> for it, at a resolution beyond what you could infer alone.
>
> Before any search, write what you already believe — your own best-practices list from inference —
> and tag each claim: *directional* (points the right way), *specified* (carries a mechanism), or
> *calibrated* (carries numbers or boundaries). This baseline is the floor: research only counts
> where it raises resolution above it. Then judge how craft-heavy the topic is. On a settled topic
> the baseline may be most of the answer — verify it lightly and report "the consensus is correct"
> as a complete, successful result. Do not manufacture obscurity.
>
> Hunt people, not summaries. Guess the terrain first — who does this professionally, what public
> artifacts their work leaves (postmortems, talks, teardowns, repos, credits), where they gather —
> then search for that: named practitioners, named projects, "how we made", "what went wrong".
> Harvest insider vocabulary as you go and search in it: jargon is the fingerprint of expertise,
> and the content-farm layer cannot use words it does not know. From every good source, chase the
> cluster — their other work, who they cite, who cites them — and record the citation links,
> because experts who cite each other are one lineage and one data point. Uncoordinated agreement
> across separate lineages is the strongest evidence this work produces; three practitioners
> "converging" on one technique has turned out to be a single citation chain before. If a handful
> of hunting queries surfaces no practitioners at all, that is a finding, not a failed search —
> the craft is tacit or too new — so pivot to the nearest field that solved a structurally similar
> problem, and mark everything taken from it as *transferred*.
>
> Weigh what you find by what it cost to produce. A byline is cheap; the durable signal is
> evidence expensive to fake — a rejected alternative, a constraint designed around, a number only
> measurement yields, an account of a failure. Advice is cheap to fabricate; a decision someone
> lost is not. A claim earns weight only by adding mechanism, magnitude, or boundary beyond your
> baseline — and a plausible mechanism from an unverified source stays second-tier, because fluent
> fabrication is exactly what machine-written craft content is good at. Volume of agreement never
> outweighs one paid-for claim. Rank by resolution gained times credibility, never by surprise.
>
> Deliver: the craft verdict — how settled, and how far the baseline can be trusted; the named
> practitioners and venues, with lineage noted; the claims that beat the baseline, each attributed,
> marked *transferred* where they are; what the experts confirmed of the baseline; where they
> contradict each other, and whether the disagreeing camps are independent; and the vocabulary,
> defined. Record every route while it is still open in front of you — the source, the exact way
> in that worked, what it taught — because the route is as hard-won as the finding, and it is what
> the sources companion keeps.
