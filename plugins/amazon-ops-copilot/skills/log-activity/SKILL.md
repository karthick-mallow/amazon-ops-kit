---
name: log-activity
description: >
  This skill should be used at the end of any conversation in which the seller worked on their
  Amazon business with KwickMetrics — an analysis, a diagnosis, a decision, a plan, or a change to
  campaigns, bids, budgets, listings or settings — and immediately after any live change is made.
  Also when the user says "log this", "save this", "add it to the tracker", or invokes
  /log-activity. It writes the activity to the seller's GitHub tracker so every AI tool can see it.
metadata:
  version: "0.5.0"
---

# Log Activity

Write what happened to the seller's tracker repo **${user_config.tracker_repo}** through the
GitHub connector, following the repo's `AGENTS.md` (the protocol every AI tool uses). Never store
the log anywhere else.

## 1. When

- **Automatically**, without asking, at the end of any conversation where real work on the
  business happened: data was pulled and discussed, a problem was diagnosed, a decision or plan was
  made, or something was changed. Skip pure chit-chat and general how-to questions.
- **Immediately** after any live change in KwickMetrics or Amazon (bid, budget, status, negative,
  listing, day-parting…), before moving on.
- If the seller says "don't log this", don't.

After saving, tell the seller in one line: `Saved to your tracker as ACT-NNN.`

## 2. Activity ID

Re-read `tracker.csv` from the default branch right now — another AI tool may have logged since.
Next ID = highest `ACT-NNN` + 1, three digits. Never reuse an ID or take it from memory.

## 3. Type — pick one

Brainstorming (ideas, plans) · Analysis (reports, reviews, trends) · Diagnosis (finding a cause) ·
Change (something was changed in the account) · Review (checking the result of earlier work).

## 4. The page

Write `activities/ACT-NNN.md` from the repo's `TEMPLATE.md` (fallback:
`${CLAUDE_PLUGIN_ROOT}/skills/setup/tracker-template/TEMPLATE.md`): all eight sections, same order
and headings; a section with nothing to say reads `Not applicable — <reason>`.

- Header: the seller's name if known, and **AI Client / Model = `Claude / <model>`**.
- Record what was actually seen and done: KwickMetrics tools called, date range, snapshot time
  (UTC), the numbers that mattered, decisions, and for a Change the exact before → after values.
- Follow-up: a date to check the result (default +7 days) and what "worked" would look like.

## 5. The tracker row

Insert directly under the header row of `tracker.csv`, columns per
`references/tracker-columns.md`. No column is left blank (`All` where it covers everything).

## 6. STATE.md and LESSONS.md

- `STATE.md`: update only the parts this activity changes — open follow-ups, changes being
  watched, next steps. Set `Last updated: <YYYY-MM-DD HH:MM UTC> — ACT-NNN — Claude / <model>`.
- `LESSONS.md`: append a lesson only if this activity taught something that should change future
  work: `## YYYY-MM-DD — <title> (ACT-NNN)`.

## 7. Commit

One commit with the page, `tracker.csv` and `STATE.md` (plus `LESSONS.md` if changed):
`ACT-NNN: <Type> — <short title> [Claude]`. If the write is rejected because a file changed,
re-read, take the next free ID, and retry. Never overwrite another tool's entries.

If GitHub cannot be reached, give the seller the page and CSV row as ready-to-save text and say
plainly that nothing was saved yet.
