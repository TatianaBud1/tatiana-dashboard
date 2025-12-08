from datetime import datetime, timedelta
import random

def generate_week_data():
    forecast = []
    today = datetime.now()

    # posibile icon-uri: 01d = soare, 02d = soare cu câțiva nori, 03d = nori, 09d = ploaie, 10d = ploaie ușoară
    icons = ["01d", "02d", "03d", "09d", "10d"]

    for i in range(7):
        day = today + timedelta(days=i)
        forecast.append({
            "date": day.strftime("%Y-%m-%d"),
            "temp": random.randint(-5, 15),
            "humidity": random.randint(50, 100),
            "precipitation": random.randint(0, 10),
            "wind": round(random.uniform(0.5, 5.0), 1),
            "icon": random.choice(icons)
        })
    
    return forecast

# test rapid
if __name__ == "__main__":
    week = generate_week_data()
    for day in week:
        print(day)
