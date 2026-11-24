---
description: "Use when modifying expense models, money conversion, JSON persistence, dates, or data storage behavior."
applyTo:
  - "expense_tracker/models.py"
  - "expense_tracker/money.py"
  - "expense_tracker/storage.py"
---

# Data and Money Guidelines

- Represent monetary values as integer cents (`amount_cents`) throughout parsing,
  storage, arithmetic, and filtering.
- Keep float conversion and currency formatting separate from storage and totals.
- The `Expense` dataclass is the serialization boundary: keep `to_dict()` and
  `from_dict()` compatible with the JSON schema used in `expenses.json`.
- Store dates as validated `YYYY-MM-DD` strings, and validate user input with
  `datetime.date.fromisoformat()` or an equivalent exact parser.
- `Store` owns JSON loading and saving. Preserve missing-file behavior as an
  empty expense list and retain monotonic IDs through `next_id()`.
- Use `EXPENSE_TRACKER_DATA` or an injected `Store.path` in tests; do not mutate
  the repository's `expenses.json`.
