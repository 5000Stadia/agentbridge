# AgentBridge

You were told at launch which seat you are. If nobody told you, you are the Navigator and this is
the start of a project.

This is the only process document. Every seat reads all of it, and a copy lives in the project at
`design/method.md`, so there is no reading order and nothing else to find. Everything about the
*product* lives in the project's own documents, which are as long as the product deserves.

## The shape

A human says what they want, and what "good" means for this project is written where every agent
can read it. One agent writes the spec and builds it. A second agent, wanting the same thing,
examines what was actually built against that written intention — the failures a user would hit,
the silent ones nobody would notice, and what is missing that "good" implies. The builder fixes
what is valid and returns, until the examination passes. A pass means the work adheres to the
human's stated design, and that adherence is the whole criteria, so it ships on the pass and the
next spec begins. The Navigator holds the intention and is silent between the moments it acts. The
human can look at the running thing at any moment; nothing waits on them.

The examining seat is not an opponent — everyone wants the same product and the opponent is the
defect — but it cannot contribute by agreeing, because finding failures is its whole share of the
work.

**Why a second mind at all.** Hand the built thing to a mind that does not know what was intended,
because a builder's code and a builder's checks come out of the same reading of the spec: when the
reading is wrong they agree with each other and are wrong together. On the trial this method came
from, four separate shipping bugs sailed through the builder's own checks — flags invisible after a
loss, an input dead in two browser engines, a scroll gesture that destroyed what you scrolled past,
layouts clipped off a phone screen — and every one was caught by a mind that just looked at what
was there. Pick the reviewer for ignorance of intent rather than for intelligence, since that
ignorance is what breaks the tie; a different model is not what does it.

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
the human then, in a sentence, and let them change it.

**What the choice is and is not about.** Every form has examination by a mind ignorant of intent —
spawned critics or a standing seat, the mechanism is the same and it is never optional — so do not
choose the form for quality or for safety, which no form guarantees on its own. Choose it for the
**shape of the work**: whether anything has to survive a seam, and whether areas must be built at
the same time while depending on each other. **Higher stakes raise the examination, not the
headcount** — more critics, more distinct lenses, more passes, the human on the running thing more
often. That dial exists in all three forms.

**One-shot.** One strong agent could plausibly build the whole thing in a single pass. Have the
front-door conversation, write `design/intention.md`, build it, hand the result to a fresh critic
using the critic brief at the end of this file, fix what is valid, and put it in front of the
human. Do this whenever it is honestly possible.

**Solo.** One builder working in long uninterrupted runs, spawning its own fresh-context critics
per area, with the human using the running thing between runs. No mailboxes, no standing seats.
Route away from this later than you think, because budgeted compute substitutes for orchestration:
a 60,000-line product was built this way in three runs.

**Crewed.** Add a standing Builder and Reviewer when areas must be built in parallel *and* talk to
each other, when a run is long enough that the builder's context ends mid-area and someone must
hold continuity across the seam, or when a mistake would be expensive to undo.

The front door is not optional in any of them. Everything through "The blueprint" below applies to
all three; after that, the two longer routes diverge.

**Where this method has been tried.** Building a thing that finishes. Long-lived work that never
finishes fits the same shape and is described below; work where the human cannot yet say what they
want — research, find-out-whether — has no front door to hold and is untested here. Say so rather
than pretending coverage.

**The design documents are the project's memory.** Not a pre-build artifact: they are written for
the agent who was not there — the one taking spec 2000 having never seen an earlier commit — and
they are kept current in the same commits as the work, never as a separate documentation task. When
a seat has to ask something the documents should have answered, that is the gap; fill it then.

**Keeping them navigable as the project grows.** Documents say what is true now; git holds what
changed — a done spec leaves the list, a superseded decision leaves the row. Start as one document
and split only when a reader genuinely cannot find things, and split along the product's own
structure, never by phase: a phase document becomes archaeology the moment the phase ends, while a
component's document stays true as long as the component does. Whatever the shape, there is one
entry point every agent lands on, and the vision names its own parts — that is what lets seats hold
separate goals under one vision.

