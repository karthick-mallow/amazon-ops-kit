# Changelog

## 0.10.0 — 2026-11-17

Kit and template ship this version together. No `tracker.csv` column changes (schema stays 4).

### Added
- **Schema version:** `config.md` gains `Tracker schema: 4`. AI tools read it before every write
  and migrate step by step from it (`AGENTS.md` section 7, with the schema 1–4 history); the
  header is only inspected when the line is missing. A tracker newer than the AI's instructions
  is never written to.
- **Tracker check:** a GitHub Action (`.github/workflows/check-tracker.yml`, standard-library
  Python in `.github/scripts/check_tracker.py`) runs on every push touching `tracker.csv`,
  `config.md` or `activities/`. It checks the header, column count, blank cells, ID / date /
  follow-up formats, allowed Type / Mode / Status / Focus values, and that each Page exists. On
  failure it opens one issue labelled `tracker-check`; the next pass closes it. Rows from before
  User/Mode (`User = unknown`) get warnings, not errors, for old values.
- AI tools look for an open `tracker-check` issue at the start of a conversation and, with the
  seller's OK, fix only what it lists — never figures.
- `KwickMetrics focus` → `Focus` (0.8.0) is recorded as the one legacy rename; columns are
  otherwise only added.

### Migration — existing seller trackers
1. Optional: add **Issues: Read-only** to each tool's GitHub key so the AI sees check failures,
   and **Workflows: Read and write** to the key Claude uses, so it can add the check.
2. Tell Claude "update my AGENTS.md". In one commit it updates the instructions, migrates the
   tracker to schema 4 if needed, adds `Tracker schema: 4` to `config.md`, and adds the two check
   files. Without the Workflows permission it adds everything else and tells you; you can then
   copy `.github/workflows/check-tracker.yml` from the template repo by hand.
3. The first push runs the check. If it opens a `tracker-check` issue, say "fix the tracker check
   issue".
Grok users: re-paste `PROMPT.md`.

## 0.9.0 — 2026-11-17

Kit (amazon-ops-kit, Amazon Ops Copilot plugin) and template (amazon-ops-tracker-template) ship
this version together.

### Added
- **`User` and `Mode` columns** in `tracker.csv`, after `AI model`. User = who asked for or approved
  the work; Mode = `Chat`, `Voice` or `Schedule`. Never blank on new rows.
- **Users** table in `config.md` (first row = owner, used when the AI can't tell who is asking).
- `Mode` line in the activity page header; `Executed By` now holds the same name as `User`.
- Scheduled runs: changes through a connected tool are logged automatically; anything else only
  when the scheduled task's instructions say so (`Logged: By the scheduled task's instructions`).
- Commit messages and `STATE.md`'s "Last updated" line include user and mode.
- load-context, review-followups and impact-dashboard read or show User / Mode.

### Migration — existing seller trackers
Nothing to do by hand. On the next logged activity (or when you tell Claude "update my
AGENTS.md"), the AI will, in one commit:
1. add `User` and `Mode` after `AI model` in `tracker.csv`, filling `unknown` for every older row
   (no guessed values);
2. add a **Users** section to `config.md` above **Goals and preferences**, with the owner's row;
3. (with "update my AGENTS.md") replace `AGENTS.md`, `README.md`, `PROMPT.md` and `TEMPLATE.md`
   with the 0.9.0 copies.
Chat apps using `PROMPT.md` (e.g. Grok): re-paste the updated prompt into their custom
instructions.

## 0.8.3 — 2026-10-16

- Safer tracker lookup: a repo the seller names wins; then `<username>/amazon-ops-tracker`; then
  one private repo holding `AGENTS.md` and `tracker.csv`. Public repos and the template repo are
  never used as a tracker; if several candidates exist, Claude asks once which one.

## 0.8.2 — 2026-10-16

- One setup path for every tool: create the tracker from the template repo (**Use this
  template**), connect your AI tool, type "Set up my tracker". Any tool finishes setup on a fresh
  tracker; Claude also does it when a conversation about the business starts on one. `/setup`
  still works, and still copies files into an empty repo.

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
