---
description: "Use when modifying the expense tracker CLI, argument parsing, command modules, or command registration."
applyTo:
  - "expense_tracker/cli.py"
  - "expense_tracker/__main__.py"
  - "expense_tracker/commands/**"
---

# CLI and Command Guidelines

- Keep argument parsing and dispatch in `expense_tracker/cli.py`; command modules
  should own only their parser and handler behavior.
- Each command module exposes `NAME`, `HELP`, `add_parser(subparsers)`, and
  `handle(args, store)`, returning an integer process exit code.
- Register every new command in `expense_tracker/commands/__init__.py`.
- Print user-facing success and validation messages to stdout consistently with
  the existing commands; return `1` for a handled error and `0` on success.
- Preserve the existing output formats for `list` and similar read-only commands.
- Parse and validate CLI input in the command handler; keep persistence behind
  the `Store` interface.
