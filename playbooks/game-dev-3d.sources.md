# Sources — game-dev-3d

Routes verified 2026-08-18, by the profiling pass that drafted the playbook. Reddit's own
front door (www/old/.json/mirror frontends) returns 403 or a JS shell to agents — the archive
API below is the way in. Share links (`/s/`) resolve to real post IDs via the redirect
`location` header with a browser user-agent, no page fetch needed.

## u/RUSuper — fishing-game series, weeks 1–3, with comment threads
- Route: `https://arctic-shift.photon-reddit.com/api/posts/ids?ids=1vlhel8,1vnjw0v,1vrjryf`;
  comments per post: `.../api/comments/search?link_id=<id>` (plain id, no `t3_` prefix, omit
  `limit` if 422)
- Feeds: §2 (roster, dispatch, init), §3 (whole pipeline), §5 (all three rule groups), §6, §8
- Taught: the studio structure, the pancake rule, provenance tags, script-as-source, every scar
- Verified: 2026-08-18

## u/RUSuper — author history (workflow answers scattered across threads)
- Route: `https://arctic-shift.photon-reddit.com/api/comments/search?author=RUSuper&limit=100`
  and `.../api/posts/search?author=RUSuper&limit=100`
- Feeds: §2.6 (models/money/time), §5.2 (verify-online), §6 (arc), §7 (budget reality)
- Taught: session-per-concern mechanics, Send Message dispatch, cost and pacing truth the posts
  omit, the prior-projects timeline
- Verified: 2026-08-18

## u/BoneShaman — "Claude Bandicoot", the Shumer gauntlet run
- Route: resolve `reddit.com/r/ClaudeAI/s/bENDr7JFsf` via redirect header → post `1v9m76g` →
  same archive API as above
- Feeds: §4 (the convergence loop, verbatim template and cost reality)
- Taught: the /goal + /loop gauntlet as run in practice — 3×5h max-effort windows, blind
  side-by-side termination, zero-asset generation from code
- Verified: 2026-08-18

## Basecamp — Shape Up (free online book, pitch chapters)
- Route: `basecamp.com/shapeup` — direct fetch works, no gate
- Feeds: §3.5 (criteria-before-changes framing), §5 (honesty mechanics behind the scored pass)
- Taught: problem-as-evidence, appetite-not-estimate, explicit no-gos — the anchor register for
  honest scoping documents
- Verified: 2026-08-18
