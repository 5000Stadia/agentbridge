# Crew — standing seats

Read this only when the front door chose standing seats. It adds to `design/method.md` and changes
nothing in it; when a project uses it, copy it into the project as `design/crew.md` so every seat
can read it.

Three seats: the Navigator, a standing Builder and a standing Reviewer. Launch them once the
blueprint and the first row exist.

**What each seat holds.** The Navigator holds the intention and writes the program the others run:
it hands each row over only once what the row stands on is real, answers forks from the whole
picture or carries them to the human, judges deadlocks by evidence, and publishes. It never relays
between the others and never narrates — a Navigator busy with traffic has stopped authoring. The
Builder plans, builds and closes each row, and when a row passes sends the Navigator the examined
commit and the closing commit. The Reviewer performs both examinations from the briefs in the
method, against the exact coordinates it is handed, and sends back unread anything that does not
resolve. It judges against *What "good" means here* rather than its own taste, and where the work
touches something the anchor also does, it puts both on the table. It never writes the fix,
because a reviewer that authors the code can no longer examine it.

**Checkouts.** The Reviewer keeps its own worktree so it can check out any commit without
disturbing work in progress, and leaves it clean after every examination. The Navigator and the
Builder share the root, so each stages by explicit path, or one commits the other's half-finished
work.

**The channel is AgentPost.** Its skill owns the commands; follow it over anything written here.
If AgentPost is not installed, tell the human what installing it takes and let them choose between
that and giving up standing seats — do not invent a channel, and do not quietly run as one agent,
because the seats were chosen for the seams. Anything decided on the channel goes into the design
documents, because mail scrolls away.

**A seat is ready when its round trip lands,** not when it was launched: its message out, your
reply arriving as a live wake. A fresh directory can sit silently at a trust prompt, and a waiting
seat looks exactly like a working one — grant trust in the same act as the launch, and if a seat
never speaks, look at its terminal. The same seat blocked twice means the launch is wrong; fix the
launch, not the seat.

**Dead air at the seams is the Navigator's to own.** A crew stalls between seats, not inside them,
and a waiting pipeline looks like a working one until the human asks. Keep one question answerable
at all times: who owes the next action, and are they moving? Moving means recent output, not a
live process — a wedged seat holds its "busy" forever — and recent output is proof of life, not of
progress. If work will ever wait on a seat or a machine while nobody is watching, set up something
that notices a handoff unclaimed past a healthy wake, a claimed row running well past what its
handoff expected, and nobody holding work that is owed. The mail store shows letters sent and
answered; where it does not record when a letter was claimed, the watcher records it the first
time it sees it. It nudges the Navigator and judges nothing. On one crewed run, fifty-six owed
images sat three and a half hours while every watcher watched a stage and nobody watched the
baton.

**Closing.** At *Done*, end the seats' runtimes and remove every worktree still standing — the
Reviewer's and any critic's — once what is worth keeping is out of them. Critic checkouts are
removed as each critic returns, not saved for the end: on one long-lived crew, a hundred standing
checkouts filled the disk before *Done* ever came.
