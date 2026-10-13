---
name: review-followups
description: >
  This skill should be used when the seller asks "what follow-ups are due", "did last week's change
  work", "check open activities", "what's pending", or invokes /review-followups. It finds tracker
  activities whose follow-up date has arrived, compares them with live KwickMetrics data, and logs
  the result.
metadata:
  version: "0.6.0"
---

# Review Follow-ups

1. **Find what is due.** Read `tracker.csv` in the seller's tracker repo (found as in `load-context`). List rows with
   Status Open, Scheduled or Monitoring and a Follow-up date on or before today, oldest first. If
   none are due, say so and list the next three dates.
2. **Check each one** (or the one the seller names): open its page, take what was done and what
   "worked" was supposed to look like, then pull the same numbers from KwickMetrics for the period
   since. Ads data takes 2–3 days to settle; say so if the window is too recent.
3. **Report** per activity: before → now, and a plain verdict — worked, partly worked, didn't work,
   or too early to tell.
4. **Record it** with `log-activity` as one **Review** activity. Then update each reviewed row's
   Status and Follow-up in place, and add a dated `Review note (YYYY-MM-DD, ACT-NNN)` at the end
   of its page. Never change the original page's figures.
