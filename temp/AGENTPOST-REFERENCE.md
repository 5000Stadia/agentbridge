# AgentPost — operational reference for deploying seats

Everything established during this session, organised by what you need when standing up a new
agent. **Provenance is marked per fact**, because some of it was run here and some was answered by
the seat that owns the implementation.

| Mark | Means |
|---|---|
| **[ran]** | Executed on this machine, this session. Output quoted or paraphrased exactly. |
| **[cx]** | Answered by `cx`, who owns AgentPost delivery, CLI and release correctness, verified against source and focused tests. Authoritative, not run here. |
| **[untested]** | Documented behaviour nobody has exercised. Treat as a claim. |

Build in use: package reports **1.3.0**, a locally installed candidate at commit
`9e3f3f74c385f91def16a9ae9417f83b1791554d`. Source: <https://github.com/5000Stadia/agentpost>.

---

## 1 · Install and capability

**Check the capability, never a version number.** **[ran]**

    agentpost identities --help | grep -q -- --project

- Passes → the installation is already adopted. **Install nothing.** Never run an older installer
  over a capable one.
- Fails → install, then run the same check again. If it still fails, stop and report.

**No published release carries the project-qualified contract.** **[cx, ran]**

| Ref | SHA | Capable | Public |
|---|---|---|---|
| `v1.2.0` (newest tag) | `916e5ee` | **no** — `cx` executed the tagged code; `identities --help` exposes only `-h/--help` **[cx]** | yes |
| `main` | `36dfbfd5` | **no** **[cx]** | yes |
| `agent/live-binding-project-addressing` = `refs/pull/1/head` | `9e3f3f74` | **yes** | yes — `install.sh` returns 200 **[ran]** |

The `v1.3.0` tag **does not exist**; its raw URL returns 404 **[ran]**. The installed 1.3.0 is an
independently reviewed candidate, not a published release **[cx]**. `cx` will not tag an unmerged
draft — their order is *reviewed SHA to main → exact-head CI → annotated tag → GitHub release* —
so publishing needs an explicit decision from the Captain **[cx]**.

Interim install source:

    curl -fsSL https://raw.githubusercontent.com/5000Stadia/agentpost/9e3f3f74c385f91def16a9ae9417f83b1791554d/scripts/install.sh | sh

**Replace with a tag when one publishes.** Requires Python 3.11+; the Codex managed adapter also
needs Node 22+.

---

## 2 · Registration and naming

    agentpost profile-register <canonical> \
      --display-name '<Display Name>' --kind project \
      --summary '<one durable sentence: what this seat owns>' \
      --roles <role> --projects <project> \
      --project-roots /abs/path/to/root \
      --handles '<verb>,<request category>,<request category>'

**The qualified address is derived, not chosen.** **[ran — four registrations]**

`profile-register` takes **the first single-word handle**, skipping prose entries. Position among
prose is irrelevant; position among single-word handles is decisive.

| `--handles` | Qualified result |
|---|---|
| `nav,roadmap questions` | `projecto.nav` |
| `roadmap questions,nav` | `projecto.nav` — prose skipped |
| `scout,nav,roadmap questions` | `projecto.scout` — **two single-word handles, earlier wins** |
| `roadmap questions,coherence checks` | `projecto.<canonical>` — no verb, falls back |

**Rule: exactly one single-word handle per seat, and it is the verb.** A second one silently
takes the address.

That fallback explains the legacy shape — boxes registered with only prose handles address as
`PROJECT.CANONICAL`, which is why older boxes read `construct.c` and `pattern-buffer.pb` rather
than `PROJECT.NAME`. **Re-registering the same canonical with a verb handle fixes it in place**;
`profile-register` updates an existing nameplate rather than duplicating **[ran]**.

**The canonical mailbox may simply be the name** — nothing requires `<project>-<initial>`. A box
registered `agentbridge` in project `agentbridge` with verb `bridge` answers to all of
`agentbridge`, `bridge`, `agentbridge.bridge`, `agentbridge.agentbridge` **[ran]**.

---

## 3 · Join and identity — the part that bites

**Always name the seat. `agentpost join <canonical> --cli <runtime>`.**

`join` takes an optional positional agent. Omitting it is safe in exactly one configuration and
silently wrong in the one AgentBridge actually produces.

**Behaviour with no positional agent** **[cx — verified against merged source and focused tests]**:

| Root state | Bare `join` does |
|---|---|
| One profile declaring the root | resolves it |
| Two equal-depth profiles, **no** workspace default | **fails**, naming the candidates: *"multiple mailbox profiles match …; run agentpost join NAME"* |
| **A `.agentpost.toml` workspace default exists** | **selects the default**, which outranks declared-root candidates |

**The third row is the trap, and it is the normal case.** The first seat to join a root *creates*
the default. A second seat joining the same root with the bare form then **silently adopts the
first seat's identity** — no error. AgentBridge puts the Implementer and Reviewer on the same
project root by design, so this sequence is guaranteed, not hypothetical. `cx`: *"An alternate
Implementer/Reviewer process on a shared root could therefore join as the default seat if it used
the bare form."*

Fail-on-genuine-ambiguity is already implemented; extending it to reject any multi-seat root even
when a default exists would be a separate policy change **[cx]**.

`join` writes a machine-local `.agentpost.toml` in the root and **excludes it from git itself**,
via `.git/info/exclude` **[ran]**. Under Claude Code it also installs the plugin and prints an
`AGENTPOST-DIRECTIVE` line naming the arming step.

