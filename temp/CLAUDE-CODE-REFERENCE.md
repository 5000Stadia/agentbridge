# Claude Code — working reference

**There is no shipped manual.** Unlike Codex, Claude Code does not install a self-documenting
`.md` on disk. This file is assembled, not copied.

**Provenance — check this before trusting any line below.**

| Source | Trust | Gathered |
|---|---|---|
| `claude --help` on this machine | verified locally | v2.1.220 |
| `/home/k/.claude/cache/changelog.md` | verified locally | v2.1.220 |
| AgentPost plugin `hooks/hooks.json` | verified locally — a working hook example | 0.0.7 |
| `code.claude.com/docs/en/hooks`, `/settings` | fetched, not executed | 2026-07-28 |

**The hook surface moves between releases.** `DirectoryAdded` landed in 2.1.219, one version
before this. Re-fetch rather than trusting this file after an update. `docs.claude.com/en/docs/
claude-code/*` now 301s to `code.claude.com/docs/en/*`.

This is scoped to what AgentBridge would plausibly use. It is not a mirror of the full docs.

---

## 1. Configuration — where it lives, what wins

| Scope | Path | Precedence | In git? |
|---|---|---|---|
| Managed / policy | IT-deployed `managed-settings.json` | 1 (highest) | admin |
| CLI flags | — | 2 | — |
| Local | `.claude/settings.local.json` | 3 | no (gitignored) |
| **Project** | **`.claude/settings.json`** | 4 | **yes — this is the shareable one** |
| User | `~/.claude/settings.json` | 5 (lowest) | no |

**Permissions merge across scopes rather than override.** Every other key follows precedence.

On this machine: user settings hold `permissions`, `hooks` (Stop + PermissionRequest → `beep.sh`),
`enabledPlugins`, `effortLevel`, `theme`. The repo holds only
`.claude/settings.local.json` with the AgentPost plugin enabled.

### Permissions

```json
{ "permissions": {
    "allow": ["Bash(npm run test *)", "Read(~/.zshrc)"],
    "deny":  ["Bash(curl *)", "Read(./.env)", "Read(./secrets/**)"],
    "ask":   ["Write(./config/**)"] } }
```

`ToolName(pattern)`; `*` within a path segment, `**` across segments. **Deny beats allow.**
Arrays merge across scopes.

---

## 2. Hooks

### Configuration shape

```json
{ "hooks": {
    "PreToolUse": [
      { "matcher": "Bash",
        "hooks": [ { "type": "command",
                     "if": "Bash(git push *)",
                     "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/gate.sh",
                     "args": [] } ] } ] } }
```

Placeholders available in commands and as env vars: `${CLAUDE_PROJECT_DIR}`,
`${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`.

Hooks may also ship from a **plugin** (`hooks/hooks.json`, the AgentPost pattern) or from
**skill/agent frontmatter** while that skill or agent is active.

### Events

**Session** — `SessionStart` (matcher: `startup|resume|clear|compact|fork`), `SessionEnd`
(`clear|resume|logout|prompt_input_exit|other`), `Setup`.

**Turn** — `UserPromptSubmit`, `UserPromptExpansion`, `Stop`, `StopFailure` (matcher: error type,
e.g. `rate_limit`, `overloaded`).

**Tools** — `PreToolUse`, `PermissionRequest`, `PermissionDenied`, `PostToolUse`,
`PostToolUseFailure`, `PostToolBatch`. Matcher is the tool name.

**Subagents/tasks** — `SubagentStart`, `SubagentStop` (matcher: agent type), `TaskCreated`,
`TaskCompleted`, `TeammateIdle`.

**Files/config** — `FileChanged` (a watched file changed on disk), `CwdChanged`, `DirectoryAdded`,
`ConfigChange`, `InstructionsLoaded` (CLAUDE.md / `.claude/rules/*.md` loaded),
`WorktreeCreate`, `WorktreeRemove`.

**Other** — `MessageDisplay`, `Notification`, `PreCompact`/`PostCompact` (`manual|auto`),
`Elicitation`, `ElicitationResult`.

### Input (stdin JSON, common fields)

`session_id`, `prompt_id`, `transcript_path`, `cwd`, `permission_mode`, `effort.level`,
`hook_event_name`, plus `agent_id` / `agent_type` inside subagents. Tool events add
`tool_input`.

### Output

Universal: `continue` (false stops Claude), `stopReason`, `suppressOutput`, `systemMessage`,
`additionalContext`.

Block via top-level `decision` on `UserPromptSubmit`, `PostToolUse`, `Stop`, `SubagentStop`,
`PreCompact`, others:

```json
{ "decision": "block", "reason": "why" }
```

`PreToolUse` uses its own shape — and can **rewrite the call**, not just refuse it:

```json
{ "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny|ask|defer",
    "permissionDecisionReason": "...",
    "updatedInput": { },
    "additionalContext": "..." } }
```

`SessionStart` can inject context and more:

```json
{ "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "...",
    "initialUserMessage": "...",
    "watchPaths": ["PROJECT-BOARD.md"],
    "sessionTitle": "...",
    "reloadSkills": true } }
```

