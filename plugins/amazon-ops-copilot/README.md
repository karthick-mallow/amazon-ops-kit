# Amazon Ops Copilot

Shared memory for Amazon sellers who use **KwickMetrics**. Every analysis, decision and change you
make with Claude is saved to your own private GitHub repo. Claude, ChatGPT, Grok, Gemini and other
AI tools read that repo first, so whichever one you open already knows what you've done, and you
never have to explain it again.

## What it does

| Skill | When it runs | What it does |
|---|---|---|
| Load context | Automatically, when you talk about your business | Reads your tracker first, so Claude knows what was done before, in any AI tool |
| Log activity | Automatically at the end of a working session, and right after any change | Saves what was done to your GitHub tracker and tells you the ID |
| Review follow-ups | `/review-followups` | Checks whether earlier changes worked, using live KwickMetrics data |
| Impact dashboard | `/impact-dashboard` | Charts your sales and ad spend with every logged activity marked on it |
| Setup | `/setup` | Creates the tracker in your GitHub repo and records your KwickMetrics accounts. Asks no questions. |

Goals are yours to set, by just saying them, e.g. "My target this month is ₹8,00,000" or "Keep
ACoS under 30%". Claude saves them in the tracker and every AI tool sees them.

Connectors: **KwickMetrics** (`https://mcp.api.kwickmetrics.com`) and **GitHub**
(`https://api.githubcopilot.com/mcp/`, using the token you enter in the plugin settings).

## Setup

1. Install: in Claude, **Customize → Plugins → + Add → Add marketplace**, enter
   `karthick-mallow/amazon-ops-kit`, then add **Amazon Ops Copilot**. In Claude Code:
   `/plugin install amazon-ops-copilot --marketplace karthick-mallow/amazon-ops-kit`.
2. Fill in the two settings: **Tracker GitHub repository** (`username/amazon-ops-tracker`) and
   **GitHub token** (fine-grained, **Contents: Read and write** on that repo only).
3. Run `/setup`.

## Your tracker repo

`AGENTS.md` (instructions every AI tool follows) · `config.md` (accounts and goals) · `STATE.md`
(where things stand) · `LESSONS.md` · `tracker.csv` (every activity) · `activities/` (one page per
activity). Its `README.md` explains how to connect other AI tools to the same memory.
