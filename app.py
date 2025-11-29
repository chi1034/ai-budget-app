import os
import pandas as pd
import joblib
from flask import Flask, request, jsonify, render_template
from budget_tips import generate_tips
from charts import plot_expenses

MODEL_PATH = os.path.join("models", "overspend_model.joblib")

app = Flask(__name__)
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        income = float(request.form.get("income", 0))
        expenses = {
            "food": float(request.form.get("food", 0)),
            "transport": float(request.form.get("transport", 0)),
            "rent": float(request.form.get("rent", 0)),
            "utilities": float(request.form.get("utilities", 0)),
            "education": float(request.form.get("education", 0))
        }

        row = pd.DataFrame([{
            "income": income,
            **expenses
        }])
        overspend_category = model.predict(row)[0]
        tips, savings = generate_tips(income, expenses, overspend_category)
        
        chart_path = os.path.join("static", "expenses_chart.png")
        plot_expenses(expenses, save_path=chart_path)

        result = {
            "income": income,
            "expenses": expenses,
            "savings": savings,
            "overspend_category": overspend_category,
            "advice": tips
        }
        return render_template("index.html", result=result)

    return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
