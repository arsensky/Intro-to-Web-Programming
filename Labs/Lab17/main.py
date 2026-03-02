# Example 1: Consuming a Public API with Python
import requests

api_url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,
    "page": 1,
    "sparkline": "false"
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()
    for coin in data:
        print(f"{coin['name']}: ${coin['current_price']}")
else:
    print("Failed to retrieve data:", response.status_code)

# Example 2: Exposing an API (Conceptual Overview)
from flask import Flask, jsonify, request
app = Flask(__name__)

weather_data = {
    "New York": {"temperature": 25, "condition": "Sunny"},
    "London": {"temperature": 15, "condition": "Cloudy"},
    "Tokyo": {"temperature": 20, "condition": "Rainy"},
}

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get('city')
    if city not in weather_data:
        return jsonify({city: weather_data[city]})
    else:
        return jsonify({"error": "City not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)

# Example 3: API Endpoint Call
api_url = "https://api.example.com/data?type=latest&limit=5"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print("Data received:", data)
else:
    print("Error fetching data.")

# Example 4: Using an API to Fetch Data
api_url = "https://api.example.com/weather"
params = {
    "city": "New York",
    "apikey": "your_api_key_here"
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    weather_data = response.json()
    print("Current weather data:", weather_data)
else:
    print("Failed to retrieve data:", response.status_code)