from typing import Dict

def validate_expenses(expenses: Dict) -> Dict:
    if not isinstance(expenses, dict):
        raise ValueError("Expenses must be a dict of category -> amount")
    clean = {}
    for k, v in expenses.items():
        try:
            amt = float(v)
        except Exception as e:
            raise ValueError(f"Invalid amount for '{k}': {v}") from e
        if amt < 0:
            raise ValueError(f"Expense '{k}' cannot be negative")
        clean[str(k)] = amt
    return clean
