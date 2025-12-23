const canvas = document.getElementById("latencyChart");
const ctx = canvas.getContext("2d");

// zilele săptămânii în română
const zileSapt = ["Duminică", "Luni", "Marți", "Miercuri", "Joi", "Vineri", "Sâmbătă"];

const canvas = document.getElementById("latencyChart");
const ctx = canvas.getContext("2d");

function drawChart(latency_history) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Setăm dimensiuni și margini
    const chartHeight = 200;
    const chartWidth = canvas.width;
    const marginLeft = 40;
    const marginBottom = 40;
    const stepX = (chartWidth - marginLeft) / (latency_history.length);

    // Desenăm linia graficului
    ctx.beginPath();
    latency_history.forEach((val, i) => {
        const x = marginLeft + i * stepX;
        const y = chartHeight - val;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
    });
    ctx.strokeStyle = "#007bff";
    ctx.lineWidth = 2;
    ctx.stroke();

    // Etichetele axei X
    ctx.fillStyle = "#000";
    ctx.font = "12px Arial";
    latency_history.forEach((val, i) => {
        const x = marginLeft + i * stepX - 15; // ajustare
        const azi = new Date();
        azi.setDate(azi.getDate() - (latency_history.length - 1 - i));
        const zi = zileSapt[azi.getDay()];
        ctx.fillText(zi, x, chartHeight + 20);
    });
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

// refresh la fiecare 5 secunde
setInterval(loadConnectivity, 8000);
loadConnectivity();
