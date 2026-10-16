---
name: load-context
description: >
  This skill should be used at the start of any conversation about the seller's Amazon business —
  whether the data comes from KwickMetrics, another connected tool or uploaded reports — and always
  before suggesting or recommending anything — sales, ads, PPC, inventory, listings, pricing,
  profit, ratings — and whenever the user asks "what did we do last time", "what's pending",
  "remind me what we changed", "catch me up", or sets a goal such as "my target this month is …"
  or "keep ACoS under 30%". It loads what the seller has already done from their GitHub tracker so
  they never have to explain it again.
metadata:
  version: "0.8.3"
---

# Load Context

The seller's history lives in their private GitHub tracker repo (see below). It is shared by every
AI tool they use (Claude, Codex, Grok, Cursor…), so it may contain work done in other
tools since this conversation began. Read it through the GitHub connector.

## Finding the tracker repo

Pick the tracker in this order:

1. A repo the seller names in the conversation (e.g. "use karthick/amazon-ops-tracker-test").
2. **`<GitHub username>/amazon-ops-tracker`** — get the username with the GitHub connector's
   `get_me`.
3. Otherwise, a **private** repo the seller owns that contains `AGENTS.md` and `tracker.csv`.
   Never use a public repo, and never the template itself (`amazon-ops-tracker-template`) — it is
   the blank starting copy, not anyone's tracker.

If step 3 finds more than one, list them and ask the seller once which is their tracker; suggest
renaming it to `amazon-ops-tracker` so it is found automatically next time.

## 1. At the start — read before answering

1. `config.md` — the seller's accounts, data sources and any goals they have set.
2. `STATE.md` — where things stand: open follow-ups, changes being watched, next steps.
3. `LESSONS.md` — what earlier work taught.
4. `tracker.csv` — the activity list, newest first.

If `config.md` is missing, or still has `{{` placeholders (a fresh copy of the template), the
tracker is not set up yet: run the `setup` skill first — it asks the seller one question and fills
everything in. The seller doesn't need to type `/setup`. If GitHub cannot
be reached, say so in one line, make no suggestions that depend on past work, and carry on.

## 2. Before suggesting anything — check the last 90 days

Every time, before you recommend, propose or suggest any action (a bid, budget, keyword, listing,
pricing or inventory move, or a plan), check the tracker first:

1. Filter `tracker.csv` to the **last 90 days**, and to rows about the same account, ASIN/SKU,
   campaign or area (focus) as the suggestion.
2. Open those pages in `activities/` and note what was done, by which AI tool, and the result.
3. In your answer, say in one or two lines what you found, e.g. *"ACT-012 (14 Sep, Grok) already
   cut bids on these keywords; ACoS fell from 48% to 35%."* If nothing related exists, say
   *"No related activity in the last 90 days."*
4. Don't repeat a suggestion that was already tried unless current data justifies it — then say
   what has changed since. Respect follow-ups still waiting for their review date.

Never skip this check, even for a quick suggestion.

## 3. Current numbers — from the data source

Numbers in the tracker are what was true when they were logged. For any current figure:

1. Use the source listed in `config.md` → **Data sources** if it is connected (KwickMetrics or any
   other connector).
2. Otherwise ask the seller for the specific report — name it and the date range, e.g. "the
   Sponsored Products search term report for the last 30 days from the Ads console" — and work
   from the uploaded file.
3. Label each figure with its source (tool, or report file and date range). When comparing with
   an earlier activity, show both and label which is which.
4. Never guess a figure you couldn't get; say what's missing.

## 4. Goals and preferences — saved only when the seller says so

The plugin never asks for targets. When the seller states one in conversation (a monthly revenue
target, a target ACoS, a budget limit, a brand to focus on, how they like reports), save it:

- Add or update a line under **Goals and preferences** in `config.md`:
  `- <goal> — set <YYYY-MM-DD> (<AI tool>)`. Replace an older line for the same goal; keep the rest.
- Confirm in one sentence: "Saved: monthly target ₹8,00,000 for November."

Use saved goals when they are relevant (e.g. compare month-to-date sales with a saved target), and
never invent one.

## 5. Logging

Follow `log-activity`: changes made through a connected tool are logged automatically right after
they happen; anything else is logged only if the seller approves when asked at the end.
