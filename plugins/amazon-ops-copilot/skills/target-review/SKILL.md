---
name: target-review
description: >
  This skill should be used when the user asks "how are we tracking against target", "month-to-date
  review", "MTD review", "will we hit the target", "run the monthly review", "forecast this month",
  or invokes /target-review. It produces the monthly target review with per-brand revenue, run
  rates, a floor forecast and ranked risks, using live KwickMetrics data.
metadata:
  version: "0.1.0"
---

# Monthly Target Review

Follow the `operating-rules` skill throughout (live data only, per-brand rows, marketplace on
every call, snapshot time stated).

## 1. Confirm the target

- Target: the monthly target in `config.md` — combined gross revenue for the in-scope brands, current
  month.
- If the target is empty or recorded for a different month, ask the
  user for this month's target before measuring against one. Never assume last month's.
- If it is unknown whether the target is measured before or after returns and cancellations,
  measure gross (before returns) and say so.

## 2. Pull the data

For each in-scope brand (account slug from `config.md`):

1. `get_sales_overview` for month-to-date — gross revenue, orders, units.
2. `get_ppc_overview` for month-to-date — spend, ad sales, ACoS; compute TACoS.
3. `get_sales_trends` daily for the month, if more than four days have elapsed (for the chart).
4. For risks: `get_restock_recommendations` (days of supply), `get_returns_overview`, and
   `get_ppc_overview` / `get_ad_campaigns` for budget-capped campaigns where available.

Today counts as a partial day: compute run rates on completed days only and say so.

## 3. Compute

| Item | Formula |
|---|---|
| Days elapsed | completed days in month |
| Days remaining | days in month − days elapsed |
| Run rate achieved | combined MTD revenue ÷ days elapsed |
| Run rate required | (target − combined MTD revenue) ÷ days remaining |
| Linear forecast (floor) | combined MTD revenue ÷ days elapsed × days in month |
| Gap | target − linear forecast |

Run the arithmetic in code, not in prose.

## 4. Forecast honesty

Present the linear projection as **the floor**, never alone as "the forecast". State that it
ignores seasonality (for example festive-season demand, sale events, Prime Day) that can lift
volume above a linear trend. If a seasonal adjustment is applied, show the assumption and its
source; otherwise give the floor and the required run rate.

## 5. Output

1. **First sentence:** ahead or behind, with the gap in currency. If the target is projected to be
   missed, say so in this sentence.
2. **Metrics table:** one row per brand plus a Combined row — MTD revenue, orders, ad spend, ACoS,
   TACoS, share of target. Exact date range and snapshot time beneath.
3. **Run-rate block:** days elapsed / remaining, run rate achieved vs required, floor forecast.
4. **Chart** of daily revenue per brand when more than four days are in the window.
5. **Key drivers** (max 3) and **risks** ranked by revenue exposure.
6. **Recommended actions** (max 3) with why, expected impact and priority — check the tracker
   for related activities first (operating-rules §6).
7. Ask permission to log the review as an **Analysis** activity via `log-activity`.
