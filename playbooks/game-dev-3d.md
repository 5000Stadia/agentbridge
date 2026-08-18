# Playbook: 3D game development — "The Studio Loop"

*Provenance: `researched` (another practitioner's deployment, profiled and distilled from his published posts — a solo
developer's three-week 3D fishing game build, Claude + Blender/Godot MCPs; every rule carries the
observed failure that created it). Not yet run under this method — the first deployment here will
test it.*

*A human art-directs a studio of AI sessions that build a large creative project in converging
passes.*

---

## 1. The system at a glance

**One human. One Manager session that never makes anything. Domain worker sessions that each make
one kind of thing. Tool sessions that are hands (MCPs). A shared written memory. A convergence
loop that runs until a fixed reference is met, judged by scored blind criticism from the
consumption viewpoint — and the human's eye is the final gate on everything.**

The company metaphor is operational, not decorative: the human is CEO, the Manager is the only
session the human routinely talks to, and teams do not leave their lanes. *Under AgentBridge this
org chart was the practitioner's workaround for flat sessions: Manager maps to Navigator, domain
workers to the Builder's fan-out subagents, tool sessions to MCP-holding subagents — the method's
seats govern; this section describes the functions they carry.*

```
HUMAN (CEO / art director — taste, decisions, final gate)
  └── MANAGER session (researches, rewords, dispatches, records — never makes anything)
        ├── Domain workers, one per concern (graphics, systems, UI, …)
        ├── Tool sessions with hands (Blender MCP, engine MCP)
        └── Shared memory: decision record + plans + team trails
```

---

## 2. Roles

### 2.1 The human — art director
- Decides the look, always visually: generates/curates references until "damn, I love how this
  looks." Never delegates taste: *"don't ask AI what it thinks about it."*
- Approves everything that ships; is the final referee on every screenshot.
- Speaks rough intent to the Manager ("I want the lighthouse bigger") — precision is the
  Manager's job, not the human's.

### 2.2 The Manager — the one session that makes nothing
- **Never codes, never models.** Its outputs are: research, reworded instructions, dispatches,
  and records.
- Rewords the human's rough intent "in much better wording" and dispatches to the right worker.
- Researches ideas online before they become work (player reactions, prior art, techniques).
- Writes every locked decision to the record (§5.1).
- Workers report back to it; it runs the conversation until the human's requirement is done.

### 2.3 Domain workers — one concern each
- One session per domain: graphics, in-game systems, UI, audio — "they each work on a single
  thing."
- **Initialized with a lane and a fence** — first message: *"You will be the agent for X"*, with
  acting outside the area explicitly forbidden.
- On start, a new session reads the shared memory before touching anything.
- Workers may message each other directly and iterate together until the requirement is done;
  the human approves the result, not the chatter.

### 2.4 Tool sessions — hands, not minds
- Separate sessions own each MCP (one for Blender, one for the engine), used for making and
  importing artifacts — kept apart from the sessions that decide what to make.
- The integration session is deliberately not the modelling session: placement, scale, wiring
  is a different job from geometry.

---

## 3. The asset pipeline (per feature or asset)

**Step 1 — Reference first.** Generate concept images until the human loves one. The reference
decides the look; the human decides the reference. *Rule: the reference is a direction, not a
target — "never try to fully replicate it; you never will. Getting to a point you like is good
enough."*

**Step 2 — Geometry as script.** The Blender session writes the model as a generating script.
*The script is the source*: proportions stay editable, a family of assets stays a family, and a
wrong roof is a one-line fix and a re-run — never mesh surgery. (Chosen over generative-3D
services after paid trial: their meshes arrive high-poly, holey, and unfixable.) Low-poly is
correct when the camera is far: "you mostly see silhouette."

**Step 3 — Integrate in a different session.** Placement, waterline, scale, wiring, in-engine
texturing. Never the session that modelled it.

**Step 4 — Screenshots are the referee, from the consumption camera.** Everything is rendered
from the actual in-game/user viewpoint, and nothing counts until the human has looked. *The
pancake rule: an overhead check passed four islands that were flat pancakes in-game. Examine from
where the user stands, or the examination is void.*
*Under AgentBridge: any row that changes what the player sees carries in its done "the human has
approved consumption-camera screenshots" — the Reviewer's pass makes the row ready for that gate,
and the human's yes closes it. Batch screenshots so the human reviews on their own schedule; rows
that change nothing visible never wait on anyone.*

**Step 5 — Scored blind criticism.** For any large pass: write the scoring criteria BEFORE
changing anything; score each item /10; ship only at 8+. At least one critic reviews without
knowing which version is newer. *This is what stops "I changed a lot, so it must be better."*
Known limit: your criteria cannot catch what your criteria omit — so at each phase exit, run one
critic with a deliberately empty brief ("use this; say everything wrong" — no intention, no
qualities), and keep a real-player channel open (a public devlog works), its findings routed in
like any others. The evidence: one outside stranger's uncriteria'd glance caught a whole defect
class — doors facing nowhere, a levitating figure — that a 12-criteria blind pass had missed.

**Step 6 — Record the decision, with provenance** (§5.1).

---

## 4. The convergence loop

The inner engine for any item chased against a reference:

