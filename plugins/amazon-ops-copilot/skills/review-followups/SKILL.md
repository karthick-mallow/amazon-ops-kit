---
name: review-followups
description: >
  This skill should be used when the seller asks "what follow-ups are due", "did last week's change
  work", "check open activities", "what's pending", or invokes /review-followups. It finds tracker
  activities whose follow-up date has arrived, compares them with fresh numbers from the same data
  source (a connected tool or an updated report), and logs the result.
metadata:
  version: "0.8.0"
---

# Review Follow-ups

1. **Find what is due.** Read `tracker.csv` in the seller's tracker repo (found as in
   `load-context`). List rows with Status Open, Scheduled or Monitoring and a Follow-up date on or
   before today, oldest first. If none are due, say so and list the next three dates.
2. **Check each one** (or the one the seller names): open its page, take what was done, what
   "worked" was supposed to look like, and its **Data Source**. Get the same numbers for the
   period since from the same source:
   - a connected tool → pull them now;
   - an uploaded report → ask the seller once, for all due items together, for the same reports
     covering the newer dates (name each report and range);
   - not available → don't guess.
   Ads data takes 2–3 days to settle; say so if the window is too recent.
3. **Report** per activity: before → now with each figure's source, and a plain verdict — worked,
   partly worked, didn't work, too early to tell, or no data yet (say which report would settle
   it).
4. **Record it** — ask the seller, then log one **Review** activity with `log-activity`. Then
   update each reviewed row's Status and Follow-up in place, and add a dated
   `Review note (YYYY-MM-DD, ACT-NNN)` at the end of its page. Never change the original page's
   figures.
