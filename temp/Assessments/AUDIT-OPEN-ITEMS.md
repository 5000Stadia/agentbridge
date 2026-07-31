# AgentBridge — open audit items

**Status:** working notes, not a board. Temporary — `agentbridge/temp/` is untracked and nothing
here is committed. Now against `bc79ad9`, on branch `agent/project-qualified-agentpost`.

Sections A–D were written against `3f1dd8d`: five contradictions fixed in `f082ddf`, AgentPost
instructions corrected against a live 1.3.0 run in `3f1dd8d`, and what those commits did **not**
address. **Section E is new** — asymmetries and loose ends introduced by `9450db9` (inbox
hygiene) and `bc79ad9` (the review handoff and `boot.md`), plus one restructure that is mapped
but deliberately not applied.

---

## A. Verified working — not open, recorded so it is not re-litigated

| Claim | Evidence |
|---|---|
| `join` writes `.agentpost.toml` and excludes it from git itself | `git check-ignore -v` → `.git/info/exclude:7`. Not tracked. Directive accurate. |
| `join` infers the seat from the project root | Ran with no positional agent, exit 0, `JOINED agentbridge claude /home/k/Projects/agentbridge`. |
| A Claude seat can arm itself | Persistent Monitor on `agentpost internal-claude-monitor` flipped QUEUED → ARMED with no restart. |
| The channel round-trips, including cross-project | `agentbridge` → `cx` queued while offline, claimed by Message-ID, replied, monitor fired. |
| Qualified suffix derivation | Four registrations, table now in the playbook. |

---

## B. Structural findings — the method itself

### B1. Nothing in the method is mechanically enforced

There is no hook, CI check, lint, schema, or script anywhere in 1,170 lines. Every rule fires
because a stateless agent re-read it and chose to comply. This is the single largest gap between
what the document asserts and what it can deliver, and several claims depend on enforcement that
does not exist:

- **The measure.** The playbook says it *"needs nobody to do anything and cannot be unseen"* and
  calls it the cheapest anti-drift mechanism in the method. In practice the Implementer computes
  it by hand at each push gate and the Navigator interprets it by hand. It is a discipline with a
  number attached, not a mechanism. Either soften the claim or make the count a script the board
  cites.
- **`decisions/` premise triggers.** *"When its condition fires, the Harness re-checks it
  mechanically rather than waiting for someone to feel uneasy."* Nothing watches those conditions.
  The re-check happens when a seat remembers, which is the failure mode the sentence disclaims.
- **Board hygiene, bounded-board, cite-don't-restate.** All enforceable by a pre-commit check on
  the bridge repo; none checked.

**Cheapest real fix:** a single `bridge-check` script the Navigator runs at the push gate —
board under N lines, `specs/` holds 0 or 1 files, every `specs/`/`archive/` filename matches
`<item>-<slug>.md`, every roadmap item number unique and never reused. Perhaps 40 lines of shell.
It would make four rules real and cost nothing per session.

### B2. Cross-spec correctness has no owner

- Implementer reads **only** its one roadmap row, and is explicitly barred from the archive and
  the wider roadmap.
- Reviewer works **per spec, never per batch**.
- Navigator's coherence read is explicitly **not correctness**.

Context economy is bought with this, and the trade is mostly right — but it means spec B breaking
spec A is nobody's job. The listed failure mode *"a fragment landing outside its spec"* is
answered by *"specs land whole"*, which prevents fragments and says nothing about interactions
between whole specs.

**Options, cheapest first:** (a) let the push gate ask "what existing behaviour could this have
changed?" as a fourth report line; (b) give the Reviewer a standing integration pass at phase
boundaries rather than per spec; (c) accept it explicitly and say so, so it is a known limit
rather than an oversight.

### B3. AgentPost is a hard dependency with no degraded path

Muster **stops** if the pinned release is unavailable or the capability check fails. The method is
otherwise careful about optionality — a git remote is optional, version control is not — but the
channel has no fallback, and it installs via `curl | sh` from a single repository.

The seats do not actually need AgentPost to work; they need *a* way to exchange messages with the
Captain in the loop. A named degraded mode — Captain relays by hand, decisions still land on the
board, nothing else changes — costs one paragraph and removes the only hard external stop in the
method.

### B4. Throughput is bounded by one human, and this is never stated as a cost

The push gate is the only reporting cadence, and every completion waits on the Captain. That is a
defensible design — correctness over speed — but someone adopting AgentBridge expecting parallel
agent throughput will discover it by being the bottleneck. One line in the README setting the
expectation would prevent a bad fit.

