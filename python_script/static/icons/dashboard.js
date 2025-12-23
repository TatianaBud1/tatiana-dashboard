const canvas = document.getElementById("latencyChart");
const ctx = canvas.getContext("2d");

function drawChart(data) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.beginPath();
    ctx.moveTo(10, 190);

    data.forEach((val, i) => {
        const x = 10 + i * 35;
        const y = 190 - val;
        ctx.lineTo(x, y);
    });

    ctx.strokeStyle = "#007bff";
    ctx.stroke();
}

async function loadConnectivity() {
    const res = await fetch("/api/connectivity");
    const data = await res.json();

    drawChart(data.latency_history);

    const alert = document.getElementById("alert");
    if (data.internet.quality === "DOWN") {
        alert.innerHTML = "🔴 INTERNET DOWN!";
        alert.style.color = "red";
    } else if (data.internet.quality === "WARNING") {
        alert.innerHTML = "🟡 Internet instabil";
        alert.style.color = "orange";
    } else {
        alert.innerHTML = "🟢 Internet OK";
        alert.style.color = "green";
    }
}

setInterval(loadConnectivity, 5000);
loadConnectivity();
