---
name: log-activity
description: >
  This skill should be used immediately after any KwickMetrics write action (a bid, budget,
  campaign, keyword, target, negative, day-parting, rule, portfolio or listing change), which it
  logs automatically, and at the end of any conversation with other work worth keeping (analysis,
  diagnosis, a plan, or a change made outside KwickMetrics), which it logs only after the seller
  approves. Also when the user says "log this", "save this", or invokes /log-activity.
metadata:
  version: "0.7.0"
---

# Log Activity

Write what happened to the seller's tracker repo — `<GitHub username>/amazon-ops-tracker`, found
as in `load-context` — through the GitHub connector (`push_files` writes all files in one commit), following the repo's `AGENTS.md` (the protocol every AI tool uses). Never store
the log anywhere else.

## 1. When — automatic or with approval

| What happened | Log it |
|---|---|
| A **change made through KwickMetrics** — any KwickMetrics tool that creates, updates, pauses, deletes, negates, applies, links or publishes something | **Automatically and immediately**, right after the change, without asking. One activity per change request (several entities changed together = one activity). |
| **Anything else** worth keeping — analysis, diagnosis, brainstorming, a plan, a follow-up review, or a change the seller made **outside KwickMetrics** (e.g. in Seller Central) | **Only with approval.** At the end of the conversation, ask once in one line: *"Shall I save this to your tracker as an Analysis?"* (name the type). Log only if the seller says yes. |
| Small talk, general how-to questions, nothing decided | Don't log, don't ask. |

- If the seller says "log this", that is approval. If they say "don't log this", don't — not even
  an automatic change log for that request.
- After saving, tell the seller in one line: `Saved to your tracker as ACT-NNN.`
- Record which way it was logged on the page (`Logged: Automatically (KwickMetrics change)` or
  `Logged: With the seller's approval`).

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

- Header: the seller's name if known, **AI Tool = `Claude`** and **AI Model = your exact model
  name** (e.g. `Claude Opus 5.5`). Never leave them blank.
- Record what was actually seen and done: KwickMetrics tools called, date range, snapshot time
  (UTC), the numbers that mattered, decisions, and for a Change the exact before → after values.
- Follow-up: a date to check the result (default +7 days) and what "worked" would look like.

## 5. The tracker row

Insert directly under the header row of `tracker.csv`, columns per
`references/tracker-columns.md` — including **AI tool** (`Claude`) and **AI model** (your exact model
name). No column is left blank (`All` where it covers everything).

If the repo's `tracker.csv` header has no `AI tool` / `AI model` columns yet (older tracker), add
them after `Date (UTC)` and fill `Not recorded` for the older rows, in the same commit.

## 6. STATE.md and LESSONS.md

- `STATE.md`: update only the parts this activity changes — open follow-ups, changes being
  watched, next steps. Set `Last updated: <YYYY-MM-DD HH:MM UTC> — ACT-NNN — Claude / <model name>`.
- `LESSONS.md`: append a lesson only if this activity taught something that should change future
  work: `## YYYY-MM-DD — <title> (ACT-NNN)`.

## 7. Commit

One commit with the page, `tracker.csv` and `STATE.md` (plus `LESSONS.md` if changed):
`ACT-NNN: <Type> — <short title> [Claude / <model name>]`. If the write is rejected because a file changed,
re-read, take the next free ID, and retry. Never overwrite another tool's entries.

If GitHub cannot be reached, give the seller the page and CSV row as ready-to-save text and say
plainly that nothing was saved yet.
