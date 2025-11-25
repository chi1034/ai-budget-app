# test_client.py
import requests

url = "http://127.0.0.1:5000/budget"
data = {
    "income": 1000,
    "expenses": {
        "food": 500,
        "transport": 400,
        "rent": 300,
        "utilities": 100,
        "education": 50
    }
}

# Send POST request
res = requests.post(url, json=data)
response_json = res.json()
print("API Response:", response_json)

# Fetch the chart image
chart_url = "http://127.0.0.1:5000" + response_json["chart"]
chart_res = requests.get(chart_url)

if chart_res.status_code == 200:
    with open("downloaded_chart.png", "wb") as f:
        f.write(chart_res.content)
    print("Chart image saved as downloaded_chart.png")
else:
    print("Failed to fetch chart image:", chart_res.status_code)
