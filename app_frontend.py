import os
import pandas as pd
import joblib
from flask import Flask, request, render_template
from budget_tips import generate_tips
from charts import plot_expenses

# Define paths
MODEL_PATH = os.path.join("models", "overspend_model.joblib")
STATIC_FOLDER = "static"
TEMPLATE_FOLDER = "templates"

# Initialize Flask app
app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)

# Load trained ML model
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        # Get income and expenses from form
        income = float(request.form.get("income", 0))
        expenses = {
            "food": float(request.form.get("food", 0)),
            "transport": float(request.form.get("transport", 0)),
            "rent": float(request.form.get("rent", 0)),
            "utilities": float(request.form.get("utilities", 0)),
            "education": float(request.form.get("education", 0))
        }

        # Predict overspend category
        row = pd.DataFrame([{"income": income, **expenses}])
        overspend_category = model.predict(row)[0]

        # Generate tips and savings
        tips, savings = generate_tips(income, expenses, overspend_category)

        # Generate chart and move to static folder
        plot_expenses(expenses)
        chart_filename = "expenses_chart.png"
        if os.path.exists(chart_filename):
            os.replace(chart_filename, os.path.join(STATIC_FOLDER, chart_filename))

        # Prepare result for rendering
        result = {
            "income": income,
            "expenses": expenses,
            "savings": savings,
            "overspend_category": overspend_category,
            "advice": tips
        }

    return render_template("index.html", result=result)

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
