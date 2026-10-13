# Tracker columns

`tracker.csv` header, in this order:

```csv
ID,Date (UTC),Type,Brand,Marketplace,ASIN,SKU,KwickMetrics focus,Summary,Follow-up,Status,Page
```

| Column | Value |
|---|---|
| ID | `ACT-XXX`, zero-padded, sequential |
| Date (UTC) | `YYYY-MM-DD HH:MM`, true UTC — must match the page header |
| Type | Brainstorming / Analysis / Diagnosis / Change / Review |
| Brand | A single in-scope brand name, or `Both` / `All` when the activity covers every in-scope brand — never blank |
| Marketplace | Amazon domain, e.g. `amazon.in`; `All` if it spans every connected marketplace — never blank |
| ASIN | ASINs covered, separated by `;`; `All` for whole account(s); `All <LINE>` for a product line — never blank |
| SKU | Seller SKUs covered, separated by `;` (for a campaign: every enabled advertised SKU); same `All` rules — never blank |
| KwickMetrics focus | PPC / SEO / Inventory / Financials / Buy Box |
| Summary | One sentence |
| Follow-up | `YYYY-MM-DD`, default +7 days, equal to section 7's review date; free text such as `Closed` once Completed |
| Status | Open / Scheduled / Monitoring / Completed |
| Page | Relative path to the page, e.g. `activities/ACT-007.md` |

The AI client that did the work is recorded in the page header and the commit message, not in a
column, so the CSV stays the same for every tool.

CSV rules: quote any field containing a comma or quote; use `;` inside multi-value cells; newest
row directly under the header.