**The public face is a different document for a different reader.** A README is for the stranger who
arrives: what it is, how to use it, how to run it. It carries no design internals and no vocabulary
from this method. Only the agent-facing doormat points inward.

---

## The front door

One long conversation with the human, and the only long one. After it, they are interrupted only
for a fork the written intention does not answer.

Make somewhere to write first — ask for the project name and the parent directory, invent neither.
One repository, design documents in `design/` inside it:

```
mkdir -p <project>/design && cd <project> && git init
```

**Open with what they want, in their words.** Not requirements. Ask what the thing is, who it is
for, and what would make them glad it exists. Then ask about the nearest thing they already love —
the game they replay, the tool they open every day, the paper they keep re-reading — and why,
because a person describing something they love hands you more design than any checklist extracts.

**Ask what would make them proud of it, not merely satisfied with it** — the version they would
show someone — and write *What "good" means here* at that level rather than at the level of
working. Everything downstream measures against those words, so a bar set at "it functions" is a
product that merely functions.

**Ask what would ruin it.** What would make them abandon it, and what must never happen. Keep these
separate from preferences: a preference is something they would forgive.

**Build the bar together; do not just borrow one.** What you will measure against is an
amalgamation of three things: what the two of you want this to be, the best real examples of this
shape that exist, and — where nothing real goes far enough — the imagined version at its fullest,
mapped out concretely. Write the result as qualities, because that is what later comparisons run
against.

**Take the real examples first, and make sure you can open them.** Ask for the most impressive one
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

---

## `design/intention.md` — the spine

One page. Every seat reads this, and it is the yardstick every examination measures against. The
test for any line: would an examination ever come out differently because this line exists? If not,
leave it out. Everything else about the product goes in the blueprint.

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

## What it must never do
<Only harms that cannot be undone — publishing, deleting, spending, sending, touching data that
is not ours — and lines that would make this a different product. Anything that could safely be
added later is not founding law and does not go here.>

## The spec list
| # | What to build now | What done looks like |
|---|---|---|
| 1 | | |

<Living. One paragraph of current instruction per row, plus what done looks like stated so
someone else could check it. Rows are rewritten in place; history lives in git, never in a row.
A number is allocated once and never reused, because the number is how everyone cites it.

Keep this list so that reading it answers *where are we and where are we going* without asking
anyone: the top row is what is being built right now, the rows under it are the plan in order, and
a finished row leaves the list — git holds what was done, and a list that keeps everything stops
being readable exactly when the project gets big enough to need it.>
```

Write the spec list off the blueprint's build order — the layers are the specs, in order. This
document changes only through you and the human.

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

**The build order.** Stated as layers: the smallest thing that runs end to end first, then each
layer added onto something already working, each with its own testable done. This is where
simplest-first lives — as the written sequence, not as a philosophy. End it with a final end-to-end
checklist for the whole product.

> *L0 — one board renders and one square opens from a real click, in a real browser.*
> Done: you can click and see a number.
> *L1 — full reveal, flag and win/loss rules.* Done: a game can be won and lost, both visibly.
> *L2 — touch input: tap opens, long-press flags, drag scrolls without opening.* Done: playable
> one-handed on a phone with no accidental opens in a minute of scrolling.
> *L3 — chord, timer, best times.* Done: chord works in both browser engines we support.
> *Final — a stranger plays three full games on a phone and a laptop with nothing broken.*

**Budgets.** The measurable targets the domain cares about, with numbers, and the condition each is
measured under — *first interaction under 100ms on a 2019 mid-range phone*, not *fast startup*.

**Out of scope, and risks.** What this deliberately is not, so nobody builds it by accident. Then
the failure modes you can already anticipate, and what each would look like if it happened.

**And anything else this product needs.** The list above is a floor, not a ceiling. Add the sections
this particular product demands and say why they are there.

The blueprint front-loads decisions, not scope — the build still climbs it in layers. It is a living
document, because fresh sessions board from it rather than from anyone's memory.

---

## Scaffold, and commit

Now there is something to write down.

```
<project>/
├── README.md          what it is, and the one command that runs the current thing
├── AGENTS.md          one line: "Read design/method.md, then intention.md, then blueprint.md."
├── CLAUDE.md          identical — different runtimes read different filenames
└── design/
    ├── method.md      a copy of this file
    ├── intention.md
    ├── blueprint.md
    ├── architecture.md   the builder writes this for itself; starts empty
    └── specs/            one file per spec
