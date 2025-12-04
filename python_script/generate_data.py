import json
import random
from datetime import datetime
import time

while True:
    data = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "cpu": random.randint(10, 90),
        "ram": random.randint(20, 80),
        "disk": random.randint(5, 90)
    }
    print(json.dumps(data))
    time.sleep(20)
