import requests
import json
from datetime import datetime
import time

# 🔑 Cheia ta API gratuită
API_KEY = "f57f791c17fe457088074df87ed9103f"

# Locatia Corjeuți, Moldova
LAT = "47.8042"
LON = "27.8553"

# Endpoint gratuit (forecast 5 zile, 3h)
URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&units=metric&appid={API_KEY}"

# Mapare iconițe meteo
ICON_MAP = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧",
    "Snow": "❄️",
    "Thunderstorm": "⛈",
    "Drizzle": "🌦",
    "Mist": "🌫",
}

def get_weather():
    response = requests.get(URL)
    data = response.json()

    days = {}
    latency_list = []

    for item in data["list"]:
        date = item["dt_txt"].split(" ")[0]
        if date not in days:
            # --- măsurare latență API pentru fiecare zi ---
            start = time.time()
            _ = requests.get(URL)  # simulăm request separat
            latency_ms = round((time.time() - start) * 1000, 2)
            latency_list.append(latency_ms)
            # --- end latency ---

            weather_main = item["weather"][0]["main"]
            days[date] = {
                "day": datetime.strptime(date, "%Y-%m-%d").strftime("%A"),
                "temp": round(item["main"]["temp"], 1),
                "humidity": item["main"]["humidity"],
                "wind": round(item["wind"]["speed"], 1),
                "icon": ICON_MAP.get(weather_main, "🌤"),
                "latency_ms": latency_ms
            }
        if len(days) == 7:
            break

    # Scriem datele într-un JSON temporar
    with open("/tmp/weather.json", "w") as f:
        json.dump(list(days.values()), f, indent=2)

    return list(days.values()), latency_list

# Test rapid
if __name__ == "__main__":
    weather_data, latency = get_weather()
    print("✅ Weather JSON generat în /tmp/weather.json")
    for day in weather_data:
        print(day)
