def build_budget_prompt(income, expenses: dict, goal: str, persona: str = "student"):
    return f"""You are a personal-finance assistant for a {persona}.
Given the user's monthly income, categorized expenses, and savings goal,
produce:
1) A concise budget summary
2) Top 3 spending insights (with % of income)
3) 3–5 actionable recommendations
4) A 2–3 sentence concluding note

Income (monthly): {income}
Expenses (monthly): {expenses}
Savings goal: {goal}
"""
