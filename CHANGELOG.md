# Changelog

## 0.4.0 — 2026-10-13

- Plugin settings cut to two required boxes: Tracker GitHub repository and GitHub token.
  Business settings (brands, marketplace, currency, target, pause threshold) are asked by
  `/setup` and kept in `config.md` in the tracker repo, so every AI tool reads the same values.

## 0.3.0 — 2026-10-12

- Tracker repo becomes shared memory for any AI tool: `AGENTS.md` rulebook, `STATE.md` current
  position, `LESSONS.md`, plus `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`
  pointers and a `PROMPT.md` starter prompt for ChatGPT, Grok and other chat apps.
- Tracker README explains how to connect Claude, Codex, Gemini CLI, Cursor, Copilot, ChatGPT and
  Grok to the repo and to KwickMetrics.
- Pages and commits record the AI client and model; logging refreshes `STATE.md` and appends
  lessons.
- Setup copies the full template, never overwrites existing history, and can rebuild `STATE.md`
  when importing an old tracker.

## 0.2.0 — 2026-10-12

- The Activity Tracker now lives only in GitHub; the Claude Docs option is removed.
- Setting "Tracker GitHub repository" replaces the store and location settings.
- Setup can import an existing tracker (Claude Docs, Notion or spreadsheet) into GitHub.

## 0.1.0 — 2026-10-12

- First release: operating rules, target review, propose change, log activity, review follow-ups,
  impact dashboard and setup skills; KwickMetrics and GitHub connectors; GitHub or Claude Docs
  tracker store.
