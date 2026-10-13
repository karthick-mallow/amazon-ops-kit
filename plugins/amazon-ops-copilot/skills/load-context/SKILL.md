---
name: load-context
description: >
  This skill should be used at the start of any conversation about the seller's Amazon business or
  KwickMetrics — sales, ads, PPC, inventory, listings, profit, ratings — and whenever the user asks
  "what did we do last time", "what's pending", "remind me what we changed", "catch me up", or sets
  a goal such as "my target this month is …" or "keep ACoS under 30%". It loads what the seller has
  already done from their GitHub tracker so they never have to explain it again.
metadata:
  version: "0.5.0"
---

# Load Context

The seller's history lives in their private GitHub repo **${user_config.tracker_repo}**. It is
shared by every AI tool they use (Claude, ChatGPT, Codex, Gemini, Grok…), so it may contain work
done in other tools since this conversation began. Read it through the GitHub connector.

## 1. At the start — read before answering

1. `config.md` — the seller's KwickMetrics accounts and any goals they have set.
2. `STATE.md` — where things stand: open follow-ups, changes being watched, next steps.
3. `LESSONS.md` — what earlier work taught.
4. `tracker.csv` — the activity list, newest first. For the topic at hand, open the related pages
   in `activities/` from the last 90 days (same account, ASIN, campaign or area).

Then answer the seller's question. Mention related earlier work briefly by ID — what was done, by
which AI tool, and what happened — so the seller sees the context was picked up. Do not recite the
whole history.

If `config.md` is missing, the tracker is not set up yet: run the `setup` skill. If GitHub cannot
be reached, say so in one line and carry on without history.

## 2. History is not live data

Numbers in the tracker are what was true when they were logged. For any current figure, pull it
from KwickMetrics now. When comparing with an earlier activity, show both and label which is which.

## 3. Goals and preferences — saved only when the seller says so

The plugin never asks for targets. When the seller states one in conversation (a monthly revenue
target, a target ACoS, a budget limit, a brand to focus on, how they like reports), save it:

- Add or update a line under **Goals and preferences** in `config.md`:
  `- <goal> — set <YYYY-MM-DD> (<AI tool>)`. Replace an older line for the same goal; keep the rest.
- Confirm in one sentence: "Saved: monthly target ₹8,00,000 for November."

Use saved goals when they are relevant (e.g. compare month-to-date sales with a saved target), and
never invent one.

## 4. Before finishing

Record the session with the `log-activity` skill.
