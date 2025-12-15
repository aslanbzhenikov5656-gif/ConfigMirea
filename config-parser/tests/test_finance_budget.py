from pathlib import Path
from .conftest import parse_cfg

def test_finance_budget(parser):
    text = Path("examples/finance_budget.cfg").read_text(encoding="utf-8")
    result = parse_cfg(parser, text)

    budget = result[0]
    assert budget[0] == "budget"

    income = budget[1]
    expenses = budget[2]
    reserve = budget[3]
    result_item = budget[4]

    assert income[1] == 150000
    assert expenses[1] == 40000
    assert reserve[1] == 10000
    assert result_item[1] == 100000
