---
description: "Use when writing or updating pytest tests, temporary JSON stores, CLI output assertions, or test fixtures."
applyTo:
  - "tests/**"
  - "pytest.ini"
  - "pyproject.toml"
---

# Python Test Guidelines

- Add behavior-level pytest tests under `tests/` for every new command or changed
  validation rule.
- Use `tmp_path` and `Store(path=tmp_path / "expenses.json")` for filesystem
  isolation; reuse `tests/conftest.py` helpers where they match the test.
- Use `capsys` to verify CLI success and error output, and discard setup output
  before asserting command output.
- Assert the stored `Expense` values and exit codes, not implementation details.
- Add a regression case that would fail without the change, including empty,
  invalid, and not-found behavior where relevant.
- Run `pytest`, `ruff check .`, and `ruff format --check .` after test changes.