`Stop` / `SubagentStop` may return `additionalContext`, which Claude sees and can act on.
`PostToolUse` may return `updatedToolOutput`.

### Exit codes

| Code | Effect |
|---|---|
| 0 | success; stdout parsed as JSON |
| **2** | **blocking** — stderr becomes the reason |
| other (incl. **1**) | non-blocking; stderr shown in transcript |

**Exit 1 does not block.** Use exit 2 to enforce anything.

Blocks on exit 2: `PreToolUse`, `PermissionRequest`, `UserPromptSubmit`, `UserPromptExpansion`,
`Stop`, `SubagentStop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted`; any non-zero fails
`WorktreeCreate`. Does **not** block: `PostToolUse`, `PostToolUseFailure`, `PermissionDenied`,
`Notification`.

### Matchers

`"*"` / `""` / omitted matches all. Letters, digits, `_`, `-`, space, `,`, `|` are exact or
alternation (`Edit|Write`). Any other character makes it an **unanchored JavaScript regex**
(`^Notebook`, `mcp__memory__.*`).

MCP tools are `mcp__<server>__<tool>`.

### `if` conditions — the important one for command gating

Narrows a tool event using permission-rule syntax: `{"if": "Bash(git *)"}`, `{"if": "Edit(*.ts)"}`.

For Bash specifically:
- `VAR=value` prefixes are stripped before matching
- **each subcommand in a chain is checked** — `npm test && git push` matches both
- **commands inside `$()` and backticks are also checked**

That last pair is what makes a Bash `if` gate hard to smuggle past by accident.

### Handler types

| Type | Receives | Returns |
|---|---|---|
| `command` | JSON on stdin | exit code + stdout JSON |
| `http` | JSON POST body | 2xx + JSON |
| `mcp_tool` | tool args (`${tool_input.x}` substitution) | tool output |
| `prompt` | prompt text | LLM yes/no decision |
| `agent` | tool args | subagent decision (experimental) |

Common fields: `if`, `timeout`, `statusMessage`, `once` (run once per session, then removed).
`command` adds `args` (exec form, no shell), `async`, `asyncRewake` (background, wake on exit 2),
`shell`.

### Inspecting and disabling

`/hooks` browses configured hooks read-only. `disableAllHooks: true` kills all hooks **and the
custom status line**. `claude --debug hooks` shows execution.

---

## 3. CLI surface worth knowing (verified, v2.1.220)

**Identity and scope** — `--agent <name>` (run main thread as a named subagent — this is the
switch AgentBridge means by "any `--agent` switch"), `--agents <json>` (define inline),
`--add-dir` (extra allowed directories — relevant to sibling-repo layouts), `--model`,
`--effort <low|medium|high|xhigh|max>`, `-n/--name`.

**Config control** — `--settings <file-or-json>`, `--setting-sources user,project,local`,
`--plugin-dir`, `--mcp-config`, `--strict-mcp-config`, `--system-prompt`,
`--append-system-prompt`.

**Bypass — matters for any hook-based rule** — `--safe-mode` disables CLAUDE.md, skills, plugins,
**hooks**, MCP, custom commands, agents, output styles. `--bare` skips hooks, plugin sync,
CLAUDE.md auto-discovery. `--dangerously-skip-permissions` bypasses permission checks.

**Headless** — `-p/--print`, `--output-format text|json|stream-json`, `--input-format`,
`--json-schema`, `--max-budget-usd`, `--include-hook-events`, `--no-session-persistence`.

**Session** — `-c/--continue`, `-r/--resume`, `--fork-session`, `--session-id`, `--from-pr`,
`--bg/--background`, `--remote-control`, `--worktree` (+ `--tmux`).

**Subcommands** — `agents`, `auth`, `doctor`, `mcp`, `plugin`, `project`, `install`,
`update`, `setup-token`, `gateway`, `ultrareview`.

---

## 4. Where customisation lives

| What | Path | Notes |
|---|---|---|
| Memory / instructions | `CLAUDE.md`, `.claude/rules/*.md` | auto-loaded; `InstructionsLoaded` fires |
| Subagents | `.claude/agents/*.md` | frontmatter sets model, tools, description |
| Skills / slash commands | `.claude/skills/`, plugin skills | invoked as `/name` |
| Hooks | `.claude/settings.json` → `hooks` | or plugin `hooks/hooks.json` |
| Plugins | marketplace + `enabledPlugins` | can bundle hooks, skills, agents, MCP |
| Status line | `statusLine` in settings | killed by `disableAllHooks` |

---

## 5. Honest limits

- **Hooks are not a security boundary.** `--safe-mode`, `--bare`, and `disableAllHooks` each turn
  them off. They stop accidents and drift, not a determined process.
- **The `prompt` and `agent` handler types put an LLM in the enforcement path.** By AgentBridge's
  own standard — *instruments get the same scrutiny as code* — those are instruments with the
  reviewed party's blind spots. Prefer `command` for anything that gates.
- **Everything in §2 is fetched, not executed.** Nothing here has been run on this machine except
  the AgentPost plugin's four hooks. Verify before relying.
