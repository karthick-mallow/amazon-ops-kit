# Amazon Ops Copilot

Run an Amazon seller business with Claude and live KwickMetrics data: monthly target reviews,
safe PPC and listing changes with approval, an Activity Tracker kept in GitHub, and an impact
dashboard that shows what each change did.

## What's inside

| Skill | Invoke | What it does |
|---|---|---|
| Operating rules | automatic | Live-data-only rules, per-brand reporting, metric definitions, response format |
| Target review | `/target-review` | Month-to-date revenue per brand, run rates, floor forecast, ranked risks |
| Propose change | `/propose-change` | Turns a change request into an approval table with limits, executes only what you approve, verifies and logs it |
| Log activity | `/log-activity` | Writes the session to the tracker in the fixed eight-section format |
| Review follow-ups | `/review-followups` | Measures due activities against their success criteria and logs a Review |
| Impact dashboard | `/impact-dashboard` | Charts daily sales, spend, ACoS and TACoS with every tracker activity marked |
| Setup | `/setup` | Connects KwickMetrics and GitHub, records your brands and target, creates the tracker |

Connectors (in `.mcp.json`): **KwickMetrics** (`https://mcp.api.kwickmetrics.com`, sign in with
your KwickMetrics account) and **GitHub** (`https://api.githubcopilot.com/mcp/`, uses the GitHub
token you enter in the plugin settings).

## One memory for every AI tool

The tracker is a private GitHub repo with an `AGENTS.md` rulebook, a `STATE.md` summary of where
things stand, `LESSONS.md`, `tracker.csv` and one page per activity. Codex, Cursor and Copilot
read `AGENTS.md` on their own; Claude Code and Gemini CLI are pointed to it by `CLAUDE.md` and
`GEMINI.md`; chat apps such as ChatGPT and Grok get a starter prompt (`PROMPT.md`). Every tool
logs the same way and records which AI client did the work. See the tracker repo's `README.md`
for how to connect each tool.

## Setup

1. Install the plugin — in the desktop app, open the `.plugin` file; in Claude Code:
   `/plugin install amazon-ops-copilot --marketplace karthick-mallow/amazon-ops-kit`.
2. Fill in the two plugin settings: **Tracker GitHub repository** (`username/amazon-ops-tracker`)
   and **GitHub token**. Everything else — brands, marketplace, currency, target, pause
   threshold — is asked by `/setup` and saved in `config.md` in the tracker repo.
3. Sign in to KwickMetrics when prompted.
4. Run `/setup`. It checks both connectors, confirms your scope and target, and creates the tracker
   repo (`AGENTS.md`, `config.md`, `STATE.md`, `LESSONS.md`, `tracker.csv`, `activities/`).

The GitHub token should be a fine-grained personal access token limited to the tracker repository
with **Contents: read and write**. It is stored in your system's secure credential store, not in
the plugin files.

## Safety built in

- No KwickMetrics write happens without your explicit approval of a specific table of changes.
- One proposal never includes a bid change above ±30%, a budget change above ±25%, more than 10
  entities, or a listing publish without preview; high-spend pauses get their own confirmation.
- Every executed change is verified with a read and logged immediately.

## Monthly housekeeping

At the start of each month, run `/setup` and choose "change my monthly target", or update the
target in the plugin settings.
