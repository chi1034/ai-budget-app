import os
import pandas as pd
import joblib
from flask import Flask, render_template, request
from budget_tips import generate_tips
from charts import plot_expenses

MODEL_PATH = os.path.join("models", "overspend_model.joblib")

app = Flask(__name__)
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        income = float(request.form.get("income", 0))
        expenses = {
            "food": float(request.form.get("food", 0)),
            "transport": float(request.form.get("transport", 0)),
            "rent": float(request.form.get("rent", 0)),
            "utilities": float(request.form.get("utilities", 0)),
            "education": float(request.form.get("education", 0)),
        }

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

        # Generate chart (saved in static folder)
        plot_expenses(expenses)
        chart_path = os.path.join(app.static_folder, "expenses_chart.png")
        if os.path.exists("expenses_chart.png"):
            os.replace("expenses_chart.png", chart_path)

        result = {
            "income": income,
            "expenses": expenses,
            "savings": savings,
            "overspend_category": overspend_category,
            "advice": tips
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
