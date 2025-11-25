# budget_tips.py

def generate_tips(income, expenses, overspend_category=None):
    tips = []
    total = sum(expenses.values())
    savings = income - total

    # Contextual tip from model
    if overspend_category:
        tips.append(f"Your spending suggests {overspend_category} is likely overspending. Focus on that category first.")

    # Ratio-based nudges
    for cat, ratio in [
        ("food", 0.35),
        ("transport", 0.25),
        ("rent", 0.45),
        ("utilities", 0.15),
        ("education", 0.20)
    ]:
        if expenses.get(cat, 0) > ratio * income:
            tips.append(f"{cat.capitalize()} exceeds {int(ratio*100)}% of income. Consider setting a cap and tracking weekly.")

    # Savings status
    if savings < 0:
        tips.append("You're overspending overall. Try a 10% cut across non-essentials for the next month.")
    else:
        tips.append(f"Good job! Estimated monthly savings: {savings}.")

    return tips, savings
