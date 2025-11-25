:

🧠 AI Budget Advisor
AI Budget Advisor is a smart budgeting web app powered by machine learning. It helps users analyze their income and expenses, predicts overspending categories, and offers personalized financial advice — all with a visual chart and downloadable insights.

🚀 Features
Predicts which expense category you're likely to overspend on

Generates AI-powered budgeting tips

Calculates potential savings

Displays a chart of your expenses

Allows users to download the chart and advice as files

🛠️ Tech Stack
Python (Flask, Pandas, scikit-learn, Matplotlib)

HTML/CSS (Jinja templates)

Machine Learning (trained model with joblib)

📁 Project Structure
ai-budget-advisor/
│
├── app_frontend.py         # Flask frontend app
├── budget_tips.py          # AI advice generator
├── charts.py               # Expense chart generator
├── models/
│   └── overspend_model.joblib  # Trained ML model
├── static/
│   └── expenses_chart.png      # Chart image
├── templates/
│   └── index.html              # HTML form + results
├── requirements.txt        # Python dependencies
└── README.md               # Project overview


📬 Contact
Created by https://github.com/chi1034 — feel free to reach out for collaboration or feedback!