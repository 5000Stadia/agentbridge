# Playbooks

Thin domain sheets carrying what the universal method cannot know: the tools that act as hands,
where references come from, what the user's viewpoint concretely is, and the scars practitioners
already paid for. Beside each sits its sources companion, `<domain>.sources.md`: where the rules'
evidence came from and the routes that actually reach it.

## Using one

Read it at the front door and take what fits; a rule nobody summoned is not carried. Before a rule
governs a project, walk the companion routes behind it and confirm each still resolves and still
teaches what the rule claims — domains move monthly, and the moment a playbook is about to govern
is the moment staleness bites, so that moment carries the check and no schedule does. Copy what you
summon into the project as `design/playbook.md`, corrected to the world as it now is, and point
the project's doors at it so every seat reads it; the companion stays here. Where a playbook places
the human differently than the method does, the playbook governs the rows it covers — the domain
knew something the armchair did not. Two playbooks summoned together merge into one, with the
precedence written like a decision hierarchy.

## Drafting one

Where none exists, research before designing, with the researcher's brief below, and write
`design/playbook.md` as this project's draft with `design/playbook.sources.md` beside it, written
while the routes are still open in front of you. Tag every rule `researched` or `felt` so nobody
mistakes homework for scar tissue. The bar is a document another practitioner would recognise as
their craft, not a survey; hand it to a fresh plan critic before the blueprint is written, because
every later examination leans on it and it is otherwise the only document nobody examines.

## What travels back

Only what a run executed. A `researched` rule a row actually ran, confirmed or corrected; a scar
the run earned that the playbook lacked; a route that died and the one that worked instead. Nothing
drafted or researched that no row ever executed travels — a line that never changed what a seat did
is exactly the speculative mass a playbook exists to refuse. At close, one issue per playbook,
labelled `playbook`, raw and naming the run. The maintainer lands each change as its own commit
naming that run.

## Conventions

**Tags.** Every rule carries one. `researched` — drafted from studying real practitioners, not yet
touched by this method's hands. `felt` — a run under this method executed it: followed and it held,
followed and it failed and was corrected, or earned outright as a new scar. The tag records whose
hands have held the rule, so a confirmation moves `researched` to `felt` the same as a correction
does. There is no third tag.

**The sources companion.** One entry per source that feeds a living rule:

    ## <source, named>
    - Route: <the way in that actually worked, exact enough to repeat>
    - Feeds: <rule sections, by number>
    - Taught: <one line>
    - Verified: <date — the run or pass that last walked the route>

An entry that feeds no living rule dies in the same commit as the rule. The companion says which
routes work now; git holds which ever did.

**The provenance line.** The top of every playbook states facts, never adjectives: its birth tag,
and the runs that have deployed it, each by name.

## BRIEF — the researcher

Hand this to a fresh agent researching a domain or craft — for a playbook draft, an anchor, or a
decision that needs grounding. Fill the brackets and keep the rest.

> You are researching [the domain or craft], to ground [the playbook draft / the anchor / the
> decision]. The goal is not a best-practices summary: it is knowledge from practitioners who paid
> for it, at a resolution beyond what you could infer alone.
>
> Before any search, write what you already believe, and tag each claim *directional* (points the
> right way), *specified* (carries a mechanism) or *calibrated* (carries numbers or boundaries).
> Research counts only where it raises resolution above that baseline. On a settled topic the
> baseline may be most of the answer — "the consensus is correct" is a complete result. Do not
> manufacture obscurity.
>
> Hunt people, not summaries: who does this professionally, what their work leaves in public —
> postmortems, talks, teardowns, repositories, credits — and where they gather. Search in their
> vocabulary, since the content-farm layer cannot use words it does not know. From every good
> source, follow the cluster — their other work, who they cite, who cites them — and note the
> links, because experts who cite each other are one lineage and one data point; agreement across
> separate lineages is the strongest evidence this work produces. If hunting surfaces no
> practitioners at all, that is a finding: the craft is tacit or new, so turn to the nearest field
> that solved a structurally similar problem, and mark what you take from it *transferred*.
>
> Weigh what you find by what it cost to produce. A rejected alternative, a constraint designed
> around, a number only measurement yields, an account of a failure — these are expensive to fake.
> Advice is cheap. A plausible mechanism from an unverified source stays second-tier, because
> fluent fabrication is exactly what machine-written craft content is good at. Volume of agreement
> never outweighs one paid-for claim.
>
> Deliver: how settled the craft is and how far the baseline can be trusted; the practitioners
> and venues, with lineage noted; the claims that beat the baseline, each attributed; what the
> experts confirmed; where they disagree and whether the camps are independent; and the
> vocabulary, defined. Record every route while it is still open — the source, the exact way in
> that worked, what it taught — because the route is as hard-won as the finding.
