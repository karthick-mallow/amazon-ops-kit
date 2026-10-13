# Amazon Activity Tracker

The shared operating memory for this seller business: every analysis, decision and change made
with any AI assistant, in one place. Any AI tool that can reach this repository picks up the same
history, the same open threads and the same rules.

- **Rules for AI assistants:** [`AGENTS.md`](AGENTS.md)
- **Where things stand now:** [`STATE.md`](STATE.md)
- **Every activity, newest first:** [`tracker.csv`](tracker.csv) → pages in [`activities/`](activities)
- **Lessons learned:** [`LESSONS.md`](LESSONS.md)
- **Settings:** [`config.md`](config.md)

Keep this repository **private**. It holds commercial data.

## Connect an AI tool

Every tool needs two things: access to **this repo** (memory) and access to **KwickMetrics** (live
data, MCP server `https://mcp.api.kwickmetrics.com`). Without KwickMetrics a tool can read and
discuss the history but must not quote current figures.

| Tool | Reads the rules on its own? | Repo access | KwickMetrics access |
|---|---|---|---|
| Claude (app, Cowork) | Yes, via the Amazon Ops Copilot plugin | Plugin's GitHub connector | KwickMetrics connector |
| Claude Code | Yes (`CLAUDE.md` → `AGENTS.md`) | Clone the repo | `claude mcp add --transport http kwickmetrics https://mcp.api.kwickmetrics.com` |
| OpenAI Codex (CLI, IDE, cloud) | Yes (`AGENTS.md`) | Clone, or connect the repo in Codex cloud | Remote MCP server in `~/.codex/config.toml` (below) |
| Gemini CLI | Yes (`GEMINI.md` → `AGENTS.md`) | Clone the repo | Remote MCP server in `.gemini/settings.json` (below) |
| Cursor, GitHub Copilot | Yes (`AGENTS.md`; Copilot also `.github/copilot-instructions.md`) | Open the cloned repo | The tool's MCP settings, same URL |
| ChatGPT | No — paste [`PROMPT.md`](PROMPT.md) into a Project's instructions | Developer mode → add a GitHub MCP connector (write access) | Developer mode → add a custom connector with the KwickMetrics URL |
| Grok | No — paste [`PROMPT.md`](PROMPT.md) into custom instructions | GitHub connector (Settings → Connectors) | "Bring your own MCP" with the KwickMetrics URL |

Tools that can read but not write the repo hand you the page, the CSV row and the `STATE.md`
changes as ready-to-commit blocks; commit them (or ask a tool with write access to) so nothing is
lost.

### Codex — `~/.codex/config.toml`

```toml
[mcp_servers.kwickmetrics]
url = "https://mcp.api.kwickmetrics.com"
```

Then sign in with `codex mcp login kwickmetrics`.

### Gemini CLI — `.gemini/settings.json`

```json
{
  "mcpServers": {
    "kwickmetrics": { "httpUrl": "https://mcp.api.kwickmetrics.com" }
  }
}
```

### GitHub access for chat apps

Use a fine-grained personal access token limited to **this repository** with **Contents: read and
write**. Give each tool its own token so you can revoke one without affecting the others.

Whether KwickMetrics accepts sign-in from a given AI tool is up to KwickMetrics. If a tool cannot
connect, ask KwickMetrics support.

## How every tool keeps the memory consistent

1. Start of session: read `AGENTS.md`, `config.md`, `STATE.md`, `LESSONS.md` and the recent rows of
   `tracker.csv`.
2. Pull live numbers from KwickMetrics; never reuse old figures.
3. Propose changes as a table; change the account only after explicit approval.
4. Log: new page in `activities/`, new top row in `tracker.csv`, refresh `STATE.md`, add a lesson
   if one was learned — all in one commit tagged with the AI client that did the work.
