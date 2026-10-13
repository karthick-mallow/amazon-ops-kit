# Lessons learned

Append-only. Each lesson changes how future work is done. Format:
`## YYYY-MM-DD — <short title> (ACT-NNN)` then what happened and what to do from now on.

## Starter lessons (general Amazon / KwickMetrics behaviour)

### Recent ads data reads too good
Amazon advertising and attribution data lags 24–72 hours, so the last 1–3 days look better than
they will settle. Do not decide bids, budgets or pauses on a window ending in the last 3 days.

### Day-parted keyword bids can silently revert
An API bid change on a keyword inside a day-parting schedule can revert to the base bid within a
day, while the read straight after the write still shows the new bid. For those keywords, change
the base bid in the KwickMetrics interface by hand, then verify 24 hours later.

### Check the P&L fee setup before trusting margins
If a brand's profit report shows zero or near-zero Amazon fees (referral, closing, FBA), the fee
configuration is incomplete and its margin is not usable until it is fixed
(`get_pnl_configuration`).
