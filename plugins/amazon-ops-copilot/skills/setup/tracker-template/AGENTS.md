# AGENTS.md — Amazon Activity Tracker

This repository is the shared memory of an Amazon seller business managed with **KwickMetrics**.
It records every analysis, decision and change the seller makes with any AI assistant — Claude,
ChatGPT / Codex, Gemini, Grok, Copilot, Cursor or another — so whichever tool they open next
already knows what has been done and the seller never has to explain it again.

Every AI tool reads and writes this repository the same way, as described below.

---

## 1. Start of every conversation — read first

1. `config.md` — the seller's KwickMetrics accounts, and any goals they have set.
2. `STATE.md` — where things stand: open follow-ups, changes being watched, next steps.
3. `LESSONS.md` — what earlier work taught.
4. `tracker.csv` — every activity, newest first. For the topic at hand, open the related pages in
   `activities/` from the last 90 days.

Then help the seller. Mention related earlier work briefly by ID (what was done, by which AI tool,
what happened) so they can see the context was picked up.

**History is not live data.** Numbers here are what was true when they were logged. For any
current figure, pull it from KwickMetrics now.

## 2. Goals — only when the seller states them

Do not ask the seller for targets. When they state one in conversation (monthly revenue, target
ACoS, a budget limit, a focus brand, a reporting preference), add or update a line under
**Goals and preferences** in `config.md`: `- <goal> — set <YYYY-MM-DD> (<AI tool>)`, and confirm
in one sentence.

## 3. Log every working session

At the end of any conversation where real work happened — data pulled and discussed, a problem
diagnosed, a decision or plan made, or something changed — log it without being asked. Log a
change to the live account **immediately** after it is made. Skip chit-chat and general how-to
questions. If the seller says "don't log this", don't.

1. **ID.** Re-read `tracker.csv` from the default branch now. Next ID = highest `ACT-NNN` + 1,
   three digits. Never reuse an ID.
2. **Page.** Write `activities/ACT-NNN.md` from `TEMPLATE.md`: eight sections, same headings, same
   order; empty sections read `Not applicable — <reason>`. In the header, record **your AI tool and
   model** (e.g. "Codex / GPT-5", "Claude / Opus", "Gemini CLI / Gemini 2.5 Pro"). Include the
   KwickMetrics tools used, date range, snapshot time (UTC), the numbers that mattered, decisions,
   and for a change the exact before → after values.
3. **Row.** Add a row directly under the header of `tracker.csv`:

   `ID,Date (UTC),Type,Brand,Marketplace,ASIN,SKU,KwickMetrics focus,Summary,Follow-up,Status,Page`

   - Type: Brainstorming · Analysis · Diagnosis · Change · Review.
   - Brand / Marketplace / ASIN / SKU: never blank — use `All` when it covers everything; separate
     several values with `;`.
   - Focus: PPC · SEO · Inventory · Financials · Buy Box.
   - Follow-up: `YYYY-MM-DD` (default +7 days). Status: Open · Scheduled · Monitoring · Completed.
   - Page: `activities/ACT-NNN.md`. Quote any field containing a comma.
4. **STATE.md.** Update only what this activity changes; set the "Last updated" line to the time,
   ID and your AI tool.
5. **LESSONS.md.** Append a lesson only if something was learned that should change future work.
6. **Commit** all files together: `ACT-NNN: <Type> — <short title> [<AI tool>]`.
7. Tell the seller: `Saved to your tracker as ACT-NNN.`

**Checking a follow-up:** log a new Review activity; in the original row update Status and
Follow-up in place; append `Review note (YYYY-MM-DD, ACT-NNN)` to the original page. Never change
an old page's figures.

## 4. Several AI tools, one memory

- Re-read `tracker.csv` and `STATE.md` just before writing. If a write is rejected because a file
  changed, re-read, take the next free ID, and retry. Never overwrite another tool's entries.
- Never delete or rewrite old rows or pages, except the Status / Follow-up update and review note.
- **Can read but not write here?** Give the seller the page, the CSV row and the `STATE.md` change
  as ready-to-save text, and say plainly that nothing was saved yet.

## 5. Files

| File | Holds |
|---|---|
| `AGENTS.md` | These instructions |
| `config.md` | KwickMetrics accounts; goals and preferences the seller has set |
| `STATE.md` | Where things stand now |
| `LESSONS.md` | Lessons learned (append-only) |
| `tracker.csv` | One row per activity, newest first |
| `activities/ACT-NNN.md` | One page per activity |
| `TEMPLATE.md` | The activity page format |
| `PROMPT.md` | Starter prompt for chat apps that don't read repo files on their own |
| `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` | Point those tools to this file |
