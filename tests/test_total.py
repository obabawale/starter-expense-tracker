from expense_tracker.cli import main
from expense_tracker.commands import add
from tests.conftest import args, make_store


def _seed(store):
    add.handle(args(amount="12.50", category="groceries", date="2026-01-01", note=""), store)
    add.handle(args(amount="40.00", category="travel", date="2026-01-02", note=""), store)
    add.handle(args(amount="10.00", category="groceries", date="2026-01-03", note=""), store)


def test_total_all(tmp_path, monkeypatch, capsys):
    store = make_store(tmp_path)
    _seed(store)
    capsys.readouterr()
    monkeypatch.setenv("EXPENSE_TRACKER_DATA", str(tmp_path / "expenses.json"))

    assert main(["total"]) == 0
    assert capsys.readouterr().out == "$62.50\n"


def test_total_empty(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("EXPENSE_TRACKER_DATA", str(tmp_path / "expenses.json"))

    assert main(["total"]) == 0
    assert capsys.readouterr().out == "$0.00\n"


def test_total_filtered_by_category(tmp_path, monkeypatch, capsys):
    store = make_store(tmp_path)
    _seed(store)
    capsys.readouterr()
    monkeypatch.setenv("EXPENSE_TRACKER_DATA", str(tmp_path / "expenses.json"))

    assert main(["total", "--category", "groceries"]) == 0
    assert capsys.readouterr().out == "$22.50\n"
    assert main(["total", "--category", "missing"]) == 0
    assert capsys.readouterr().out == "$0.00\n"
