# Amazon Ops Copilot

Shared memory and follow-through for Amazon sellers who use AI. Every change you make through a
connected tool, and any analysis or decision you choose to keep, is saved to your own private
GitHub repo, with the AI tool, model and data source behind it. Claude, Codex, Grok and Cursor read
that repo first, so whichever one you open already knows what you've done, and
you never have to explain it again.

**Works with any data source:** KwickMetrics (built in as the default connector), any other MCP
connector you add (another seller tool, Amazon Ads…), or reports you download from Seller Central
or the Ads console and upload in the chat.

## What it does

| Skill | When it runs | What it does |
|---|---|---|
| Load context | Automatically, when you talk about your business | Reads your tracker first, and always checks the last 90 days of related activity before suggesting anything |
| Log activity | Automatically right after any change made through a connected tool; for anything else, after you say yes | Saves the activity to your GitHub tracker with the AI tool, model and data source, and tells you the ID |
| Review follow-ups | `/review-followups` | Checks whether earlier changes worked, with fresh numbers from the same source (or an updated report) |
| Impact dashboard | `/impact-dashboard` | Charts your sales and ad spend with every logged activity marked on it |
| Setup | `/setup` | Creates the tracker in your GitHub repo. Asks one question: where your data comes from |

Goals are yours to set, by just saying them, e.g. "My target this month is ₹8,00,000" or "Keep
ACoS under 30%". Claude saves them in the tracker and every AI tool sees them.

Connectors: **GitHub** (`https://api.githubcopilot.com/mcp/`, required) and **KwickMetrics**
(`https://mcp.api.kwickmetrics.com/mcp/kwickmetrics`, optional default data source).

## Setup

1. Create a private GitHub repo named exactly `amazon-ops-tracker`, and a fine-grained GitHub token
   with **Contents: Read and write** on that repo only.
2. In Claude, **Customize → Plugins → + Add → Add marketplace**, enter
   `karthick-mallow/amazon-ops-kit`, then add **Amazon Ops Copilot**.
3. Open the plugin's **Connectors** tab:
   - **github → Connect → Continue**. Under **Authentication** choose **No sign-in**. Under
     **Request headers** add `Authorization` = `Bearer <your token>`. Click **Add**.
   - **If you use KwickMetrics:** **KwickMetrics → Connect**, and sign in. Using another tool?
     Add it under Customize → Connectors. Using reports? Nothing to connect.
4. In a Cowork task, run `/setup` and answer its one question.

Claude Code: `/plugin install amazon-ops-copilot --marketplace karthick-mallow/amazon-ops-kit`

The plugin has no settings. It finds your tracker at `<your GitHub username>/amazon-ops-tracker`.

## Your tracker repo

`AGENTS.md` (instructions every AI tool follows) · `config.md` (accounts, data sources and goals) ·
`STATE.md` (where things stand) · `LESSONS.md` · `tracker.csv` (every activity) · `activities/`
(one page per activity). Its `README.md` explains how to connect other AI tools to the same memory.