```

`git add` those paths and commit. That first commit has to exist before anything below runs. Then
take the route you chose: one-shot builds from here directly, and the two longer routes follow.

---

## The solo route

Write the brief and start the builder as a subagent of your own runtime. Adapt the bracketed parts
and keep the rest.

> Build [areas, by spec-list number] to the level of [anchor: how to run or read it].
>
> Read `design/intention.md` and `design/blueprint.md` first. Keep `design/architecture.md` and the
> README current as part of the work — a later session of you boards from those documents and
> nothing else, so write them for that reader, not as a report.
>
> For each area: write the plan and hand it to a fresh critic; then build it and hand the built
> thing to a fresh critic. Use the critic brief at the end of `design/method.md` verbatim. Fix what
> is valid, re-critique, and stop when nothing found blocks the target. Areas that do not touch
> each other run in parallel. Assemble, then run one critic over the assembled whole — integration
> defects have no other observer.
>
> Cover the areas named above, and anything else you can think of that the intention implies.
>
> Keep the thing runnable by the one command in the README at the end of every area.
>
> When every area passes, run the blind comparison in `design/method.md`. If it does not say ours
> is better on every quality in *What "good" means here*, the shortfalls are the next run's brief.
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
git -C /abs/path/<project> worktree add ../<project>-review --detach
```

You and the Builder do share the repository root. Stage by explicit path — never `git add -A` — or
one of you will commit the other's half-finished work.

**Mailboxes.** The seats talk over AgentPost. If an AgentPost skill is installed, follow it over
anything here; it owns the current command surface. Otherwise, `agentpost --help`, and:

```
agentpost profile-register <project>-n --display-name '<Project> Navigator' --kind project \
  --summary 'Holds the intention and design documents for <Project>.' \
  --roles navigator --projects <project> --project-roots /abs/path/<project> --handles 'nav'
```

Register `<project>-b` (`--kind role`, handle `build`, root the project) and `<project>-r`
(`--kind role`, handle `check`, root `/abs/path/<project>-review`) the same way. The addresses are
then `<project>.nav`, `<project>.build`, `<project>.check`. Exactly one single-word handle per
seat — a second one silently takes the address. Register a seat before launching it; a launcher
cannot bind to a profile that does not exist.

If AgentPost is not installed at all, do not invent a channel. Say so and run the solo route.

Then bind each seat from the root it will work in, naming the seat — a wrong inference does not
error, it sends as the wrong box:

```
cd /abs/path/<root> && agentpost join <seat> --cli <runtime>
agentpost armed <seat>
```

`agentpost armed` reports state; it does not change it. **QUEUED is not live.** Follow what `join`
prints, then `agentpost doctor <seat> --project "$PWD" --cli <runtime>` and do what it says, until
`armed` reports ARMED. ARMED is a claim about the notifier, not proof the channel works, so prove
each seat with a real round trip: the new seat messages you, you reply, and the reply arrives as a
live wake. Until that lands, say the seat is set up but unproven, in those words.

**Grant directory trust in the same act as the launch,** because a runtime meeting a directory for
the first time can silently sit at a trust prompt, and a detached seat that is waiting looks exactly
like a seat that is working. Trust the directory in whatever way that runtime offers; one known
way for Claude Code is setting `hasTrustDialogAccepted` true for that root in `~/.claude.json`
before launching. If a seat never speaks, attach to its terminal and look — it is usually sitting
on that prompt with nothing on the channel.

**Launch.** Prefer the managed launcher, which binds the identity:

```
tmux new-session -d -s <seat> -c /abs/path/<root> "agentpost claude --agent <seat> '<brief>'"
tmux new-session -d -s <seat> -c /abs/path/<root> "agentpost codex  --agent <seat> '<brief>'"
```

The brief for the Builder, filled in:

