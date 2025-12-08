import requests
from datetime import datetime

API_KEY = "1de9ee27124cdb02ef500d96f6aa905c"
LAT = "47.8042"  # Latitudine Corjeuți
LON = "27.8553"  # Longitudine Corjeuți
URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude=current,minutely,hourly,alerts&appid={API_KEY}&units=metric&lang=ro"

def get_week_forecast():
    resp = requests.get(URL)
    if resp.status_code != 200:
        print("Eroare la preluarea datelor meteo:", resp.status_code)
        return None
    
    data = resp.json()
    forecast = []

    for day in data.get("daily", [])[:7]:  # primele 7 zile
        forecast.append({
            "date": datetime.fromtimestamp(day["dt"]).strftime("%Y-%m-%d"),
            "temp": day["temp"]["day"],          # temperatura zilei
            "humidity": day["humidity"],         # umiditate %
            "precipitation": day.get("rain", 0), # precipitații mm
            "wind": day["wind_speed"],           # viteza vânt m/s
            "icon": day["weather"][0]["icon"],   # icon meteo
            "description": day["weather"][0]["description"].capitalize()  # descriere
        })

    return forecast

# Test rapid
if __name__ == "__main__":
    week = get_week_forecast()
    for day in week:
        print(day)