### B5. Onboarding cost is real and concentrated in one file

Measured from the scaffolded artifacts:

| Artifact | Words | Read by |
|---|---|---|
| `playbook.md` | 6,392 | every seat, every session |
| `PROJECT-BOARD.md` (template) | 659 | every seat, every session |
| `directives/navigator.md` | 853 | Navigator only |
| `directives/implementer.md` | 597 | Implementer only |
| `directives/reviewer.md` | 462 | Reviewer only |
| doormats (×4) | 65–69 | one per root |

A Navigator session reads ~7,970 words before the live spec — roughly **10–11k tokens**, of which
**~80% is the playbook**. That is affordable, and the flat-cost property still holds: it does not
grow with the project. But "four files every session" understates it, and a meaningful share of
the playbook is justification written for a human reader rather than instruction for a seat — the
*Ambient context* section spends 25 lines defending a four-line file.

**Worth considering:** split `playbook.md` into the rules a seat must hold (short) and the
rationale behind them (read once, cited when challenged). The risk is a pointer chain, which the
document explicitly warns against — so this is a real trade, not an obvious win.

### B6. Four files must stay identical with nothing syncing them

`AGENTS.md` and `CLAUDE.md` in each of two roots carry deliberately identical content, and the
playbook states *"nothing copies or syncs."* Written once, this is fine. Edited once, it is two
stale copies — precisely the *stale parallel descriptions* failure the method lists. They are
short and rarely touched, so the exposure is small, but the mitigation is a one-line equality
check in the B1 script.

### B7. The Chart requires research that no seat is equipped for

The Chart's exit condition includes *prior art cited in the bet*, and instructs that survey work
happen before the bet is written. Nothing states who does it, with what tooling, or what happens
when the Navigator's runtime has no web access. The playbook's own answer — that recurring or
deep-domain work is a subagent with a file — is never applied here, though it fits exactly.

### B8. The method is still untested

Six commits, no deployment. Everything above concerns design quality; efficacy is unmeasured. The
first real deployment is the experiment, and the Harness auditing the apparatus after one phase is
the method's own prescribed way to find out.

---

## C. AgentPost items — outside this repo

### C1. `send` inverts the bare-is-local rule — report upstream to `cx`

Verified on 1.3.0:

| Subcommand | bare cross-project | qualified `PROJECT.NAME` |
|---|---|---|
| `resolve` | refused — *"cross-project addresses must use PROJECT.SEAT"* | accepted |
| `list` | refused, same message | accepted |
| `send` | **accepted** — the rule forbids this | **rejected** — *"unknown agent"* |

So the addressing form the design mandates cannot send, and the accident the rule exists to
prevent is the one that works. This directly blocks the intended two-projects-talking case. The
playbook now carries the resolve-then-send-canonical workaround and instructions to delete it once
fixed. **Not yet reported to `cx`** — worth a letter, since the round trip proved that path works.

### C2. Twelve boxes are on the legacy `PROJECT.CANONICAL` form

Every existing box predates the verb-handle convention, so none addresses as `PROJECT.NAME`:

```
ag         (no project at all — bare-only)   pbeo       pattern-buffer-evolution.pbeo
apr        agentpost.apr                     pbeocx     pattern-buffer-evolution.pbeocx
c          construct.c                       pbr        pattern-buffer.pbr
cr         construct.cr                      cx         agentpost.cx
jobhunting job.jobhunting                    k          kernos.k
kernosresearch kernos.kernosresearch         pb         pattern-buffer.pb
```

Each is fixed by re-registering the same canonical name with a single-word verb handle —
`profile-register` updates in place rather than duplicating, verified on `agentbridge`. Mechanical
and low risk, but it is twelve commands and it changes addresses other agents may have cited, so
it is the Captain's call whether and when.

`ag` additionally has no project alias, so it is unreachable by any qualified address and can only
be addressed bare — which, given C1, means it can only be reached by the path that is supposed to
be forbidden.

### C3. The `agentbridge` box is live

Registered, joined, ARMED on this session's monitor, and holding one read reply from `cx`. Keep it
or `agentpost wipe agent agentbridge` — the process it existed to verify is verified.

---

## D. If only three things get done

1. **B1 — the `bridge-check` script.** Converts four asserted rules into enforced ones for ~40
   lines. Everything else in the audit is judgement; this one is just missing.
2. **C1 — report the `send` defect to `cx`.** It blocks the addressing structure the project has
   decided on, and the reporter has a working channel to the box that owns it.
3. **B3 — name a degraded mode without AgentPost.** One paragraph removes the only hard external
   stop in the method.

