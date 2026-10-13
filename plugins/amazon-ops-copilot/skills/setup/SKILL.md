---
name: setup
description: >
  This skill should be used when the user says "set up Amazon Ops Copilot", "set up my tracker",
  "create my activity tracker", "import my tracker into GitHub", "use the tracker with ChatGPT /
  Codex / Gemini / Grok", "connect another AI tool", or invokes /setup, and whenever another
  Amazon Ops Copilot skill finds the tracker missing. It prepares the seller's private GitHub
  tracker repo without asking any questions.
metadata:
  version: "0.6.0"
---

# Setup

Do the whole setup without asking the seller anything. Report at the end in a few lines.

## 1. Check the two connections

- **GitHub:** call `get_me` to get the seller's username, then open
  `<username>/amazon-ops-tracker` (or another repo the connector can access that already holds
  `AGENTS.md`). If GitHub isn't connected, or the repo can't be opened, stop and tell the seller in
  plain words: on the plugin's **Connectors** tab, connect **github** with their key, and make sure
  their private repo is named `amazon-ops-tracker` and the key has **Contents: Read and write** on
  it. Never ask them to paste a key in chat.
- **KwickMetrics:** call `get_accounts`. If it fails, tell the seller to connect KwickMetrics in
  the plugin's **Connectors** tab and sign in, then run `/setup` again.

## 2. Create the tracker files

Copy every file from the `tracker-template/` folder that sits next to this skill
(`${CLAUDE_PLUGIN_ROOT}/skills/setup/tracker-template/`; if that path can't be read, fetch the same
folder from the public repo `karthick-mallow/amazon-ops-kit` at
`plugins/amazon-ops-copilot/skills/setup/tracker-template/`) into the tracker repo:
`AGENTS.md`, `README.md`, `PROMPT.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`,
`config.md`, `STATE.md`, `LESSONS.md`, `TEMPLATE.md`, `tracker.csv`, `activities/.gitkeep`.

Fill in, without asking:
- `config.md` → the **KwickMetrics accounts** table from `get_accounts` (name, slug, marketplace,
  ads connected yes/no) and `Updated`. Leave **Goals and preferences** empty; the seller sets
  goals later by chatting.
- `PROMPT.md` → replace `OWNER/REPO` with the tracker repo's full name.
- `STATE.md` → `Last updated: <now UTC> — setup — Claude / <model>`.

**If the repo already has a tracker:** add only missing files. Never overwrite `tracker.csv`,
pages, `STATE.md`, `LESSONS.md` or `config.md` goals; only refresh the accounts table.

Commit as `Set up Amazon Activity Tracker`.

## 3. Finish

Tell the seller, in three short lines:
- The tracker is ready in `<username>/amazon-ops-tracker`, with the KwickMetrics accounts it found.
- From now on every conversation about their business is saved there automatically, and any AI
  tool connected to the repo picks up from it.
- They can set goals any time by just saying them, e.g. "My target this month is ₹8,00,000".

## Only when the seller asks

- **Import an existing tracker** (Claude Docs, Notion, a spreadsheet): copy every row and page
  exactly as it is — same IDs, dates and figures — into `tracker.csv` and `activities/`, in one
  commit `Import existing tracker (ACT-001 to ACT-NNN)`. Rebuild `STATE.md` from the rows still
  open. Report the count imported against the source; leave the original untouched.
- **Connect another AI tool:** point them to the "Connect an AI tool" section of the repo's
  `README.md` for the tool they name.
- **Update my AGENTS.md** (after a plugin update): replace the repo's `AGENTS.md`, `README.md` and
  `TEMPLATE.md` with the plugin's latest copies, keeping everything else, and say what changed.
