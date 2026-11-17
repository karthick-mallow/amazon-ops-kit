# Tracker columns

`tracker.csv` header, in this order:

```csv
ID,Date (UTC),AI tool,AI model,User,Mode,Type,Brand,Marketplace,ASIN,SKU,Focus,Data source,Summary,Follow-up,Status,Page
```

| Column | Value |
|---|---|
| ID | `ACT-XXX`, zero-padded, sequential |
| Date (UTC) | `YYYY-MM-DD HH:MM`, true UTC — must match the page header |
| AI tool | The AI app that did the work, e.g. `Claude`, `Codex`, `Grok`, `Cursor` — never blank |
| AI model | The exact model name, e.g. `Claude Opus 5.5` — as the tool reports it; `Unknown` only if the tool cannot tell |
| User | The person who asked for or approved the work, as named in `config.md` → **Users**; unknown on an automatic log → the owner (first row); `Schedule` → who set up the scheduled task, else the owner — never blank |
| Mode | `Chat` (typed), `Voice` (spoken request) or `Schedule` (started by a scheduled task / routine with no person sending it); unsure between Chat and Voice → `Chat` — never blank |
| Type | Brainstorming / Analysis / Diagnosis / Change / Review |
| Brand | The brand or account the activity is about, or `All` when it covers every account — never blank |
| Marketplace | Amazon domain, e.g. `amazon.in`; `All` if it spans every marketplace — never blank |
| ASIN | ASINs covered, separated by `;`; `All` for whole account(s); `All <LINE>` for a product line — never blank |
| SKU | Seller SKUs covered, separated by `;` (for a campaign: every enabled advertised SKU); same `All` rules — never blank |
| Focus | PPC / SEO / Inventory / Financials / Buy Box / Listings / Pricing / Returns |
| Data source | Where the numbers came from: the connected tool's name (e.g. `KwickMetrics`); `Report: <report name> (<start>–<end>)` for an uploaded file; `Seller` for figures given in chat; `None` for pure brainstorming. Several separated by `;` — never blank |
| Summary | One sentence |
| Follow-up | `YYYY-MM-DD`, default +7 days, equal to section 7's review date; free text such as `Closed` once Completed |
| Status | Open / Scheduled / Monitoring / Completed |
| Page | Relative path to the page, e.g. `activities/ACT-007.md` |

CSV rules: quote any field containing a comma or quote; use `;` inside multi-value cells; newest
row directly under the header.

This is **schema 4** (`Tracker schema: 4` in `config.md`). Older trackers are migrated as
`AGENTS.md` section 7 describes: `Not recorded` in `AI tool`, `AI model` and `Data source`, and
`unknown` in `User` and `Mode`, for rows written before them — never guessed values.

The tracker check (`.github/scripts/check_tracker.py`) enforces these rules on GitHub: header,
column count, no blanks, ID / date / follow-up formats, the allowed Type, Mode, Status and Focus
values, and that Page exists.