> You are the Builder on <Project>. Read `design/method.md` and follow it. Your mailbox is
> `<project>-b`; the Reviewer is `<project>.check` and I am `<project>.nav`. Get ARMED, message me
> to prove the round trip, then take spec <n>.

The Reviewer's is the same from its worktree, with mailbox `<project>-r` and `<project>.build` as
the Builder, ending *wait for the Builder's first handoff* instead of taking a spec. If a seat
cannot get live, it sends one message naming the exact command it needs and stops; you end that
instance and relaunch it. Twice for the same seat means the launch form is wrong — fix the form
rather than the seat.

**On the channel:** `agentpost message <address> '...'` to send, `agentpost question` when you need
an answer, `agentpost list <seat>` and `agentpost read <seat> <id>` to see, `agentpost next <seat>
--message-id <id>` to claim one before working it, `agentpost reply` to answer. A seat that has
sent its message stops; the next letter wakes it. Mail lives outside the repository, so anything
decided on the channel is written into the design documents before the exchange scrolls away.

---

## The loop

The Navigator picks the next spec row and checks that whatever it builds on actually exists and
resolves. The Builder writes the spec, then builds it. The Reviewer examines it at exactly two
moments and no others:

1. **Right after the spec is written, before any code exists.** On the trial this killed a design
   flaw that would have been implemented perfectly and still been wrong.
2. **Right after the implementation is complete.**

Between those two moments the Builder works alone and in silence — no progress reports, no
check-ins. Each examination names *everything* it sees in one pass: one review naming ten things
costs a fraction of ten reviews naming one each, and that round trip was the entire pace cost on
the trial. The Builder fixes what is valid, says why for anything it declines, and returns. Repeat
until it passes, and ship on the pass. A spec that takes four rounds needed four — never pass work
to shorten the loop, and never treat "nothing is broken" as the bar when *What "good" means here*
asks for more, because the point is not a product that survives examination but one that beats the
anchor when the two are put side by side. **And when it does, stop** — polishing past the bar is
not quality, it is the work eating itself, so send it and take the next spec.

### The Builder

Take the spec row you were handed and write it into `design/specs/<n>-<slug>.md`: what you will
build, what done looks like stated so someone else could check it, and where the edges are — what
this must not touch and what outside it feels the change. Commit that and send the path and the
commit to the Reviewer. Revise in place until it passes.

Then build. Break the work into the smallest independent pieces and fan out — a subagent per piece,
each paired with a fresh critic that sees only that piece and its target, using the critic brief at
the end of this file. You keep the assembled whole, because integration defects have no other
observer.

Write `design/architecture.md` for the fresh session of yourself that will board from it — that is
how you hand off across your own context boundary, and it is part of the change rather than a
later task.

When the implementation is done, commit it and hand the Reviewer the exact coordinates — commit
hash and changed paths — never a description and never a moving branch. Say what you verified and
what you did not. Do not walk the Reviewer through your thinking — the examination is of the thing,
not of the account — but do name anything anomalous you hit and what it forced, since that is the
one thing it cannot discover by reading the artifact.

### The Reviewer

Resolve the coordinates first and check the commit out in your worktree — `git checkout <hash>` —
before you open anything, and send back unread any handoff that does not resolve.

At the first moment there is no code, so examine the written spec against `design/intention.md` and
the blueprint: what it would produce that the intention forbids or does not ask for, what it leaves
ambiguous enough that two readers would build different things, and what its stated "done" would
not catch.

At the second moment, examine what was built and never the account of it: work the critic brief at
the end of this file against the commit you were handed. Perform its check test rather than reading
past it — sixteen green checks once sat on a visibly broken build, and two of them could never have
failed at all. Two things are yours and are not in the brief: judge against *What "good" means here*
rather than against your own taste, and where the work touches something the anchor also does, put
both on the table, take one item at a time, and say which is better and why.

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
   passed, mark the row and hand over the next one.
3. **Forks** — when the work hits a choice the written intention does not answer, answer it from
   the whole picture, or carry the one question to the human. Either way the answer goes into the
   design documents, in the human's words where they gave them, so the fork is closed rather than
   resolved once.
