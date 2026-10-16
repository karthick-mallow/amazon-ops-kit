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

## Recommended AI tools

Use these four. Stick to the ones you need — every extra tool is another key to manage and another
place changes can come from.

| Tool | Best for | Reads the rules | Saves to this repo |
|---|---|---|---|
| **Claude** (desktop app) | Your main tool: day-to-day analysis and changes | Automatically, via the Amazon Ops Copilot plugin | Automatically |
| **Codex** | A second opinion and deeper analysis | Automatically (`AGENTS.md`) | Commits and pushes |
| **Cursor** | Working with files: report exports, bulk listing edits, sheets | Automatically (`AGENTS.md`) | Commits and pushes |
| **Grok** | Quick checks on your phone | Paste [`PROMPT.md`](PROMPT.md) into its custom instructions | Through its GitHub connector |

Every tool needs two things: **this repo** (the memory) and **your data** — a connector to your
seller tool (an MCP server, e.g. KwickMetrics) or reports you download from Seller Central / the
Ads console and share in the chat. The first tool you open on a new tracker sets it up by asking
one question (see `AGENTS.md`, section 0).

### Claude

1. In the Claude desktop app: **Customize → Plugins → + Add → Add marketplace** →
   `karthick-mallow/amazon-ops-kit` → add **Amazon Ops Copilot**.
2. On the plugin's **Connectors** tab: **github** → No sign-in, request header
   `Authorization: Bearer <your key>`. Connect your data tool too (KwickMetrics is listed there).
3. In a Cowork task, type **Set up my tracker**. Claude asks one question and finishes setup.

### Codex

1. Open this repo in Codex: clone it and open the folder in the Codex app, IDE extension or CLI —
   or connect the repo in Codex cloud. Codex reads `AGENTS.md` by itself.
2. Data connector (optional): add it to `~/.codex/config.toml`, then sign in:

   ```toml
   [mcp_servers.kwickmetrics]
   url = "https://mcp.api.kwickmetrics.com/mcp/kwickmetrics"
   ```

   `codex mcp login kwickmetrics` — or skip this and share report files instead.
3. Ask about your business as usual. Let Codex commit and push when it saves an activity.

### Cursor

1. **Clone** this repo in Cursor and open it. Cursor reads `AGENTS.md` by itself.
2. Data connector (optional): **Cursor Settings → MCP → Add new MCP server**, or add
   `.cursor/mcp.json` to your user folder:

   ```json
   { "mcpServers": { "kwickmetrics": { "url": "https://mcp.api.kwickmetrics.com/mcp/kwickmetrics" } } }
   ```

   Or skip it and drop report files into the chat.
3. Work in **Agent** mode. Let it commit and push when it saves an activity.

### Grok

1. Paste the text from [`PROMPT.md`](PROMPT.md) into Grok's **custom instructions**.
2. **Connectors:** add **GitHub** and give it access to this repo; add your data tool as a
   **Custom** connector with its MCP server URL (e.g.
   `https://mcp.api.kwickmetrics.com/mcp/kwickmetrics`), or upload reports instead.
3. If Grok can't write to the repo, it hands you the entry as text: save it with Claude, Codex or
   Cursor.

### Other tools (advanced)

ChatGPT (Developer mode, with `PROMPT.md` in a Project), Gemini CLI (`GEMINI.md`), GitHub Copilot
(`.github/copilot-instructions.md`) and Claude Code (`CLAUDE.md`) follow the same `AGENTS.md`
rules. They aren't part of the recommended set.

### GitHub keys

Use a fine-grained personal access token limited to **this repository** with **Contents: Read and
write**. Give each tool its own key so you can revoke one without affecting the others. Never
paste a key into a chat.

Whether a data provider accepts sign-in from a given AI tool is up to that provider. If a tool
cannot connect, ask the provider's support, or work from uploaded reports.

## How every tool keeps the memory consistent

1. Start of a conversation: read `AGENTS.md`, `config.md`, `STATE.md`, `LESSONS.md` and the recent
   rows of `tracker.csv`.
2. Get current numbers from the data source; never reuse old figures as live data.
3. Before suggesting anything: check the last 90 days of related activity.
4. Log: changes made through a connected tool automatically; anything else only with the seller's
   approval. Each entry — a page in `activities/`, a top row in `tracker.csv`, an updated
   `STATE.md` — records the AI tool, model and data source.
