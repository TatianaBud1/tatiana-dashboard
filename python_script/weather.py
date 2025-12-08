import requests
from datetime import datetime

API_KEY = "1de9ee27124cdb02ef500d96f6aa905c"
LAT = "47.8042"  # latitudine Corjeuți
LON = "27.8553"  # longitudine Corjeuți
URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude=current,minutely,hourly,alerts&appid={API_KEY}&units=metric&lang=ro"

def get_week_forecast():
    resp = requests.get(URL)
    if resp.status_code != 200:
        return None
    
    data = resp.json()
    forecast = []

    for day in data.get("daily", [])[:7]:  # primele 7 zile
        forecast.append({
            "date": datetime.fromtimestamp(day["dt"]).strftime("%Y-%m-%d"),
            "temp_day": day["temp"]["day"],
            "humidity": day["humidity"],
            "precipitation": day.get("rain", 0),
            "wind": day["wind_speed"],
            "icon": day["weather"][0]["icon"]  # aici preluăm icon-ul pentru fiecare zi
        })

    return forecast
