# charts.py

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_expenses(expenses, save_path="expenses_chart.png"):
    categories = list(expenses.keys())
    values = list(expenses.values())
    
    plt.figure(figsize=(6,6))
    plt.pie(values, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Breakdown")
    plt.savefig(save_path)
    plt.close()

