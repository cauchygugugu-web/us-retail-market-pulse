# Instructions for Future Codex Chats

## Project purpose

This is a learning and portfolio project. It should help the user practise building a structured
Python project in PyCharm while producing a credible U.S. retail market analysis for job
applications.

The business question is: which major U.S. retail categories show the strongest combination of
real demand growth, market-share momentum, stability, and manageable inventory risk?

## How to resume work

At the beginning of a new chat:

1. Read `README.md` and `TASKS.md`.
2. Inspect `git status`, the latest commit, and the current project structure.
3. Run the smallest relevant existing test before changing code.
4. Start from the first unchecked item under **Next smallest action** in `TASKS.md`.
5. Explain the purpose of the task in beginner-friendly Chinese before implementation.

## Teaching style

- The user is learning Python project development, not only requesting a finished artifact.
- Prefer one small, verifiable task at a time.
- Explain what each important file, function, command, and test is for.
- When practical, let the user implement a learning step and then review it.
- Do not introduce advanced modeling before the data definitions and validation are trustworthy.
- Keep technical language clear and concise; use Chinese for guidance and English where it belongs
  in code, identifiers, commit messages, and portfolio-facing documentation.

## Project rules

- Treat official Census and BLS sources as authoritative.
- Verify fields, units, category codes, frequency, and adjustment status before using a series.
- Keep raw source extracts unchanged.
- Keep reusable transformations in `src/us_retail_market_pulse/`.
- Use notebooks for exploration and communication, not as the only implementation.
- Add tests for reusable logic and important calculations.
- Preserve chronological order in any time-series evaluation.
- Label nominal and inflation-adjusted measures explicitly.
- Describe lead/lag or regression results as predictive associations unless a credible causal design
  exists.
- Never commit `.env`, API keys, virtual environments, caches, or large raw data extracts.
- Do not claim findings in the README until they are reproduced from verified data.

## Change discipline

- Inspect existing files before editing them.
- Preserve unrelated user changes.
- Do not commit or push unless the user asks.
- After code changes, run `python -m pytest` and `python -m ruff check .` when applicable.
- Update `TASKS.md` when a checklist item is completed or the next action changes.
- Prefer small commits that describe one meaningful learning milestone.

## Current handoff

The minimal package structure, virtual environment, smoke test, lint configuration, local Git
history, and public GitHub repository are working. No analysis data has been downloaded and no
findings have been produced.

The next task is to verify the official Census MRTS metadata and identify the exact fields, units,
seasonal-adjustment flags, total-retail denominator, and category codes for the six target retail
categories. See `TASKS.md` for the complete roadmap.
