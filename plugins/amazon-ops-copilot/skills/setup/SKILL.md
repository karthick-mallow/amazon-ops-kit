---
name: setup
description: >
  This skill should be used when the user says "set up Amazon Ops Copilot", "configure the plugin",
  "create my activity tracker", "connect KwickMetrics", "change my monthly target", "add a brand",
  "import my tracker into GitHub", "use the tracker with ChatGPT / Codex / Gemini / Grok", "connect
  another AI tool", or invokes /setup, and whenever another Amazon Ops Copilot skill finds the
  seller's settings or tracker missing. It confirms the connectors, discovers the seller's
  accounts, records settings and creates the shared GitHub tracker repo every AI tool can use.
metadata:
  version: "0.3.0"
---

# Setup

Keep the conversation plain and short. Ask with multiple-choice questions where possible.

## 1. Check the connectors

- **KwickMetrics:** call `get_accounts`. If it fails, tell the user to connect or sign in to
  KwickMetrics (with their Amazon Seller and Ads accounts linked in KwickMetrics), then retry.
- **GitHub** (required — the tracker lives only there): open the configured tracker repo, or list
  the user's repos if none is set. If it fails, the token is missing or lacks access — ask for a
  fine-grained token with Contents read/write on the tracker repo only, entered in the plugin's
  settings, never pasted in chat. Do not continue to step 4 without working GitHub access.

## 2. Discover and confirm scope

From `get_accounts`, list each account with slug, marketplace and whether ads are integrated. Ask:
- which accounts count toward the monthly target (default: all with ads integrated);
- which marketplace to use (default: the one the accounts share);
- the monthly gross-revenue target for the current month, and whether it is measured before or
  after returns (default: before);
- the high-spend pause threshold (default 500 per day).

## 3. Record the settings

Fill `config.md` from `${CLAUDE_PLUGIN_ROOT}/skills/setup/tracker-template/config.md` with the
confirmed values (replace every `{{...}}`). When the target changes for a new month, update the target and Updated lines.

## 4. Create the shared tracker repo

The tracker repo is the seller's memory for **every** AI tool, not only Claude. Use the repo in
the plugin settings, or offer to create a **private** repo named `amazon-ops-tracker`.

Copy every file from `${CLAUDE_PLUGIN_ROOT}/skills/setup/tracker-template/`:

| File | Action |
|---|---|
| `AGENTS.md` | Rulebook every AI client follows — copy as is |
| `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` | Pointers to AGENTS.md — copy as is |
| `PROMPT.md` | Starter prompt for chat apps — replace `OWNER/REPO` with the repo |
| `README.md` | How to connect each AI tool — copy as is |
| `config.md` | Filled in step 3 |
| `STATE.md` | Fill `{{UPDATED_UTC}}` with now, `{{ACT_ID}}` with `setup`, `{{AI_CLIENT}}` with `Claude / <model>` |
| `LESSONS.md`, `TEMPLATE.md`, `tracker.csv`, `activities/.gitkeep` | Copy as is |

**Existing repo:** add only the files that are missing. Never overwrite `tracker.csv`, pages,
`STATE.md` or `LESSONS.md`. If `AGENTS.md` exists and differs, show the differences and ask
before replacing it.

Commit as `Initialise Amazon Activity Tracker`, and confirm it matches the plugin's "Tracker GitHub repository" setting.

**Moving an existing tracker** (from Claude Docs, Notion or a spreadsheet): if the user asks,
read every existing row and page and write them to `tracker.csv` and `activities/ACT-NNN.md`
exactly as they are — same IDs, dates and figures — in one commit
`Import existing Activity Tracker (ACT-001 to ACT-NNN)`. Then rebuild `STATE.md` from the rows
that are still open (follow-ups, Monitoring changes), offer to draft `LESSONS.md` entries from
lessons recorded on the pages, show a count of rows and pages imported against the source, and
leave the old tracker untouched as a read-only archive.

## 5. Connect other AI tools (optional)

If the user wants to use the same memory from other AI tools, walk through the "Connect an AI
tool" table in the repo's `README.md` for the tools they name: each needs access to this repo and
to KwickMetrics. For chat apps that do not read repo files on their own (e.g. ChatGPT, Grok), give
them the filled-in `PROMPT.md` to paste into the app's custom or project instructions. Recommend a
separate fine-grained GitHub token per tool, limited to this repo.

## 6. Confirm it works

Run one short check: month-to-date gross revenue per in-scope brand via `get_sales_overview`, with
the date range and snapshot time. Offer to log it as the next Activity ID (Analysis) to prove the
round-trip, and point the user to `/target-review` and `/impact-dashboard`.
