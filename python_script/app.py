from flask import Flask, render_template
from weather import get_week_forecast
from generate_data import generate_week_data

app = Flask(__name__)

@app.route("/")
def dashboard():
    forecast = get_week_forecast()
    if not forecast:
        forecast = generate_week_data()  # fallback dacă nu merge API-ul
    return render_template("index.html", forecast=forecast)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
