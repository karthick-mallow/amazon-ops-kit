# Amazon Activity Tracker

The shared memory for this seller business: every analysis, decision and change made with any AI
assistant, in one place. Any AI tool that can reach this repository picks up the same history, the
same open threads and the same rules — whatever data source the numbers come from.

- **Rules for AI assistants:** [`AGENTS.md`](AGENTS.md)
- **Where things stand now:** [`STATE.md`](STATE.md)
- **Every activity, newest first:** [`tracker.csv`](tracker.csv) → pages in [`activities/`](activities)
- **Lessons learned:** [`LESSONS.md`](LESSONS.md)
- **Accounts, data sources and goals:** [`config.md`](config.md)

Keep this repository **private**. It holds commercial data.

## Connect an AI tool

Every tool needs two things:

1. **This repo** — the memory.
2. **Your data** — either a connector (an MCP server such as KwickMetrics, another seller tool or
   Amazon Ads) or reports you download from Seller Central / the Ads console and upload in the
   chat. Without either, a tool can read and discuss the history but must not quote current
   figures.

| Tool | Reads the rules on its own? | Repo access | Data from a connector |
|---|---|---|---|
| Claude (app, Cowork) | Yes, via the Amazon Ops Copilot plugin | Plugin's GitHub connector | Plugin's KwickMetrics connector, or any connector you add |
| Claude Code | Yes (`CLAUDE.md` → `AGENTS.md`) | Clone the repo | `claude mcp add --transport http <name> <url>` |
| OpenAI Codex (CLI, IDE, cloud) | Yes (`AGENTS.md`) | Clone, or connect the repo in Codex cloud | Remote MCP server in `~/.codex/config.toml` (below) |
| Gemini CLI | Yes (`GEMINI.md` → `AGENTS.md`) | Clone the repo | Remote MCP server in `.gemini/settings.json` (below) |
| Cursor, GitHub Copilot | Yes (`AGENTS.md`; Copilot also `.github/copilot-instructions.md`) | Open the cloned repo | The tool's MCP settings |
| ChatGPT | No — paste [`PROMPT.md`](PROMPT.md) into a Project's instructions | Developer mode → add a GitHub MCP connector (write access) | Developer mode → add a custom connector |
| Grok | No — paste [`PROMPT.md`](PROMPT.md) into custom instructions | GitHub connector (Settings → Connectors) | "Bring your own MCP" |

Every tool that accepts file uploads can also work from **reports you upload** instead of a
connector.

Tools that can read but not write the repo hand you the page, the CSV row and the `STATE.md`
changes as ready-to-commit blocks; commit them (or ask a tool with write access to) so nothing is
lost.

### Example connector: KwickMetrics

MCP server URL: `https://mcp.api.kwickmetrics.com/mcp/kwickmetrics`. Any other MCP server is added
the same way with its own name and URL.

Codex — `~/.codex/config.toml`:

```toml
[mcp_servers.kwickmetrics]
url = "https://mcp.api.kwickmetrics.com/mcp/kwickmetrics"
```

Then sign in with `codex mcp login kwickmetrics`.

Gemini CLI — `.gemini/settings.json`:

```json
{
  "mcpServers": {
    "kwickmetrics": { "httpUrl": "https://mcp.api.kwickmetrics.com/mcp/kwickmetrics" }
  }
}
```

Whether a data provider accepts sign-in from a given AI tool is up to that provider. If a tool
cannot connect, ask the provider's support, or work from uploaded reports.

### GitHub access for chat apps

Use a fine-grained personal access token limited to **this repository** with **Contents: read and
write**. Give each tool its own token so you can revoke one without affecting the others.

## How every tool keeps the memory consistent

1. Start of a conversation: read `AGENTS.md`, `config.md`, `STATE.md`, `LESSONS.md` and the recent
   rows of `tracker.csv`.
2. Get current numbers from the data source; never reuse old figures as live data.
3. Before suggesting anything: check the last 90 days of related activity.
4. Log: changes made through a connected tool automatically; anything else only with the seller's
   approval. Each entry — a page in `activities/`, a top row in `tracker.csv`, an updated
   `STATE.md` — records the AI tool, model and data source.
