---
name: propose-change
description: >
  This skill should be used before any KwickMetrics write — when the user asks to "change a bid",
  "raise the budget", "pause this campaign", "negate these search terms", "add keywords", "update the
  listing", "publish", "set up day-parting", "fix the ACoS", "optimize my campaigns", or invokes
  /propose-change. It turns the request into an approval-ready proposal, enforces the safety
  limits, executes only what is approved, verifies it, and logs it immediately.
metadata:
  version: "0.1.0"
---

# Change Authorization

Applies to every KwickMetrics write: bids, budgets, campaign / ad group / keyword / target status,
negations, day-parting, rule sets, portfolios, listing content and publishes.

## 1. Vague requests are not approval

"Optimize my campaigns", "fix the ACoS" or "do what you think is best" is an instruction to bring
back a proposal — never to write.

## 2. Build the proposal

1. Read the tracker for related activities in the last 90 days (operating-rules §6).
2. Pull the **current** values live (e.g. `get_ad_campaigns`, `get_ad_campaign_entities`,
   `get_ppc_reports`) on a window ending 3 days before today.
3. Present one table, one row per entity:

| # | Tool | Entity (name + ID) | Current | Proposed | % change | Reason (data) | Rollback condition |
|---|---|---|---|---|---|---|---|

Rollback condition = metric + threshold + timeframe (e.g. "ACoS above 45% over the next 7 days").

## 3. Limits on one proposal

Do not include in a single batch:

- a bid change greater than ±30% of current;
- a budget change greater than ±25% of current;
- a pause of any entity that spent more than the high-spend pause threshold in `config.md` per day over
  the last 7 days — list it separately and ask for its own confirmation;
- any listing content publish — one at a time, `preview_listing` first;
- more than 10 entities, unless the user asks for a bulk operation by name.

Split anything larger into stages and say so.

## 4. Known trap — day-parted keywords

API bid writes on keywords inside a day-parting schedule can revert to the base bid within a day,
while the read straight after the write still shows the new value. For these keywords, do not
write the bid by API: ask the user to change the **base bid** in the KwickMetrics interface, then
verify 24 hours later. Check `get_ad_day_partings` / `get_ad_day_parting_campaigns` before any
keyword bid proposal.

## 5. Approval and execution

1. Wait for explicit approval in this session. One approval covers only the rows it names.
2. Capture the before-state (already pulled) and keep it.
3. Execute exactly the approved rows, nothing else.
4. Verify each write with a read call and report any row that did not take.
5. **Log immediately** with `log-activity` as a **Change** activity, filling the Change Record
   table (before, after, scope, rollback condition). An executed change that is not logged is a
   gap in the tracker. Set Status to Monitoring and the follow-up to the rollback timeframe.
