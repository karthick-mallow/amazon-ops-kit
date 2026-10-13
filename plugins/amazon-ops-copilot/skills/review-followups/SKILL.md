---
name: review-followups
description: >
  This skill should be used when the user asks "what follow-ups are due", "review last week's
  change", "did the bid change work", "check open activities", "run the weekly review", or invokes
  /review-followups. It finds tracker activities whose follow-up date has arrived, measures them
  against their success criteria with live KwickMetrics data, and logs the result as a Review.
metadata:
  version: "0.1.0"
---

# Follow-up Review

Follow `operating-rules` and read the tracker as described in `log-activity`.

1. **Find what is due.** Read the tracker. List rows with Status Open, Scheduled or Monitoring and a
   Follow-up date on or before today, oldest first. If none are due, say so and show the next
   three upcoming dates.
2. **For each due activity** (or the one the user names):
   - Open its page. Take the metrics, success criteria and rollback condition from sections 5
     and 7, and the before-state from section 4 or the Change Record.
   - Pull the same metrics live for the comparable window after the activity, using the same tools
     and filters as the original page. Respect latency: end the window 3 days before today.
   - Build a before / after table per brand with the change and % change.
   - Verdict: **Met**, **Partly met**, **Not met**, or **Too early** (window still settling).
   - If a rollback condition has tripped, say so in the first sentence and offer a rollback
     proposal through `propose-change`. Never roll back without approval.
3. **Report**: verdicts first, then the tables, then at most three next actions.
4. **Log** (with permission) one **Review** activity covering the reviewed IDs. Then, for each
   reviewed activity, update its row's Status and Follow-up in place and append
   `Review note (YYYY-MM-DD, ACT-XXX)` to the end of its page with the verdict and the key
   numbers. Never edit the original figures.
