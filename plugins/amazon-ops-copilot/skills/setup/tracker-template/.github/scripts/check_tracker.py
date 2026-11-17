#!/usr/bin/env python3
"""Check the Amazon Activity Tracker against its schema (see AGENTS.md, "Schema versions").

Standard library only. Exit 0 = pass (warnings allowed), 1 = errors found.
Usage: python3 .github/scripts/check_tracker.py [--root .] [--report report.md]
"""
import argparse
import csv
import os
import re
import sys

CURRENT_SCHEMA = 4

HEADERS = {
    1: "ID,Date (UTC),Type,Brand,Marketplace,ASIN,SKU,KwickMetrics focus,Summary,Follow-up,Status,Page",
    2: "ID,Date (UTC),AI tool,AI model,Type,Brand,Marketplace,ASIN,SKU,KwickMetrics focus,Summary,Follow-up,Status,Page",
    3: "ID,Date (UTC),AI tool,AI model,Type,Brand,Marketplace,ASIN,SKU,Focus,Data source,Summary,Follow-up,Status,Page",
    4: "ID,Date (UTC),AI tool,AI model,User,Mode,Type,Brand,Marketplace,ASIN,SKU,Focus,Data source,Summary,Follow-up,Status,Page",
}

ENUMS = {
    "Type": {"Brainstorming", "Analysis", "Diagnosis", "Change", "Review"},
    "Mode": {"Chat", "Voice", "Schedule"},
    "Status": {"Open", "Scheduled", "Monitoring", "Completed"},
    "Focus": {"PPC", "SEO", "Inventory", "Financials", "Buy Box", "Listings", "Pricing", "Returns"},
}
MULTI_VALUE = {"Focus"}
# Rows written before User/Mode existed hold `unknown` there (AGENTS.md, "Schema versions").
LEGACY_VALUES = {"Mode": {"unknown"}}
ID_RE = re.compile(r"^ACT-(\d{3,})$")
DATETIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SCHEMA_RE = re.compile(r"^Tracker schema:\s*(\S+)\s*$", re.MULTILINE)


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def error(self, where, msg):
        self.errors.append((where, msg))

    def warn(self, where, msg):
        self.warnings.append((where, msg))


def check(root, rep):
    config_path = os.path.join(root, "config.md")
    tracker_path = os.path.join(root, "tracker.csv")
    if not os.path.isfile(config_path):
        rep.error("config.md", "file is missing")
        return
    if not os.path.isfile(tracker_path):
        rep.error("tracker.csv", "file is missing")
        return

    config = open(config_path, encoding="utf-8").read()
    m = SCHEMA_RE.search(config)
    if not m:
        rep.error("config.md", "no `Tracker schema: N` line — ask your AI tool to \"update my AGENTS.md\"")
        return
    if not m.group(1).isdigit() or int(m.group(1)) not in HEADERS:
        rep.error("config.md", f"unknown tracker schema `{m.group(1)}` (this check knows 1–{CURRENT_SCHEMA})")
        return
    schema = int(m.group(1))
    if schema < CURRENT_SCHEMA:
        rep.warn("config.md", f"tracker schema {schema} is older than {CURRENT_SCHEMA} — the next AI "
                 "entry will migrate it (AGENTS.md, \"Schema versions\")")

    with open(tracker_path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        rep.error("tracker.csv", "file is empty — it must hold at least the header row")
        return
    header = rows[0]
    if ",".join(header) != HEADERS[schema]:
        rep.error("tracker.csv:1", f"header doesn't match schema {schema}. Expected: `{HEADERS[schema]}`")
        return
    col = {name: i for i, name in enumerate(header)}

    seen, numbers = {}, []
    for line_no, row in enumerate(rows[1:], start=2):
        where = f"tracker.csv:{line_no}"
        if not any(cell.strip() for cell in row):
            rep.error(where, "blank line — remove it")
            continue
        if len(row) != len(header):
            rep.error(where, f"has {len(row)} columns, header has {len(header)} — quote any field "
                      "that contains a comma")
            continue
        get = lambda name: row[col[name]].strip()
        act_id = get("ID")
        where = f"{where} ({act_id or 'no ID'})"

        for name in header:
            if not get(name):
                rep.error(where, f"`{name}` is blank")

        m = ID_RE.match(act_id)
        if act_id and not m:
            rep.error(where, "ID must look like `ACT-007`")
        elif m:
            if act_id in seen:
                rep.error(where, f"duplicate ID (also on line {seen[act_id]})")
            seen[act_id] = line_no
            numbers.append(int(m.group(1)))

        if get("Date (UTC)") and not DATETIME_RE.match(get("Date (UTC)")):
            rep.error(where, "`Date (UTC)` must be `YYYY-MM-DD HH:MM`")

        follow = get("Follow-up")
        if follow and not DATE_RE.match(follow) and get("Status") != "Completed":
            rep.error(where, "`Follow-up` must be `YYYY-MM-DD` unless Status is Completed")

        # Rows written before User/Mode existed are legacy: their enum slips are warnings only.
        legacy = "User" in col and get("User") == "unknown"
        for name, allowed in ENUMS.items():
            if name not in col or not get(name):
                continue
            values = [v.strip() for v in get(name).split(";")] if name in MULTI_VALUE else [get(name)]
            bad = [v for v in values if v not in allowed and v not in LEGACY_VALUES.get(name, set())]
            if bad:
                msg = f"`{name}` has {', '.join(f'`{b}`' for b in bad)}; allowed: {', '.join(sorted(allowed))}"
                (rep.warn if legacy else rep.error)(where, msg)

        if "User" in col and not legacy and get("Mode") == "unknown":
            rep.error(where, "`Mode` is `unknown` on a row with a named User — use Chat, Voice or Schedule")

        page = get("Page")
        if page and act_id:
            if page != f"activities/{act_id}.md":
                rep.error(where, f"`Page` should be `activities/{act_id}.md`")
            elif not os.path.isfile(os.path.join(root, page)):
                rep.error(where, f"page `{page}` doesn't exist")

    if numbers != sorted(numbers, reverse=True):
        rep.warn("tracker.csv", "rows aren't newest first (highest ID directly under the header)")


def render(rep):
    lines = []
    if rep.errors:
        lines.append(f"**Tracker check failed** — {len(rep.errors)} error(s), {len(rep.warnings)} warning(s).\n")
        lines.append("Ask your AI tool: *\"Fix the tracker check issue\"*. It fixes only what is listed "
                     "here and never changes figures.\n")
        lines.append("### Errors\n")
        lines += [f"- {w}: {m}" for w, m in rep.errors]
    else:
        lines.append(f"**Tracker check passed** — {len(rep.warnings)} warning(s).\n")
    if rep.warnings:
        lines.append("\n### Warnings\n")
        lines += [f"- {w}: {m}" for w, m in rep.warnings]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--report")
    args = ap.parse_args()
    rep = Report()
    check(args.root, rep)
    text = render(rep)
    print(text)
    for where, msg in rep.errors:
        print(f"::error title=Tracker check::{where}: {msg}")
    for where, msg in rep.warnings:
        print(f"::warning title=Tracker check::{where}: {msg}")
    if args.report:
        open(args.report, "w", encoding="utf-8").write(text)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        open(summary, "a", encoding="utf-8").write(text)
    sys.exit(1 if rep.errors else 0)


if __name__ == "__main__":
    main()