B2 and B5 are genuine trades that need the Captain's judgement rather than a fix. B8 resolves only
by deploying.

---

## E. Introduced by the workflow changes — asymmetries and loose ends

Ordered by how load-bearing the ambiguity is.

### E1. The Reviewer suggesting fixes collides with a standing rule ⚠ highest

The new red protocol has the Reviewer respond with *"why + suggestions for resolution."* The
Reviewer's directive says, under **Never**: *"Author what you will later review. Your duties are
review-, critique- and evidence-shaped."*

Those are in direct tension. A Reviewer that supplies the corrected text and then greens it is
reviewing its own words, and the second look is worth nothing — this is the same defect the
different-model-family suggestion exists to avoid, arriving through the front door.

**The distinction that resolves it:** a red may name the **direction and the constraint** — *this
must not assume the extractor sees the key; the invariant belongs at the boundary, not in the
caller* — and must not supply the replacement text. Direction is critique. Text is authorship.
Nothing currently states that line, so both readings are legal today.

*Recommendation:* one clause in the Reviewer directive. Cheap, and it protects the seat's whole
value.

### E2. Three seats can move a spec, so "only the Reviewer advances state" is not an invariant

Current movers:

| Move | By | Meaning |
|---|---|---|
| → `review/` | Implementer | ready for a verdict |
| `review/` → `specs/` | **Reviewer** | green, cleared to build |
| `specs/` → `review/` | **Navigator** | coherence read found drift |
| `specs/` → `archive/` | **Implementer** | implementation green, done |

The spec handoff was designed around *the verdict is the move, performed by the seat with the
authority*. The archive move breaks that: the Implementer declares its own work finished. The
Navigator kickback is defensible — drift is its call — but it means the invariant cannot be stated
simply either way.

**Two coherent options, and the choice is the Captain's:**

- **Tighten** — the Reviewer also moves `specs/` → `archive/` on implementation green. Then *only
  the Reviewer advances state* is true without exception, and it mirrors *you do not push on your
  own authority*.
- **State the asymmetry deliberately** — the Implementer archives because archiving is
  bookkeeping after a verdict already given, not a verdict. Defensible, but it must be written, or
  the next reader will "fix" it.

Doing neither leaves a rule that looks like an invariant and is not one.

### E3. Two files named `boot.md` with opposite lifetimes

`<bridge>/boot.md` deletes itself; the seat-level boot being discussed does not. Same name, same
repo, opposite rules — a seat that learns "boot.md deletes itself" and then meets the other one
has been actively misled.

*Recommendation:* rename one. `directives/spawn.md` reads correctly for the seat file — its
trigger is a spawn — and keeps `boot.md` unambiguous as the project's one-time setup.

**The underlying principle is worth stating once, wherever it lands:** *a file deletes itself when
its trigger can only fire once.* Project setup fires once, ever. Seat setup fires again for every
new instance, seat type, and machine.

### E4. The AgentPost restructure is mapped but not applied

Of the playbook's 173-line AgentPost section, roughly **90 lines are boot-only** — the capability
check and install, the release gate, the naming and verb-derivation tables, the register/join/
verify block, second-instance naming, and the wipe procedure. Every seat reloads all of it every
session to perform it once.

The hot residue is small: mail lives outside the repos, bare-vs-qualified addressing and the
`send` defect, armed-is-per-session, and inbox hygiene. Call it ~35 lines against 173.

Moving the cold half into the seat boot file is the largest single reduction available on the hot
path, and it is exactly what the seat boot file *is*. **Deliberately not applied** — held pending
the Captain's stated approach.

### E5. Smaller inconsistencies from the same changes

- **"Every seat reads four things, in this order."** With `boot.md` there is a fifth, read once at
  spawn. The sentence is now slightly false as written.
- **Board `In flight` — *"spec ID and status"*.** The location is now the status, so this asks for
  the thing the same commit told the board to stop restating. Should read spec ID and owner.
- **`archive/` naming is settled but its trigger row is not.** The locations table still describes
  `archive/` as opened when "behaviour and agreement disagree" — accurate, but it no longer
  mentions that a spec arrives there by move, under a name fixed at authorship.

---

## F. What did not change

Everything in §B (no mechanical enforcement, cross-spec correctness unowned, AgentPost as a hard
dependency, throughput bounded by the Captain, onboarding cost, doormat drift, Chart research
unassigned, method untested) and §C (the `send` defect unreported, twelve boxes on the legacy
address form) stands as written.

§B5's numbers are now conservative: the playbook grew with the review handoff and `boot.md`,
though E4 would cut it well below where it started.