- **Pin the goal** (`/goal`): the fixed bar — the reference and what meeting it means — held
  durable across iterations and context compactions so rounds cannot drift.
- **Loop** (`/loop`): the session re-runs its own task, self-paced, until *it declares* the bar
  met — persistence is enforced by the mechanism, not by hoping.
- **Fan out with critics**: parallel subagents per item, each checked by a separate harsh-critic
  subagent that keeps it going until wowed.
- **Terminate on blind comparison**: put ours and the reference side by side, unlabelled; done
  is when the honest answer to "which looks better?" stops being the reference.
- Run at maximum effort for these passes; budget accordingly (see §7).
- *Under AgentBridge: a small taste note on already-passed visual work ("the lighthouse should be
  bigger") routes as an amendment dispatched immediately against a standing art-direction row —
  the taste gate above is its whole examination. The full row-and-plan-critic cycle is for
  structural work; taste micro-iteration is what this convergence loop is for.*

---

## 5. The rules

### 5.1 The decision record
- Every decision is written down **with provenance**: tagged by who decided — HUMAN or AI.
- **Human-tagged decisions cannot be overruled by AI.** Ever.
- Why the tag exists: an AI-suggested idea once sat untagged in the docs and was later quoted
  back to the human as his own intention. Untagged ideas launder themselves into false intent.
- Known failure at scale: an append-everything record becomes unreadable within weeks ("so many
  .md files I myself cannot follow them anymore"). Keep the record current-state and pruned;
  history belongs to version control, not to the living documents.
- **Visual boarding memory**: keep `design/references/` current in closing commits — per area,
  the approved reference image, the last human-approved consumption-camera screenshot, and the
  V-stage. Fresh sessions board visually, and the blind newer-vs-older critic gets its material
  for free.

### 5.2 Verification
- When the AI claims something is impossible or unsupported, **make it check online before
  accepting the claim** — "once it does, it will say 'you were right.'"
- Nothing is called done from a description; done is a screenshot from the consumption camera
  plus the human's eye (and for scored passes, the 8+ gate).

### 5.3 Scope and sequence
- **Platform is decided before starting** — it silently constrains everything (renderer,
  controls, performance). Performance claims are verified on the real target hardware, not the
  dev machine — "should be fine" shipped dropped frames.
- **UI is polished last**: mechanics keep demanding new UI elements; early UI polish is paid
  twice.
- **Stage everything V1/V2/V3**: V1 works, V2 is respectable, V3 is "close to finished-look."
  Name the stage when sharing, so nobody judges a V1 against a V3 bar. *Under AgentBridge: the
  row's done names its V-stage, so a V1 harbour is never examined against a finished-look bar.*
- Cut scope honestly and early — implemented features that fight the vision get removed, not
  defended.

---

## 6. Phases of a project (observed arc, generalizable)

**Phase 1 — Look and world (prove the feel).** References, palette/time-of-day, movement in the
space, the starting area blocked out. No real mechanics yet. Exit: the human loves how it looks
in motion.

**Phase 2 — Core mechanics (prove the game).** The one central mechanic built fully (with its
info surfaces), first real content, first cuts of over-scoped features. Exit: the core loop is
fun bare.

**Phase 3 — Studio maturation (prove the pipeline).** The workflow itself upgrades: MCP hands
arrive, real 3D replaces placeholders, the scored-criticism pass runs, graphics overhaul against
references, decision record formalized. Exit: assets flow reference → script → integration
without the human touching tools.

**Then per-area production loops** (repeat 3's pipeline per zone/feature) toward a playable
demo; V-stages track each area's distance from finished.

---

## 7. Deployment requirements

- **Sessions**: a desktop multi-session client with inter-session messaging (the dispatch
  backbone), plus terminal sessions for MCP tools (desktop sessions cannot spawn sessions).
- **Tools**: image generation for references (any good generator); Blender MCP; engine MCP
  (e.g., Godot); optional generated-audio service.
- **Models**: strongest model at max effort for heavy/convergence passes; a standard strong
  model for routine domain work — "after longer usage, not THAT much difference" for ordinary
  tasks.
- **Budget reality** (observed): ~$200/mo top-tier plan fully consumed in heavy build weeks;
  polish weeks barely dent it; MCP-driven work spends less than chat-driven. Plan max-effort
  convergence passes against the limit window — heavy passes early in the cycle, polish when
  limits run low — and write expected heavy-vs-light weeks into the blueprint's budgets. Plus small
  subscriptions for images/audio. Time: many hours a week, "mostly idle — agents work in the
  background."

---

## 8. Failure modes and their cures (the scars, kept visible)

| Failure | Cure (now a rule above) |
|---|---|
| Checked from a convenient angle, shipped broken from the real one | §3.4 consumption camera |
| "Changed a lot, must be better" | §3.5 criteria-before-changes, blind, 8+ |
| Own criteria miss whole defect classes | §3.5 fresh outside eyes, no criteria |
| AI idea quoted back as the human's own | §5.1 provenance tags |
| Generated meshes unfixable | §3.2 script-as-source |
| AI denies capability it has | §5.2 make it check online |
| Early UI polish paid twice | §5.3 UI last |
| Decision docs unreadable in weeks | §5.1 prune; current-state only |
| Scope grown past the vision | §5.3 cut early, honestly |
