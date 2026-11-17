---
name: setup
description: >
  This skill should be used when the user says "set up Amazon Ops Copilot", "set up my tracker",
  "create my activity tracker", "import my tracker into GitHub", "change my data source", "use the
  tracker with Codex / Grok / Cursor", "connect another AI tool", "update my AGENTS.md", "update my
  tracker", "upgrade my tracker", "migrate my tracker", or invokes /setup, and whenever another
  Amazon Ops Copilot skill finds the tracker missing. It prepares the seller's private GitHub
  tracker repo and asks one question: where their Amazon data comes from; after a plugin update it
  migrates an existing tracker to the latest rules and schema, keeping the seller's own rules.
metadata:
  version: "0.10.1"
---

# Setup

Set up the tracker with **one question only** — the seller's data source. Ask nothing else (no
targets, thresholds or preferences; the seller sets goals later by chatting). Report at the end in
a few lines.

## 1. Check GitHub

Find the tracker repo exactly as `load-context` describes (a repo the seller names, else
`<username>/amazon-ops-tracker`, else one private repo of theirs holding `AGENTS.md` — never a
public repo or the template itself). If GitHub isn't connected, or the
repo can't be opened, stop and tell the seller in plain words: on the plugin's **Connectors** tab,
connect **github** with their key, and make sure their private repo is named `amazon-ops-tracker`
and the key has **Contents: Read and write** on it (optional: **Issues: Read-only** to see tracker
check failures, **Workflows: Read and write** to add the check to an older tracker). Never ask them to paste a key in chat.

## 2. Ask the one question — the data source

Ask once, in plain chat, as a short numbered list (more than one answer is fine):

> Where does your Amazon data come from?
> 1. **KwickMetrics** — connected in this plugin
> 2. **Another connected tool** — tell me its name
> 3. **Reports I download** from Seller Central or the Ads console and upload here

Then, without further questions:

- **KwickMetrics:** call `get_accounts`. If it fails, tell the seller to connect KwickMetrics on
  the plugin's **Connectors** tab and sign in, then run `/setup` again. Fill the accounts from it.
- **Another connected tool:** find that tool among your connectors. If it has a call that lists
  accounts or profiles, use it to fill the accounts; otherwise record the source and leave the
  accounts for the first conversation. If you can't find the tool, say so and suggest adding it
  as a connector (Customize → Connectors) — or using reports for now.
- **Reports:** record `Uploaded reports`. Accounts are filled in later from the first reports the
  seller shares or the brand names they mention.

If the seller doesn't answer (an unattended run), default to KwickMetrics when it is connected,
else `Uploaded reports`, and say which was chosen.

## 3. Create the tracker files

Most sellers create their repo from the template
(`karthick-mallow/amazon-ops-tracker-template` → **Use this template**), so the files are already
there: skip copying and go straight to "Fill in" below. Only if the repo is empty or files are
missing, copy every file from the `tracker-template/` folder that sits next to this skill
(`${CLAUDE_PLUGIN_ROOT}/skills/setup/tracker-template/`; if that path can't be read, fetch the same
folder from the public repo `karthick-mallow/amazon-ops-kit` at
`plugins/amazon-ops-copilot/skills/setup/tracker-template/`) into the tracker repo:
`AGENTS.md`, `README.md`, `PROMPT.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`,
`config.md`, `STATE.md`, `LESSONS.md`, `TEMPLATE.md`, `tracker.csv`, `activities/.gitkeep`,
`.github/workflows/check-tracker.yml`, `.github/scripts/check_tracker.py`. Writing the workflow
file needs the key to have **Workflows: Read and write**; if it's refused, copy the rest and tell
the seller how to add it (or to add the file by hand).

Fill in:
- `config.md` → the **Data sources** table (each source the seller chose, how it's used —
  Connector or Uploaded reports), the **Accounts** table (name, ID or slug, marketplace, source)
  where known, the **Users** table (one Owner row: the seller's name if you know it, else their
  GitHub username — don't ask), and `Updated`. Leave **Goals and preferences** empty.
- `PROMPT.md` → replace `OWNER/REPO` with the tracker repo's full name.
- `STATE.md` → `Last updated: <now UTC> — setup — Claude / <model> — <User> (<Mode>)`.

**If the repo already has a tracker:** add only missing files. Never overwrite `tracker.csv`,
pages, `STATE.md`, `LESSONS.md` or `config.md` goals; only refresh the data sources and accounts
tables.

Commit as `Set up Amazon Activity Tracker`.

## 4. Finish

Tell the seller, in three short lines:
- The tracker is ready in `<username>/amazon-ops-tracker`, with the data source and accounts found.
- Changes made through a connected tool are saved there automatically; for anything else Claude
  asks before saving. Any AI tool connected to the repo picks up from it.
- They can set goals any time by just saying them, e.g. "My target this month is ₹8,00,000".

## Only when the seller asks

- **Change my data source:** ask the same one question, update the **Data sources** and
  **Accounts** tables in `config.md`, commit `Update data sources`.
- **Import an existing tracker** (Claude Docs, Notion, a spreadsheet): copy every row and page
  exactly as it is — same IDs, dates and figures — into `tracker.csv` and `activities/`, in one
  commit `Import existing tracker (ACT-001 to ACT-NNN)`. Fill `Not recorded` in any column the
  source doesn't have (`unknown` for `User` / `Mode`) — never guessed values. Rebuild `STATE.md` from the rows still open. Report the count imported
  against the source; leave the original untouched.
- **Connect another AI tool:** point them to the "Connect an AI tool" section of the repo's
  `README.md` for the tool they name.
- **Update my AGENTS.md / my tracker** (after a plugin update): first **keep the seller's own
  rules** — compare the repo's `AGENTS.md` with the plugin's copy and list every rule, section or
  block the plugin's copy doesn't contain (e.g. a "Standing instruction" block, a rule about a data
  source). Map each into `config.md`: data sources → **Data sources**, rules → **Seller rules**
  (worded for the seller), goals → **Goals and preferences**; mark any the new `AGENTS.md` already
  covers. Do the same for edits the seller made to `TEMPLATE.md` (keep added page sections as a
  Seller rule). Show the seller the list and wait for their OK — don't commit before it. Add the
  **Seller rules** section if missing.
  Then replace the repo's `AGENTS.md`, `README.md`, `PROMPT.md` and `TEMPLATE.md` with the
  plugin's latest copies, keeping everything else. Then
  migrate the tracker to the current schema exactly as the new `AGENTS.md` section 7 describes
  (schema from `Tracker schema` in `config.md`, or from the header if that line is missing), add the
  check files if missing, and set `Tracker schema: 4`. If `config.md` has a `KwickMetrics accounts`
  section, turn it into the **Data sources** (KwickMetrics, Connector) and **Accounts** tables,
  keeping the goals. One commit, `Update to Amazon Ops Copilot <version> [Claude / <model> ·
  <User> · <Mode>]`. Say what changed, including where each moved rule now lives.
