import os
import pandas as pd
import joblib
from flask import Flask, request, jsonify
from budget_tips import generate_tips
from charts import plot_expenses

MODEL_PATH = os.path.join("models", "overspend_model.joblib")

app = Flask(__name__)
model = joblib.load(MODEL_PATH)   # load trained model

@app.route('/budget', methods=['POST'])
def budget_advice():
    data = request.json
    income = float(data.get('income', 0))
    expenses = data.get('expenses', {})

    # Ensure all categories exist
    for cat in ["food", "transport", "rent", "utilities", "education"]:
        expenses.setdefault(cat, 0.0)

    # Predict overspend category
    row = pd.DataFrame([{
        "income": income,
        "food": expenses["food"],
        "transport": expenses["transport"],
        "rent": expenses["rent"],
        "utilities": expenses["utilities"],
        "education": expenses["education"]
    }])
    overspend_category = model.predict(row)[0]

    # Generate tips + savings
    tips, savings = generate_tips(income, expenses, overspend_category)

    # Generate chart
    plot_expenses(expenses)

    return jsonify({
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "overspend_category": overspend_category,
        "advice": tips,
        "chart": "expenses_chart.png"
    })

if __name__ == '__main__':
    app.run(debug=True)
