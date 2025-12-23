# Tatiana Dashboard – Proiect Final DevOps

## 📌 Descriere

Acest proiect a fost realizat pentru **examenul de absolvire – Proba Practică DevOps**. Scopul lui este monitorizarea vremii din **Corjeuți, Moldova**, prezentată într-un dashboard modern, generat de un serviciu Python/Flask, plus un script Bash care afișează informații în terminal.

Proiectul include:

* **Script Bash** (`monitor.sh`) – monitorizează conexiunea la internet și latența.
* **Aplicație Python/Flask** (`app.py`) – generează dashboard cu grafice meteo și latency.
* **Containerizare completă în Docker**.
* **Orchestrare cu Docker Compose**.

---

## 🗂 Structura proiectului

Proiect_ITSchool/
│
├─ bash_script/
│ └─ monitor.sh
│
├─ python_script/
│ ├─ app.py
│ ├─ generate_data.py
│ ├─ static/
│ │ └─ icons/ (iconițe meteo)
│ └─ templates/
│ └─ dashboard.html
│
├─ Dockerfile.bash
├─ Dockerfile.python
├─ docker-compose.yml
├─ README.md
└─ .gitignore

yaml
Копировать код

---

## 🧰 Cerințe

* **Docker**
* **Docker Compose**
* Python 3.x (opțional pentru rulare locală fără Docker)

### 1️⃣ Clonarea proiectului

```bash
git clone https://github.com/<username>/tatiana-dashboard-devops.git
cd tatiana-dashboard-devops/
🏗️ Construire & Rulare
2️⃣ Construirea containerelor
bash
Копировать код
docker-compose build
3️⃣ Pornirea aplicației
docker-compose up
Servicii porniți:

Bash Service → afișează în terminal datele monitorizate.

Python Flask Dashboard → disponibil pe:
👉 http://localhost:8000

🛑 Oprirea serviciilor
bash
Копировать код
docker-compose down
🧪 Rulare locală fără Docker (opțional)
bash
Копировать код
cd python_script
pip install -r requirements.txt
python3 app.py
Dashboard-ul devine accesibil la:
👉 http://127.0.0.1:8000

🔍 Testare
Verificare loguri container Bash
bash
Копировать код
docker logs tatiana_bash
Verificare dashboard
Graficele să fie animate.

Iconițele meteo să fie încărcate corect.

Datele să fie generate prin generate_data.py.

🐳 Docker Compose – Arhitectură
Serviciu Bash rulează periodic scriptul monitor.sh.

Serviciu Python rulează serverul Flask.

Volumele sunt configurate pentru acces la fișiere.

📈 Funcționalități principale
Afișare temperatură zilnică pe 7 zile.

Grafic animat cu Chart.js pentru date meteo și latency.

Iconițe dinamice în funcție de starea vremii.

Actualizare automată a datelor.

Design curat și ușor de folosit.

Monitorizare internet și latență în timp real.

🚀 Extensii posibile
Adăugare API real OpenWeatherMap (gratuit sau plătit).

Integrare CI/CD (GitHub Actions).

🧬 CI/CD – Integrare Automatizată
Diagramă Arhitectură CI/CD
scss
Копировать код
Developer (Tatiana) → GitHub Repository → GitHub Actions CI → Docker Build + Test → GHCR
Workflow CI: build automat imagini Docker, testează Flask și validate docker-compose.

Workflow CD: push imagini în GitHub Container Registry.

🧩 Cerințe pentru Deploy pe GHCR
Creezi un Personal Access Token cu permisiuni: write:packages, read:packages, delete:packages.

Adaugi secretul GHCR_TOKEN în repository la Settings → Secrets → Actions.

📁 Workflow CI Example: .github/workflows/docker-ci.yml
yaml
Copiere cod
name: CI DevOps Dashboard

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - uses: docker/setup-buildx-action@v2
      - run: docker build -f Dockerfile.bash -t tatiana-bash:latest .
      - run: docker build -f Dockerfile.python -t tatiana-dashboard:latest .
      - run: docker compose config
📁 Workflow CD Example: .github/workflows/docker-cd.yml
yaml
Копировать код
name: CD – Deploy to GHCR

on:
  push:
    branches: [ "main" ]

jobs:
  push-images:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - uses: docker/login-action@v2
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GHCR_TOKEN }}
      - run: docker build -f Dockerfile.bash -t ghcr.io/${{ github.repository_owner }}/tatiana-bash:latest .
      - run: docker build -f Dockerfile.python -t ghcr.io/${{ github.repository_owner }}/tatiana-dashboard:latest .
      - run: docker push ghcr.io/${{ github.repository_owner }}/tatiana-bash:latest
      - run: docker push ghcr.io/${{ github.repository_owner }}/tatiana-dashboard:latest
🎉 Utilizare imagini din GHCR
bash
Копировать код
docker pull ghcr.io/<username>/tatiana-dashboard:latest
docker pull ghcr.io/<username>/tatiana-bash:latest