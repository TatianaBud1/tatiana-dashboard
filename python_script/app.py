from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():
    times = [f"{h}:00" for h in range(24)]
    cpu_values = [random.randint(10, 90) for _ in times]
    ram_values = [random.randint(20, 80) for _ in times]
    disk_values = [random.randint(5, 90) for _ in times]

    return render_template("index.html",
                           owner="Tatiana",
                           times=times,
                           cpu=cpu_values,
                           ram=ram_values,
                           disk=disk_values)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)