# Amazon Ops Kit

Shared memory and follow-through for Amazon sellers who use AI tools. Everything a seller does —
analyses, decisions, changes — is logged to their own private GitHub repo, which every AI tool
reads first. Whichever tool they open already knows what was done, so they never have to explain
it again.

**Recommended AI tools:** **Claude** (main tool, with this plugin) · **Codex** (second opinion,
deeper analysis) · **Cursor** (report files, bulk edits) · **Grok** (quick checks on the phone).
Others that read `AGENTS.md` work too, but aren't part of the recommended set.

It works with **any data source**: KwickMetrics (built in as the default connector), any other MCP
connector, or reports downloaded from Seller Central or the Ads console and uploaded in the chat.

Two parts:

1. **The tracker repo template** — `plugins/amazon-ops-copilot/skills/setup/tracker-template/`.
   A private GitHub repo built from it holds the instructions every AI tool follows (`AGENTS.md`),
   the seller's accounts, data sources and goals (`config.md`), where things stand (`STATE.md`),
   lessons learned, and every activity.
2. **The Amazon Ops Copilot plugin for Claude** — reads that history at the start of a
   conversation, checks the last 90 days before suggesting anything, logs changes automatically
   (other work with approval), reviews follow-ups, draws an impact dashboard, and sets the repo up
   with one question: where the seller's data comes from.

## Start with Claude

**Claude desktop app / Cowork:** add this repository as a plugin marketplace (Customize → Plugins →
Add marketplace → `karthick-mallow/amazon-ops-kit`) and add **Amazon Ops Copilot**.

**Claude Code:**

```bash
claude plugin marketplace add karthick-mallow/amazon-ops-kit
claude plugin install amazon-ops-copilot@amazon-ops-kit
```

Then run `/setup`. It creates your private tracker repo from the template.

## Start with Codex, Cursor or Grok

1. Open [karthick-mallow/amazon-ops-tracker-template](https://github.com/karthick-mallow/amazon-ops-tracker-template),
   click **Use this template → Create a new repository**, name it `amazon-ops-tracker` and choose
   **Private**. (Or copy everything in `plugins/amazon-ops-copilot/skills/setup/tracker-template/`
   into a new private repo, including `.github/`.)
2. Connect your tool to the repo — and to your data connector, if you use one — following the
   steps for that tool in the new repo's `README.md`.
3. Start a conversation. On a new tracker the AI asks one question — where your data comes from —
   and sets everything up (`AGENTS.md`, section 0). Adding Claude later is fine: `/setup` keeps
   what is there.

## How the shared memory works

```
          any AI tool ──reads──▶ AGENTS.md  (rules)
                       ──reads──▶ config.md · STATE.md · LESSONS.md · tracker.csv
                       ──pulls──▶ your data source (a connector, or reports you upload)
                       ──writes─▶ activities/ACT-NNN.md + tracker.csv + STATE.md  (one commit)
```

Every page and commit records which AI tool and model did the work and where the numbers came
from, so a session in Codex on Monday and one in Claude on Tuesday continue the same thread.

## Repository layout

```
.claude-plugin/marketplace.json                  marketplace catalog
plugins/amazon-ops-copilot/
  .claude-plugin/plugin.json                     manifest
  .mcp.json                                      GitHub (required) + KwickMetrics (default data source)
  skills/                                        five skills
  skills/setup/tracker-template/                 the shared tracker repo template
CHANGELOG.md
```

Your tracker data never lives in this repository.

## Updating

Maintainers bump `version` in `plugin.json` and add a line to `CHANGELOG.md`. Claude Code users
update with `claude plugin update amazon-ops-copilot@amazon-ops-kit`. Changes to `AGENTS.md` in the
template reach existing trackers when a seller says "Update my AGENTS.md".
