# AGENTS.md — Amazon Activity Tracker

This repository is the shared memory of an Amazon seller business. It records every analysis,
decision and change the seller makes with any AI assistant — Claude, ChatGPT / Codex, Gemini,
Grok, Copilot, Cursor or another — so whichever tool they open next already knows what has been
done and the seller never has to explain it again.

It works with any data source: a connected tool (KwickMetrics, another seller tool, Amazon Ads or
any MCP connector) or reports the seller downloads from Seller Central or the Ads console and
uploads. `config.md` lists the seller's sources.

Every AI tool reads and writes this repository the same way, as described below.

---

## 1. Start of every conversation — read first

1. `config.md` — the seller's accounts, data sources, and any goals they have set.
2. `STATE.md` — where things stand: open follow-ups, changes being watched, next steps.
3. `LESSONS.md` — what earlier work taught.
4. `tracker.csv` — every activity, newest first. For the topic at hand, open the related pages in
   `activities/` from the last 90 days.

**Before suggesting anything, always check the last 90 days.** Filter `tracker.csv` to the last
90 days and to the same account, ASIN/SKU, campaign or area; open those pages; tell the seller in
one or two lines what was already done, by which AI tool, and what happened (or "No related
activity in the last 90 days"). Don't repeat something already tried unless current data justifies
it, and say what has changed since.

## 2. Current numbers — from a data source, never from memory

**History is not live data.** Numbers here are what was true when they were logged.

1. If a source in `config.md` is connected to you, pull current figures from it.
2. If not, ask the seller for the specific report you need — name it and the date range (e.g.
   "Sponsored Products search term report, last 30 days, from the Ads console") — and work from
   the file they share.
3. Label every figure with where it came from: the tool, or the report file and its date range.
4. Never guess or estimate a figure you couldn't get; say what is missing.

## 3. Goals — only when the seller states them

Do not ask the seller for targets. When they state one in conversation (monthly revenue, target
ACoS, a budget limit, a focus brand, a reporting preference), add or update a line under
**Goals and preferences** in `config.md`: `- <goal> — set <YYYY-MM-DD> (<AI tool>)`, and confirm
in one sentence.

## 4. Logging — automatic for changes made through a connected tool, approval for everything else

| What happened | Log it |
|---|---|
| A change made **through a connected tool** — any tool call that creates, updates, pauses, deletes, negates, applies, links or publishes something in the seller's Amazon account, ads or listings (KwickMetrics or any other connector) | **Automatically, right after the change.** Don't ask. |
| Anything else worth keeping: analysis, diagnosis, brainstorming, a plan, a follow-up review, work done from uploaded reports, or a change the seller made **by hand** (e.g. in Seller Central) | **Only with the seller's approval.** At the end, ask once: "Shall I save this to your tracker as an <Type>?" |
| Small talk, general how-to, nothing decided | Don't log. |

"Log this" counts as approval; "don't log this" stops any logging for that request.

1. **ID.** Re-read `tracker.csv` from the default branch now. Next ID = highest `ACT-NNN` + 1,
   three digits. Never reuse an ID.
2. **Page.** Write `activities/ACT-NNN.md` from `TEMPLATE.md`: eight sections, same headings, same
   order; empty sections read `Not applicable — <reason>`. In the header, record **AI Tool** (your
   app's name, e.g. Claude, ChatGPT, Grok, Gemini), **AI Model** (your exact model name, e.g.
   Claude Opus 5.5), **Data Source**, and how it was logged (automatically or with approval).
   Include the tools called or reports used, date range, snapshot time (UTC), the numbers that
   mattered, decisions, and for a change the exact before → after values.
3. **Row.** Add a row directly under the header of `tracker.csv`:

   `ID,Date (UTC),AI tool,AI model,Type,Brand,Marketplace,ASIN,SKU,Focus,Data source,Summary,Follow-up,Status,Page`

   - AI tool / AI model: your app and exact model name — never blank.
   - Type: Brainstorming · Analysis · Diagnosis · Change · Review.
   - Brand / Marketplace / ASIN / SKU: never blank — use `All` when it covers everything; separate
     several values with `;`.
   - Focus: PPC · SEO · Inventory · Financials · Buy Box · Listings · Pricing · Returns.
   - Data source: the connected tool's name (e.g. `KwickMetrics`), or `Report: <report name>
     (<start>–<end>)` for an uploaded file, or `Seller` for figures the seller gave in chat, or
     `None` for pure brainstorming; several separated by `;`.
   - Follow-up: `YYYY-MM-DD` (default +7 days). Status: Open · Scheduled · Monitoring · Completed.
   - Page: `activities/ACT-NNN.md`. Quote any field containing a comma.
4. **STATE.md.** Update only what this activity changes; set the "Last updated" line to the time,
   ID, your AI tool and model.
5. **LESSONS.md.** Append a lesson only if something was learned that should change future work.
6. **Commit** all files together: `ACT-NNN: <Type> — <short title> [<AI tool> / <AI model>]`.
7. Tell the seller: `Saved to your tracker as ACT-NNN.`

**Checking a follow-up:** pull the same numbers from the same source as the original activity (for
a report, ask the seller for the same report covering the newer dates). Give each a verdict —
worked, partly worked, didn't work, or too early / no data yet. With the seller's approval, log a
new Review activity; in the original row update Status and Follow-up in place; append
`Review note (YYYY-MM-DD, ACT-NNN)` to the original page. Never change an old page's figures.

**An older tracker** (header without `AI tool` / `AI model`, or with `KwickMetrics focus` and no
`Data source`): before writing, bring the header up to date in the same commit — add `AI tool` and
`AI model` after `Date (UTC)`, rename `KwickMetrics focus` to `Focus`, add `Data source` after it
— and fill `Not recorded` in the new columns for older rows. Change nothing else in old rows.

## 5. Several AI tools, one memory

- Re-read `tracker.csv` and `STATE.md` just before writing. If a write is rejected because a file
  changed, re-read, take the next free ID, and retry. Never overwrite another tool's entries.
- Never delete or rewrite old rows or pages, except the Status / Follow-up update, the review note
  and the header update above.
- **Can read but not write here?** Give the seller the page, the CSV row and the `STATE.md` change
  as ready-to-save text, and say plainly that nothing was saved yet.

## 6. Files

| File | Holds |
|---|---|
| `AGENTS.md` | These instructions |
| `config.md` | Accounts, data sources, and goals and preferences the seller has set |
| `STATE.md` | Where things stand now |
| `LESSONS.md` | Lessons learned (append-only) |
| `tracker.csv` | One row per activity, newest first |
| `activities/ACT-NNN.md` | One page per activity |
| `TEMPLATE.md` | The activity page format |
| `PROMPT.md` | Starter prompt for chat apps that don't read repo files on their own |
| `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` | Point those tools to this file |