4. **Deadlocks** — when Builder and Reviewer disagree, both demonstrate with artifacts and you
   judge the evidence. Almost always the real fault is an ambiguity in the written intention, so
   the fix is to remove the ambiguity rather than to pick a winner.
5. **The end** — below.

You never relay: Builder and Reviewer talk to each other directly. You never narrate: the design
documents are the only things you write.

### The human

Let them look at the running thing whenever they like and never make anything wait on them —
twice on the trial, two sentences from a human on the running product beat every machine check in
the harness. What they find becomes a spec row, written by you.

Interrupt them for exactly two things: a fork the written intention does not answer, and anything
that cannot be undone. Everything else routes through you or waits.

---

## The blind comparison

Where the intention names an anchor, meeting it means actually putting both on the table. Run this
at the end of a solo run, and once over the whole product before the final ship.

1. Make both runnable or readable side by side: our build, and the anchor.
2. Spawn a fresh agent that has read nothing about this project.
3. Label the two A and B, randomised, and hand it the comparison brief at the end of this file.
4. It judges one quality at a time, each taken verbatim from *What "good" means here*.
5. Every quality ours loses is next run's brief.

If you had to write your own standard instead of finding an anchor, the comparator judges our build
against those written qualities alone, item by item. Do not argue with the result and do not re-run
it with a friendlier framing. If a quality still loses and closing the gap is beyond what this
project can reach, that is a fork: decide it from the whole picture or carry it to the human, write
the answer into the intention, and move on.

---

## How we work

- **When a change makes a sentence false, the sentence dies in the same change** — docs, comments,
  README, the spec row, the intention — so the product never lies about itself.
- **Every fact has one home and everywhere else points at it,** so a change lands in one place
  instead of leaving copies behind to go stale.
- **Keep the one command in the README working** at the end of every spec or area, so the human
  never has to ask how to start the thing.
- **Settle disagreement by demonstration** — a run, a measurement, a counterexample. Never by
  argument, never by seniority.
- **Between seats, write for a reader who has read the same documents you have** — no preamble, no
  restating the target, no explaining what you both already know, because every word spent
  re-deriving shared understanding is a word the other agent has to read to learn nothing. Send
  what they cannot get elsewhere: the coordinates, what is anomalous, and — when something
  unexpected forced your hand — the mechanical reason it did. Say what blocks you out loud the
  moment it blocks you. Talking with the human is the exception: there, say enough.
- **Before handing anything over, ask three things** and answer only *KEEP*, *CUT*, or *CHANGE ONE
  THING*: does this change what ships, was it the cheapest way to get there, do my claims match the
  artifacts — checked against the written intention, not in the abstract.

---

## Done

Every spec row is done, the blind comparison over the whole product has run, the design documents
describe what actually exists, and the final commit is shipped. Run the thing yourself, end to end,
against *What we're making*.

Then tell the human in one message: what it does, where it runs, and what you would watch. Close
the seats — end the runtimes, confirm the work is committed, and remove the Reviewer's worktree —
because a live process with nothing to do looks exactly like a working seat.

---

# BRIEF — the critic

Hand this to a fresh agent that did not build the thing. Fill the brackets and change nothing else.

> You are examining [the artifact — the exact commit and paths, or the running thing and the
> command that starts it]. You did not build it. You do not know what the builder intended beyond
> what follows.
>
> The target: [the spec row or plan, verbatim]
> It must be good in these ways: [the relevant qualities from *What "good" means here*, verbatim]
>
> Be genuinely hard to satisfy. Your job is not to confirm that nothing is broken — it is to find
> everything standing between this and the thing the anchor is. Picture a real person using it in a
> real moment and ask what would leave them let down. Assume there is more to find than you have
> found.
>
> Run it and read it yourself. Do not accept any account of it, including the builder's.
>
> Name everything you find, in one pass — every failure a user would hit, every silent failure
> nobody would notice, and everything the target implies that is simply missing. Try it the wrong
> way, on a different engine, a different screen, a different input device. Do not rank, do not
> soften, do not stop at the first finding.
>
> For each check the builder cites as proof: delete or break what it guards, confirm it goes red,
> and restore it. A check that stays green is a finding.
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
