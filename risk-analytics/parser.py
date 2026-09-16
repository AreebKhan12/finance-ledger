# risk-analytics/parser.py

def analyze_raw_transactions(transactions: list[dict]) -> dict:
    """
    Takes a list of transaction dictionaries and calculates core cash flow totals.
    Each transaction dictionary looks like:
    {"date": "2026-09-01", "description": "Metro", "amount": 64.20, "category": "Groceries"}
    """
    total_income = 0.0
    total_spend = 0.0
    discretionary_spend = 0.0

    # Non-essential spending categories
    discretionary_categories = {"Dining", "Entertainment", "Shopping"}

    # TODO: Loop through 'transactions'
    # 1. If amount is negative, add its absolute value to total_income
    # 2. If amount is positive:
    #      a. Add to total_spend
    #      b. If the category is in discretionary_categories, add to discretionary_spend

    # TODO: Calculate net_savings (income - spend)

    return {
        "total_income": round(total_income, 2),
        "total_spend": round(total_spend, 2),
        "discretionary_spend": round(discretionary_spend, 2),
        "net_savings": 0.0  # replace with your calculation
    }


if __name__ == "__main__":
    # Test data
    sample_data = [
        {"description": "Campus Bookstore", "amount": 142.50, "category": "Education"},
        {"description": "Metro Grocery",    "amount": 64.20,  "category": "Groceries"},
        {"description": "Uber Eats",        "amount": 28.75,  "category": "Dining"},
        {"description": "Payroll Deposit",  "amount": -650.00, "category": "Income"},
        {"description": "Spotify Student",  "amount": 5.99,   "category": "Entertainment"},
        {"description": "TTC Transit",      "amount": 128.15, "category": "Transit"},
    ]

    results = analyze_raw_transactions(sample_data)
    print("Execution Result:", results)