"""The ``total`` command: sum recorded expenses."""

from __future__ import annotations

from ..money import format_amount

NAME = "total"
HELP = "Total expenses, optionally filtered by category"


def add_parser(subparsers) -> None:
    parser = subparsers.add_parser(NAME, help=HELP)
    parser.add_argument(
        "--category",
        default=None,
        help="Only total expenses in this category",
    )


def handle(args, store) -> int:
    total_cents = sum(
        expense.amount_cents
        for expense in store.load()
        if args.category is None or expense.category == args.category
    )
    print(format_amount(total_cents))
    return 0
