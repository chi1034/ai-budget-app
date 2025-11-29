# AI Budget Advisor

AI Budget Advisor is a smart web application designed to help you take control of your finances. By analyzing your income and expenses, it uses a machine learning model to predict potential overspending categories and provides personalized, actionable advice to help you save more.

## Features

-   **Expense Analysis**: Input your monthly income and expenses across various categories (Food, Transport, Rent, Utilities, Education).
-   **AI Predictions**: Uses a pre-trained Machine Learning model to identify which category you are most likely to overspend in.
-   **Visual Insights**: Generates a dynamic pie chart to visualize your expense breakdown.
-   **Smart Tips**: Receives tailored budgeting advice and savings estimates based on your spending habits.
-   **Downloadable Reports**: Download your advice and charts for offline reference.

## Tech Stack

-   **Backend**: Python, Flask
-   **Data Processing**: Pandas
-   **Machine Learning**: Scikit-learn, Joblib
-   **Visualization**: Matplotlib
-   **Frontend**: HTML, CSS (Jinja2 templates)

## Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone https://github.com/chi1034/ai-budget-app.git
    cd ai-budget-app
    ```

2.  **Set up a virtual environment** (recommended):
    *   Windows:
        ```powershell
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application**:
    ```bash
    python app.py
    ```

2.  **Open your browser**:
    Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

3.  **Get Advice**:
    -   Enter your monthly income.
    -   Fill in your estimated expenses for each category.
    -   Click "Get Advice" to see your results, charts, and AI-driven recommendations.

## Project Structure

```
ai_budget_app/
├── app.py                 # Main Flask application
├── budget_tips.py         # Logic for generating advice
├── charts.py              # Logic for generating charts
├── requirements.txt       # Project dependencies
├── models/
│   └── overspend_model.joblib  # Pre-trained ML model
├── static/
│   └── ...                # Static assets (CSS, images)
└── templates/
    └── index.html         # HTML template
```

## License

This project is open source and available under the [MIT License](LICENSE).