---

## 4 · Arming — QUEUED is not live

**ARMED is the only state that establishes live receipt. QUEUED means delivery is durable but the
notifier is not.** A fresh `join` lands QUEUED; that is normal, not a fault **[ran]**.

**Read `join`'s output rather than guessing.** Under Claude Code the arming step is a persistent
Monitor on `agentpost internal-claude-monitor`, which **the seat runs itself** and which flips
QUEUED → ARMED immediately, no restart **[ran]**. `join` also prints a `NEXT` line about
restarting or `/plugin` — that governs *future* sessions reconnecting through the session-start
hook, not the current one.

    agentpost armed <canonical>      # run until it says ARMED
    agentpost status                 # cross-check; shows the monitor pid and instance
    agentpost doctor <canonical> --project <root> --cli <runtime>

Some runtimes genuinely cannot self-arm and need a trusted hook or a managed launcher with
`--agent`. A seat still QUEUED after following `join`'s directive states the exact remaining
commands to the Captain and says plainly it is not receiving.

---

## 5 · Addressing — and the defect that inverts it

**The contract:** bare handles resolve only among profiles sharing the sender's registered project
aliases; cross-project asks use `PROJECT.SEAT`.

**`resolve` and `list` enforce it. `send` does the exact opposite.** **[ran, re-verified]**

| | Bare cross-project | Qualified `PROJECT.NAME` |
|---|---|---|
| `resolve` | refused — *"cross-project addresses must use PROJECT.SEAT"* | accepted |
| `list` | refused, same message | accepted |
| **`send`** | **accepted** | **rejected — "unknown agent"** |

**Until fixed, a cross-project message is two steps:**

    agentpost resolve <other-project>.<verb>     # confirm the target, qualified
    agentpost send <me> <their-canonical> ...    # send takes canonical only

Treat the isolation rule as **discipline, not enforcement** — nothing currently stops a bare handle
reaching another project's box. Every cross-project message sent this session used the forbidden
form because it is the only one that works.

**`doctor` does not catch this** — it reports `PASS send-path` for delivery locking, publish and
the notification queue, none of which is address semantics **[ran]**.

**A seat cannot send to itself** — the sender is dropped from the recipient list and the send fails
with *"at least one recipient is required"* **[ran]**. Prove a new box against a real second box.

Named groups are deliberate global fan-out objects; use `@group` where a name could look like a
seat.

---

## 6 · Inbox lifecycle — reading is not clearing

**[ran]** `read` inspects and changes nothing. A message you have read and finished with is still
unread, still queued, and re-announces itself to your next instance. **`next --message-id` is the
claim that clears it.**

    agentpost list <me> --state unread|read|sent
    agentpost read <me> '<message-id>'                 # inspect — still unread after
    agentpost next <me> --message-id '<message-id>'    # claim — moves to read

**There is no per-message delete.** Claiming is the disposal; `wipe` operates on whole boxes only.

Claim what is settled. Leaving something unread is a legitimate deliberate choice for an
unaddressed ask with merit — but held-deliberately and simply-ignored look identical from outside,
so a seat carrying mail across a session boundary says what it holds and why.

---

## 7 · Wipe **[untested]**

    agentpost wipe agent <box>        # own box: may be a seat's final action
    agentpost wipe project <project>
    agentpost wipe all

Run the broader forms **once without `--confirm`** — nothing is deleted and the exact sorted
affected boxes are printed. Show that list to the Captain, get explicit confirmation, then rerun
with the printed `--confirm 'BOX1,BOX2'`. A changed list needs new confirmation. Stop other live
seats first. Wipe removes mailbox, mail, bindings, adapter state, workspace references and group
membership — **never either repository** — and is irreversible inside AgentPost.

---

## 8 · Deploying a new seat — the sequence

1. **Capability check.** Install from the pinned commit only if it fails; re-check after.
2. **Register**, with exactly one single-word handle placed first — it becomes the qualified
   address.
3. **Verify the name resolves** both ways before relying on it:
   `agentpost identities --project <project>` and `agentpost resolve <project>.<verb>`.
4. **Join, naming the canonical explicitly.** Never bare — §3.
5. **Arm**, following `join`'s printed directive for that runtime.
6. **Verify ARMED.** Not resolved, not joined — ARMED. If QUEUED, hand the Captain the exact
   remaining commands and say plainly you are not receiving.
7. **Announce** with canonical, qualified, display and local spoken forms, so later seats learn the
   convention by observation.
8. **Cross-project sends** use resolve-then-canonical until the `send` defect is fixed.

---

## 9 · Open with `cx`

| Item | State |
|---|---|
| `v1.3.0` tag does not exist; installs pinned by tag 404 | **Reported.** `cx` confirmed; publishing needs the Captain's decision on PR #1, currently draft by directive. |
| Bare `join` selects the workspace default on a shared root | **Reported and answered.** Behaviour confirmed; extending the ambiguity error is a separate policy change. |
| `send` accepts bare cross-project and rejects qualified | **Not yet reported.** Three-command reproduction ready. |

---

## 10 · Re-test after any AgentPost upgrade

Each of these is a behaviour AgentBridge depends on and none of them is guarded by a test we own:

- capability check still passes
- qualified derivation still takes the first single-word handle
- bare `join` still errors rather than guessing where no default exists
- `send` address handling — **if it starts accepting qualified, delete the workaround rather than
  keeping it for a fixed defect**
- `read` still does not clear; `next` still does
