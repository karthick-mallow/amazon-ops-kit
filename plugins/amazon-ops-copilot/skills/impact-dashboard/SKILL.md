---
name: impact-dashboard
description: >
  This skill should be used when the user asks for "the impact dashboard", "show what our changes
  did", "chart sales with our activities", "plot ad spend with the tracker markers", "refresh the
  dashboard", or invokes /impact-dashboard. It builds a page charting daily KwickMetrics metrics per
  brand with every tracker activity marked on the timeline and its before / after impact.
metadata:
  version: "0.1.0"
---

# Impact Dashboard

Follow `operating-rules`. The dashboard joins two sources: daily metrics from KwickMetrics and
activities from the tracker (`log-activity`).

## 1. Gather the data

1. Read the tracker: every activity in the last 90 days — ID, date, type, brand, title/summary,
   status, follow-up, and the before / after or headline numbers from the page.
2. For each in-scope brand, pull daily series for the last 90 completed days:
   `get_sales_trends` (sales, orders) and `get_ppc_trends` (spend, ad sales). Compute ACoS and
   TACoS per day. Exclude today (partial day) and shade the last 3 days as "still settling".
3. Save the rows to data files and compute in code. Every plotted value must come from these
   calls; record the tool names and snapshot time.

## 2. Build the page

Read `references/dashboard-spec.md` and follow it. Publish the page as an artifact (or the
platform's equivalent page output) so the seller can reopen and share it. Embed the data in the
page with the snapshot time in the subtitle; do not fetch live data from the page unless the
platform offers a live-data capability and the user asks for it.

## 3. Report

One or two sentences: the window, the biggest visible effect (with its numbers and ACT-ID), and
any activity whose effect cannot yet be read because its window is still settling.
