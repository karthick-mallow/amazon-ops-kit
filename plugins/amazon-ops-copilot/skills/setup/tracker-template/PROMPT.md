# Starter prompt for chat apps

Paste this into the custom instructions of any AI chat app connected to GitHub that does not read
repo files on its own — for example Grok. Claude (with the plugin), Codex and Cursor read
`AGENTS.md` by themselves and don't need it. Setup fills in the repository name for you.

---

My Amazon business history lives in the GitHub repository **OWNER/REPO**. It records everything
I've done with any AI tool, so you can pick up where I left off.

At the start of every conversation about my business, open `AGENTS.md` in that repository and
follow it: read `config.md`, `STATE.md`, `LESSONS.md` and the recent rows of `tracker.csv` before
answering, and always check the last 90 days of activity before suggesting anything. If the
tracker isn't set up yet, follow the "First conversation" section of `AGENTS.md`. For current
numbers use my data source listed in `config.md`; if you can't reach it, ask me for the report you
need and say where each figure came from. Log every change made through a connected tool
automatically; ask me before logging anything else. Record your AI tool, exact model name and the
data source in each entry, and tell me the activity ID. If you can't write to the repository, give
me the entry as ready-to-save text.
