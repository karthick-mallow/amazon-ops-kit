---
name: impact-dashboard
description: >
  This skill should be used when the user asks for "the impact dashboard", "show what our changes
  did", "chart sales with our activities", "plot ad spend with the tracker markers", "refresh the
  dashboard", or invokes /impact-dashboard. It builds a page charting daily sales and ads metrics
  per account — from a connected tool or uploaded reports — with every tracker activity marked on
  the timeline, so the seller sees what each activity did.
metadata:
  version: "0.8.1"
---

# Impact Dashboard

The dashboard joins two sources: daily metrics from the seller's data source and the activities in
the seller's GitHub tracker (see `load-context`).

## 1. Gather the data

1. Read the tracker: every activity in the last 90 days — ID, date, type, brand, title/summary,
   status, follow-up, data source, and the before / after or headline numbers from the page.
2. Get daily series for the last 90 completed days for each account in `config.md`: sales,
   orders, ad spend and ad sales.
   - **Connected tool:** use its daily trend calls (for KwickMetrics, `get_sales_trends` and
     `get_ppc_trends`).
   - **Uploaded reports:** ask once for the reports that hold daily figures — e.g. the Business
     Report by date (sales, orders) from Seller Central and a daily Sponsored Products campaign
     report (spend, ad sales) from the Ads console — for the same 90 days.
   Compute ACoS and TACoS per day. Exclude today (partial day) and shade the last 3 days as
   "still settling".
3. Save the rows to data files and compute in code. Every plotted value must come from these
   sources; record the tool names or report files and the snapshot time.

## 2. Build the page

Read `references/dashboard-spec.md` and follow it. Publish the page as an artifact (or the
platform's equivalent page output) so the seller can reopen and share it. Embed the data in the
page with the source and snapshot time in the subtitle; do not fetch live data from the page
unless the platform offers a live-data capability and the user asks for it.

## 3. Report

One or two sentences: the window, the biggest visible effect (with its numbers and ACT-ID), and
any activity whose effect cannot yet be read because its window is still settling.
