# charts.py

import matplotlib.pyplot as plt

def plot_expenses(expenses, outfile="expenses_chart.png"):
    categories = list(expenses.keys())
    values = list(expenses.values())

    plt.figure(figsize=(6,6))
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.title("Expense Breakdown")
    plt.tight_layout()
    plt.savefig(outfile)
    plt.close()
    return outfile
