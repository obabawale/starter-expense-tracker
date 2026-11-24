# Copilot Instructions

## What This Is

This is a small Python command-line expense tracker. It stores expenses as JSON
in the local file system and has no database, HTTP service, or web UI.

## Stack & Versions

- Python 3.10 or newer (`requires-python = ">=3.10"`).
- Standard library only at runtime; no application dependencies.
- pytest and Ruff for development (`requirements-dev.txt`).
- Ruff targets Python 3.10 and uses a 100-character line length.
- Package entry point: `expense-tracker = expense_tracker.cli:main`.

## How to Run Things

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python -m expense_tracker --help
pytest
ruff check .
ruff format --check .
```

The default data file is `expenses.json` in the current working directory.
Set `EXPENSE_TRACKER_DATA` to override it for testing or isolated use.

## Conventions

- Keep changes small and match the existing module and command structure.
- Use PEP 8 and Python type hints for public functions.
- Store money as integer cents; never introduce float arithmetic for money.
- Parse and validate dates in `YYYY-MM-DD` form before storing them.
- Add behaviour tests under `tests/`, using `tmp_path` for filesystem isolation.
- Update `README.md` when usage or setup changes.

## Boundaries

- Do not add frameworks, databases, network services, or dependencies unless
  the task explicitly requires them.
- Do not modify `expenses.json` as test setup or implementation work; use
  `EXPENSE_TRACKER_DATA` or a temporary path.
- Do not expose secrets or personal/financial data in logs or prompts.
- Do not edit exercise specifications unless the user explicitly requests it.

## Definition of Done

- The requested behaviour is implemented and matches the current CLI style.
- Relevant pytest tests pass, including a case that would fail without the
  change.
- `ruff check .` and `ruff format --check .` pass.
- The diff is limited to the requested files and contains no application-data
  changes.
- Help text, examples, and README usage stay accurate after CLI changes.
