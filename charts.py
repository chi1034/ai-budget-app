# charts.py

import matplotlib.pyplot as plt

def plot_expenses(expenses):
    categories = list(expenses.keys())
    values = list(expenses.values())
    
    plt.figure(figsize=(6,6))
    plt.pie(values, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Breakdown")
    plt.savefig("expenses_chart.png")  # saves chart as an image file
