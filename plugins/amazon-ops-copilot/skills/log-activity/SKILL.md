---
name: log-activity
description: >
  This skill should be used immediately after any change made through a connected tool to the
  seller's Amazon account, ads or listings (KwickMetrics or any other connector — a bid, budget,
  campaign, keyword, target, negative, day-parting, rule, portfolio, price or listing change),
  which it logs automatically, and at the end of any conversation with other work worth keeping
  (analysis, diagnosis, a plan, work from uploaded reports, or a change made by hand), which it
  logs only after the seller approves. Also when the user says "log this", "save this", or invokes
  /log-activity.
metadata:
  version: "0.10.2"
---

# Log Activity

Write what happened to the seller's tracker repo — `<GitHub username>/amazon-ops-tracker`, found
as in `load-context` — through the GitHub connector (`push_files` writes all files in one commit),
following the repo's `AGENTS.md` (the protocol every AI tool uses). Never store the log anywhere
else.

## 1. When — automatic or with approval

| What happened | Log it |
|---|---|
| A **change made through a connected tool** — any call to KwickMetrics or another connector that creates, updates, pauses, deletes, negates, applies, links or publishes something in the seller's Amazon account, ads or listings | **Automatically and immediately**, right after the change, without asking. One activity per change request (several entities changed together = one activity). The GitHub writes that save the log don't count. |
| **Anything else** worth keeping — analysis, diagnosis, brainstorming, a plan, a follow-up review, work done from uploaded reports, or a change the seller made **by hand** (e.g. in Seller Central) | **Only with approval.** At the end of the conversation, ask once in one line: *"Shall I save this to your tracker as an Analysis?"* (name the type). Log only if the seller says yes. |
| Small talk, general how-to questions, nothing decided | Don't log, don't ask. |

- If the seller says "log this", that is approval. If they say "don't log this", don't — not even
  an automatic change log for that request.
- After saving, tell the seller in one line: `Saved to your tracker as ACT-NNN.`
- Record which way it was logged on the page (`Logged: Automatically (change via <tool name>)`,
  `Logged: With the seller's approval`, or `Logged: By the scheduled task's instructions`).
- **Scheduled run** (no person in the conversation): log changes made through a connected tool
  automatically; anything else only if the scheduled task's instructions say to log it.

## 1a. User and Mode — on every entry

- **User:** the person who asked for or approved the work, by their name in the repo's
  `config.md` → **Users**. Use the name they give or the name you know them by. If you can't tell
  and you're asking the save question anyway, add "and under which name?". For an automatic log
  where you can't tell, use the owner (first row of **Users**). Schedule mode: whoever set up the
  scheduled task, else the owner. A name not yet listed → add a row to **Users** in the same commit.
- **Mode:** `Chat` (typed in this conversation), `Voice` (the request was spoken — voice mode or
  a dictated request marked as voice) or `Schedule` (this session was started by a scheduled task,
  routine or trigger, not by a person's message). Unsure between Chat and Voice → `Chat`.

## 2. Activity ID

Take the ID **last**: after drafting the page and row, right before the commit, re-read
`tracker.csv` from the default branch — another AI tool may have logged since. Next ID = highest
`ACT-NNN` + 1, three digits. Never reuse an ID or take it from memory or an earlier read.

## 3. Type — pick one

Brainstorming (ideas, plans) · Analysis (reports, reviews, trends) · Diagnosis (finding a cause) ·
Change (something was changed in the account) · Review (checking the result of earlier work).

## 4. The page

Write `activities/ACT-NNN.md` from the repo's `TEMPLATE.md` (fallback:
`${CLAUDE_PLUGIN_ROOT}/skills/setup/tracker-template/TEMPLATE.md`): all eight sections, same order
and headings; a section with nothing to say reads `Not applicable — <reason>`.

- Header: the seller's name if known, **AI Tool = `Claude`**, **AI Model = your exact model name**
  (e.g. `Claude Opus 5.5`), **Executed By** (= the User), **Mode** and **Data Source** — never blank.
- Record what was actually seen and done: the tools called or the report files used (name and
  date range), snapshot time (UTC), the numbers that mattered with their source, decisions, and
  for a Change the exact before → after values.
- Follow-up: a date to check the result (default +7 days), what "worked" would look like, and
  which source or report the check needs.

## 5. The tracker row

Insert directly under the header row of `tracker.csv`, columns per
`references/tracker-columns.md` — including **AI tool** (`Claude`), **AI model** (your exact model
name), **User**, **Mode** and **Data source**. No column is left blank (`All` where it covers everything).

Before writing, read `Tracker schema` in `config.md` and follow `AGENTS.md` section 7 (the plugin's
copy if the repo's is older): **4** → carry on; **higher** → don't write, tell the seller to update
the plugin; **lower or missing** → migrate in the same commit (older rows: `Not recorded` in
AI tool / AI model / Data source, `unknown` in User / Mode, never guessed), set
`Tracker schema: 4`. Also, if the repo's check files
(`.github/workflows/check-tracker.yml`, `.github/scripts/check_tracker.py`) are missing or their
`Amazon Ops Copilot kit:` line is older than this plugin's, replace them in the same commit from
`${CLAUDE_PLUGIN_ROOT}/skills/setup/tracker-template/.github/` — otherwise the check can reject
values these rules allow. If writing the workflow file is
refused (the key lacks **Workflows: Read and write**), commit the rest and tell the seller once.

## 6. STATE.md and LESSONS.md

- `STATE.md`: update only the parts this activity changes — open follow-ups, changes being
  watched, next steps. Set `Last updated: <YYYY-MM-DD HH:MM UTC> — ACT-NNN — Claude / <model name> — <User> (<Mode>)`.
- `LESSONS.md`: append a lesson only if this activity taught something that should change future
  work: `## YYYY-MM-DD — <title> (ACT-NNN)`.

## 7. Commit

One commit with the page, `tracker.csv` and `STATE.md` (plus `LESSONS.md` / `config.md` if changed):
`ACT-NNN: <Type> — <short title> [Claude / <model name> · <User> · <Mode>]`. If the write is rejected because a file
changed, re-read, take the next free ID, and retry. Never overwrite another tool's entries.

If GitHub cannot be reached, give the seller the page and CSV row as ready-to-save text and say
plainly that nothing was saved yet.
