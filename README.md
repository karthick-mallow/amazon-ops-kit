# Amazon Ops Kit

Run an Amazon seller business with AI assistants on live KwickMetrics data, with **one shared
memory in GitHub** that every AI tool reads and writes: Claude, ChatGPT / Codex, Gemini, Grok,
Copilot or Cursor.

Two parts:

1. **The tracker repo template** — `plugins/amazon-ops-copilot/skills/setup/tracker-template/`.
   A private GitHub repo built from it holds the rulebook (`AGENTS.md`), the current position
   (`STATE.md`), lessons learned, and every activity. Any AI tool that can reach GitHub and
   KwickMetrics picks up the same history and follows the same rules.
2. **The Amazon Ops Copilot plugin for Claude** — skills that follow that rulebook: target
   reviews, approval-first changes, logging, follow-up reviews, an impact dashboard and setup.

## Start with Claude

**Claude desktop app / Cowork:** open the `.plugin` file and accept it, or add this repository as
a plugin marketplace in the app's plugin settings and install **amazon-ops-copilot**.

**Claude Code:**

```bash
claude plugin marketplace add karthick-mallow/amazon-ops-kit
claude plugin install amazon-ops-copilot@amazon-ops-kit
```

Then run `/setup`. It creates your private tracker repo from the template.

## Start without Claude

1. Create a new **private** GitHub repo.
2. Copy everything in `plugins/amazon-ops-copilot/skills/setup/tracker-template/` into it,
   including `.github/`.
3. Fill in `config.md` (brands, KwickMetrics account slugs, marketplace, currency, target).
4. Replace `OWNER/REPO` in `PROMPT.md`.
5. Connect your AI tool to the repo and to KwickMetrics using the table in the template's
   `README.md`.

## How the shared memory works

```
          any AI tool ──reads──▶ AGENTS.md  (rules)
                       ──reads──▶ config.md · STATE.md · LESSONS.md · tracker.csv
                       ──pulls──▶ KwickMetrics (live numbers)
                       ──writes─▶ activities/ACT-NNN.md + tracker.csv + STATE.md  (one commit)
```

Every page and commit records which AI client did the work, so a session in Codex on Monday and
one in Claude on Tuesday continue the same thread.

## Repository layout

```
.claude-plugin/marketplace.json                  marketplace catalog
plugins/amazon-ops-copilot/
  .claude-plugin/plugin.json                     manifest and settings
  .mcp.json                                      KwickMetrics + GitHub connectors
  skills/                                        seven skills
  skills/setup/tracker-template/                 the shared tracker repo template
CHANGELOG.md
```

Your tracker data never lives in this repository.

## Updating

Maintainers bump `version` in `plugin.json` and add a line to `CHANGELOG.md`. Claude Code users
update with `claude plugin update amazon-ops-copilot@amazon-ops-kit`. Changes to `AGENTS.md` in the
template reach existing trackers only when a seller copies them in (or runs `/setup`, which shows
the differences and asks first).
