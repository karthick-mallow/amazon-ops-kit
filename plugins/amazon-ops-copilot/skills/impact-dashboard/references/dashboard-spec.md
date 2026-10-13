# Impact Dashboard — page spec

## Layout

- **Header:** title "Impact Dashboard", subtitle `<marketplace> · KwickMetrics data to <last
  complete day> · snapshot <UTC time> · today is partial and not plotted`.
- **Brand switch** (segmented control): one button per account in `config.md`, plus "All". "All"
  draws one line per brand in its own colour — never a summed line.
- **Main panel (about 78% width on desktop, full width on mobile):**
  - Toolbar: Metric (Sales, Ad spend, Orders, ACoS, TACoS) · Style (Area, Line, Bar) · Range
    (7D, 30D, 60D, 90D; default 30D) · Annotations dropdown with checkboxes for Changes (C),
    Analysis (A), Diagnosis (D), Reviews (R) and Brainstorming (B).
  - Legend row: brand name, latest value, change vs the start of the range, and a dashed 7-day
    moving average.
  - Chart: daily series; 7-day moving average dashed; the last 3 days shaded "settling".
  - Activity markers: a lettered circle per activity on its date, coloured by type, on a short stem
    above the plot. Several activities on one day collapse into one marker showing the count.
  - Hover or tap a day: crosshair, value, and the activities on that date.
  - Selecting a Change marker shades 7 days before (blue tint) and 7 days after (red tint).
- **Side panel (about 22%):** activity cards, newest first, filtered by the current brand and
  annotation choices. Each card: ACT-ID, type, date, title, one-line summary, status pill, the AI
  client that did the work (from the page header, e.g. Claude, Codex, Gemini), and for
  Change / Review activities a small before / after table (metric, before, after, change) taken
  from the page. Cards with an open follow-up show "Waiting — review on <date>". Clicking a card
  selects its marker and scrolls the chart to it, and vice versa.

## Colours

- Activity types: Change red-orange, Analysis blue, Diagnosis amber, Review teal, Brainstorming
  grey. Up = green, down = red for change values (for ACoS/TACoS, down is good — colour by
  direction of good, not sign).
- One distinct colour per brand, consistent across the chart, legend and cards.
- Define all colours as CSS variables with a dark-mode set; give `body` an explicit background.

## Behaviour and accessibility

- Works at phone width with a 16px side gutter and no horizontal scroll; the side panel stacks
  under the chart below about 980px.
- Keyboard focus visible on every control and marker; markers are buttons with an aria-label
  `ACT-XXX <type>, <date>: <title>`.
- Tabular, monospaced numbers; currency formatted for the seller's currency.
- Remember the last brand, metric and range per viewer in browser storage, wrapped in try/catch.

## Data notes printed under the chart

- Sources: tool names, date range, snapshot time.
- "Before / after numbers on cards are copied from tracker pages and are not recalculated here."
- Any brand or day with missing data, stated plainly.
