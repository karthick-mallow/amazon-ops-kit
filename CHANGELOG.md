# Changelog

## 0.8.1 — 2026-10-16

- Recommended AI tools: Claude (main), Codex, Cursor and Grok. The tracker's `README.md` gives
  step-by-step connection for each; ChatGPT, Gemini CLI, Copilot and Claude Code move to
  "Other tools (advanced)".
- `AGENTS.md` gains section 0, "First conversation": any AI tool sets up a new tracker by asking
  the one data-source question, so Codex, Cursor and Grok users don't need Claude to start.
- Tools working on a local clone (Codex, Cursor) pull before and push right after each entry.
- Public template repo `karthick-mallow/amazon-ops-tracker-template` for "Use this template".

## 0.8.0 — 2026-10-16

- Works with any data source: KwickMetrics (still the built-in default connector), any other
  connector, or reports the seller downloads and uploads. When nothing is connected, the AI asks
  for the specific report and labels every figure with its source.
- `/setup` asks one question — where the seller's data comes from — and records the answer in a
  new **Data sources** table in `config.md`. KwickMetrics is no longer required; only GitHub is.
- Automatic logging covers changes made through any connected tool, not only KwickMetrics.
- Follow-up reviews re-check the same source; for reports they ask for the same report covering
  the newer dates, and say "no data yet" rather than guess.
- Impact dashboard can be built from uploaded daily reports.
- `tracker.csv`: `KwickMetrics focus` renamed `Focus`; new `Data source` column after it. Pages
  gain a `Data Source` header line. Older trackers are brought up to date with `Not recorded` in
  the new column ("Update my AGENTS.md").

## 0.7.0 — 2026-10-13

- Changes made through KwickMetrics are logged automatically; analysis, diagnosis, plans and
  changes made outside KwickMetrics are logged only after the seller approves.
- Before suggesting anything, the AI always checks the last 90 days of related activity and says
  what it found.
- New `AI tool` and `AI model` columns in `tracker.csv` (after `Date (UTC)`) and matching page
  fields; older trackers get the columns added with `Not recorded`.

## 0.6.1 — 2026-10-13

- Correct KwickMetrics MCP address: `https://mcp.api.kwickmetrics.com/mcp/kwickmetrics`.

## 0.6.0 — 2026-10-13

- No plugin settings. The Claude app doesn't show plugin settings boxes, so the tracker is found by
  name: `<GitHub username>/amazon-ops-tracker` (via the GitHub connector's `get_me`).
- GitHub connector no longer expects a token from settings; sellers add it as an `Authorization`
  request header when connecting github on the plugin's Connectors tab.
- Setup can fetch the tracker template from the public kit repo if the plugin folder can't be read.

## 0.5.0 — 2026-10-13

- Refocused on one job: shared activity memory across AI tools. The plugin reads the seller's
  history at the start of a conversation and logs each working session automatically.
- Removed the target review and change-approval skills, the operating rules, and the pause
  threshold. New `load-context` skill.
- `/setup` asks no questions: it reads accounts from KwickMetrics and creates the tracker.
- Goals (monthly target, target ACoS…) are saved only when the seller states them in chat.
- New plugin and marketplace descriptions.

## 0.4.0 — 2026-10-13

- Plugin settings cut to two required boxes: Tracker GitHub repository and GitHub token.
  Business settings (brands, marketplace, currency, target, pause threshold) are asked by
  `/setup` and kept in `config.md` in the tracker repo, so every AI tool reads the same values.

## 0.3.0 — 2026-10-12

- Tracker repo becomes shared memory for any AI tool: `AGENTS.md` rulebook, `STATE.md` current
  position, `LESSONS.md`, plus `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`
  pointers and a `PROMPT.md` starter prompt for ChatGPT, Grok and other chat apps.
- Tracker README explains how to connect Claude, Codex, Gemini CLI, Cursor, Copilot, ChatGPT and
  Grok to the repo and to KwickMetrics.
- Pages and commits record the AI client and model; logging refreshes `STATE.md` and appends
  lessons.
- Setup copies the full template, never overwrites existing history, and can rebuild `STATE.md`
  when importing an old tracker.

## 0.2.0 — 2026-10-12

- The Activity Tracker now lives only in GitHub; the Claude Docs option is removed.
- Setting "Tracker GitHub repository" replaces the store and location settings.
- Setup can import an existing tracker (Claude Docs, Notion or spreadsheet) into GitHub.

## 0.1.0 — 2026-10-12

- First release: operating rules, target review, propose change, log activity, review follow-ups,
  impact dashboard and setup skills; KwickMetrics and GitHub connectors; GitHub or Claude Docs
  tracker store.
