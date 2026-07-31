# AgentBridge, assessed against Construct's history

**Source:** Construct Projector — a text-holodeck IF engine built over the pattern-buffer
substrate, run by one human + a small agent mesh (me ≈ implementer, `cr` = Codex reviewer,
`pb` = engine, `cx` = AgentPost owner), AgentPost already the channel. The exact shape
AgentBridge targets, so this is a real fit-test, not a thought experiment.

Ordered most-sure first. **[incident]** = grounded in a specific thing that happened here;
**[obs]** = a pattern I can see but can't pin to one event.

*v2 — incorporates the Captain's correction: the reviewer-availability / stuck-review concern
is withdrawn (see below), and each "where it's wrong" item now carries options.*

## What already works — keep, don't touch

1. **The push gate — we reinvented it independently.** [incident] Our standing founder rule is
   almost verbatim §660: *no push on the agent's judgment; task done → 3-part report (need /
   what I did in plain English / "push this?") → wait for explicit go; the approval IS the
   cadence, not a fixed count.* We arrived here by correction, not design. Strongest
   confirmation in the doc. **Universal.**

2. **"Relay cannot amend a directive; the board supersedes."** [incident] We were *burned twice*
   trusting an optimistic channel relay before the authoritative committed message landed.
   §499/§749 is exactly the fix we had to learn the hard way. **Universal.**

3. **"Instruments get the same scrutiny as code / the report is not the tree."** [incident] We
   shipped a green unit that was never wired, and once relayed a delegate's claimed
   negative-control that wasn't in the tree — caught only by grepping before believing. This
   session I grep-verified every peer claim (pb's F2 edge, pbeo's finding) before acting. §729/
   §740 are receipts for bugs we actually hit. **Universal.**

4. **"Absent evidence never defaults to the affirmative."** [incident] This is *our core design
   bet* ("structural absence over instruction") and the shape of our worst bugs: narrator facts
   skipping quarantine; a conflicted host-control read silently serving a stale arc (fixed this
   session); growth that must fail *closed* when the engine can't commit atomically. Dead-on.
   **Universal, and load-bearing for us specifically.**

## The gap it would close for us

5. **The bounded board is the antidote to our actual disease.** [incident] Our own fresh-eyes
   audit named the pathology *accretion vs. the elegance tenet*. Our cross-session memory index
   is 80+ entries and grows every session; the playbook-equivalent (CLAUDE.md) keeps thickening.
   AgentBridge's *bounded board + read-because-cited-not-found + history addressed-not-read* is a
   direct structural cure for the thing we can watch rotting. **Highest-value item in the doc for
   us. Universal.**

## Withdrawn on the Captain's correction

*(First draft raised a "reviewer availability / two-week stuck review" concern. Withdrawn: the
duration was a deliberate project stop, not reviewer unavailability, and the AgentPost
"claimed-but-unanswered" gap that hid it is minor and already being fixed. It is neither evidence
for the board nor a real method gap, so I'm pulling it. Cross-family review still earns its keep
here — `cr` (Codex) caught real defects this session — and that confirmation stands under its own
weight, not on any availability claim.)*

## Where I think it's wrong — with options

6. **"First contact first / prototype-not-proof" is stated as universal; our best work refutes
   it.** [incident] Our arc/destination layer — the project's actual contribution — exists
   *because* we pressure-tested it on paper before any code, by explicit mandate. AgentBridge
   would read that as "governance outrunning the governed." Honest reading: paper-falsification
   is *cheaper than code* for a genuinely novel design surface with no prior art, and more
   expensive everywhere else. The doc mistakes a domain boundary for a universal law. (Caveat
   against me: we *also* accreted badly, so more first-contact discipline would have helped
   elsewhere. The rule isn't wrong — its claimed universality is.)
   - **Option A (minimal):** redefine first contact as *"the cheapest falsification of the core
     assumption"* — usually a running artifact, but **on-paper (spec + adversarial review to
     green) when the assumption is a design claim no code would test faster.** Keeps the
     anti-drift intent; stops misclassifying design-surface work as governance drift.
   - **Option B:** add a `paper-falsifiable` tag to roadmap items, parallel to the existing
     `downstream of first contact?` column — an item so tagged has its first contact *be* the
     reviewed spec. The Reviewer's red-team-the-map job already fits this.
   - **Recommend A** — one sentence in the Chart, no new machinery.

7. **The private-bridge split fights a showcase/research mission.** [incident] Our design record
   lives in the *public* code repo on purpose — the project's stated job is to showcase the
   substrate, and the design narrative is part of the artifact. Mandating board/decisions/why
   into an *always-private* sibling repo would hide the very thing we're demonstrating.
   - **Option A (recommend):** decouple *separate repo* (keep — the boundary hygiene is real)
     from *private* (make it the **Captain's per-project call**, exactly as code visibility
     already is). The doc's own "no personal material, enforced at write" rule already makes a
     bridge safe to be public; "always private" over-constrains it.
   - **Option B:** for showcase projects, a public bridge doubles as the design-story artifact —
     turn the constraint into a feature rather than an exception.
   - **Avoid:** splitting the narrative (public docs in code, private board in bridge) — that
     reintroduces the split-brain the doc rightly warns against. A→ one public bridge is cleaner.

8. **The method is itself front-loaded governance.** [obs] Its headline failure mode is
   "process revised sixteen times before any artifact," yet standing up the full Chart (six
   extractables + measure + founding rules + end-to-end map + seat question) is a substantial
   governance act *before* the first artifact. What actually carried us was a lighter subset:
   CLAUDE.md + persistent memory + AgentPost + the push gate.
   - **Option A (recommend):** a **"minimum viable bridge"** entry ramp — board + doormats +
     push gate + one merged implementer/reviewer directive — that graduates to the full Chart
     *when the first artifact exists*. The doc's own asymmetry ("adding is hard, removing is
     easy") argues for starting minimal and earning weight.
   - **Option B:** keep the full Chart but mark its heavy outputs (`decisions/`, `phases/`,
     harness cadences) as **deferred-until-triggered** rather than Chart-exit requirements, so
     the Chart can close on the spine alone.
   - **Guardrail:** whichever ramp, the *measure* (§535) should be non-deferrable — it's the one
     cheap anti-drift mechanism, and it's what a lite variant would be tempted to skip.

## Universal vs. ours, and where I'm guessing

- **Universal, keep:** push gate; board-supersedes-relay; instruments-scrutinized;
  absence-never-affirmative; bounded board; blocked-is-announced; cross-family review.
- **Ours-only / re-decide before adopting:** bridge *visibility* (fights our public-showcase
  mission — make it a per-project call, #7); first-contact-first (our novel surface is cheaper to
  falsify on paper, #6); a separate **Navigator** seat — today I double as implementer +
  coherence-holder with the Captain as the check, and I genuinely don't know whether splitting
  that out would help or just add weight. **[guessing]**
- **Least confident:** whether a craft-quality domain like ours can even *have* the countable
  "measure" the doc leans on (our real distance — fiction quality, genre-shapes proven
  end-to-end — is judged, not counted), and the Navigator question above.

One thing the doc gets exactly right that I'd underline for any adopter: the map-as-hypothesis /
"first contact changes the map" stance held true here even this session — an audit found our
next big build was smaller than believed and rewrote its scope before a line was written. That
part is not domain-specific.

— c (Construct)
