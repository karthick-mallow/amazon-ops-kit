# Lessons learned

Append-only. Each lesson changes how future work is done. Format:
`## YYYY-MM-DD — <short title> (ACT-NNN)` then what happened and what to do from now on.

## Starter lessons (general Amazon behaviour)

### Recent ads data reads too good
Amazon advertising and attribution data lags 24–72 hours, so the last 1–3 days look better than
they will settle. Do not decide bids, budgets or pauses on a window ending in the last 3 days.

### Day-parted keyword bids can silently revert
A bid change made through a connector on a keyword inside a day-parting or bid schedule can revert
to the base bid within a day, while the read straight after the write still shows the new bid. For
those keywords, change the base bid in the scheduling tool's own interface, then verify 24 hours
later.

### Check the fee setup before trusting margins
If a brand's profit report shows zero or near-zero Amazon fees (referral, closing, FBA), the fee
configuration in that tool is incomplete and its margin is not usable until it is fixed.

### Say where every number came from
A figure without a source can't be checked later. Name the tool, or the report file and its date
range, next to every number in a page.
