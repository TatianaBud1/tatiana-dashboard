from flask import Flask, render_template, jsonify
from generate_data import get_weather
import os, json

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/weather")
def api_weather():
    weather_data, latency_list = get_weather()
    return jsonify({
        "weather": weather_data,
        "latency": latency_list
    })

@app.route("/api/connectivity")
def connectivity():
    if os.path.exists("data/connectivity.json"):
        with open("data/connectivity.json") as f:
            return jsonify(json.load(f))
    return jsonify({"error": "no connectivity data"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
