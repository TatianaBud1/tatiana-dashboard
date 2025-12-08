# Tatiana Dashboard – Proiect Final DevOps

## 📌 Descriere

Acest proiect a fost realizat pentru **examenul de absolvire – Proba Practică DevOps**. Scopul lui este monitorizarea vremii din **Corjeuti, Moldova**, prezentată într-un dashboard modern, generat de un serviciu Python/Flask, plus un script Bash care afișează informații în terminal.

Proiectul include:

* **Script Bash** (`monitor.sh`) – colectează și afișează resursele sistemului.
* **Aplicație Python/Flask** (`app.py`) – generează dashboard cu grafice meteo.
* **Containerizare completă în Docker**.
* **Orchestrare cu Docker Compose**.

---

## 🗂 Structura proiectului

```
ProiectResurse/
│
├─ bash_script/
│   └─ monitor.sh
│
├─ python_script/
│   ├─ app.py
│   ├─ generate_data.py
│   └─ static/
│       └─ icons/   (iconițe meteo)
│
├─ index.html
│
├─ Dockerfile.bash
├─ Dockerfile.python
├─ docker-compose.yml
└─ README.md
```

---

## 🧰 Cerințe

* **Docker**
* **Docker Compose**
* Python 3.x (opțional pentru rulare locală fără Docker)

---

## 🔽 Instalare

### 1️⃣ Clonarea proiectului

```bash
git clone https://github.com/<username>/tatiana-dashboard-devops.git
cd tatiana-dashboard-devops/docker
```

---

## 🏗️ Construire & Rulare

### 2️⃣ Construirea containerelor

```bash
docker-compose build
```

### 3️⃣ Pornirea aplicației

```bash
docker-compose up
```

Servicii porniți:

* **Bash Service** → afișează în terminal datele monitorizate.
* **Python Flask Dashboard** → disponibil pe:
  👉 [http://localhost:5000](http://localhost:5000)

---

## 🛑 Oprirea serviciilor

```bash
docker-compose down
```

---

## 🧪 Rulare locală fără Docker (opțional)

```bash
cd python_script
pip install -r requirements.txt
python3 app.py
```

Dashboard-ul devine accesibil la:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔍 Testare

### Verificare loguri container Bash

```bash
docker logs tatiana_bash
```

### Verificare dashboard

* Graficele să fie animate.
* Iconițele meteo să fie încărcate corect.
* Datele să fie generate prin `generate_data.py`.

---

## 🐳 Docker Compose – Arhitectură

* **Serviciu Bash** rulează periodic scriptul `monitor.sh`.
* **Serviciu Python** rulează serverul Flask.
* Volumele sunt configurate pentru acces la fișiere.

---

## 📈 Funcționalități principale

* Afișare temperatură zilnică pe 7 zile.
* Grafic animat cu Chart.js.
* Iconițe dinamice în funcție de starea vremii.
* Actualizare automată a datelor.
* Design curat și ușor de folosit.

---

## 🚀 Extensii posibile

* Adăugare API real OpenWeatherMap.
* Integrare CI/CD (GitHub Actions).


---

## 🧬 CI/CD – Integrare Automatizată

## 🖼️ Diagramă Arhitectură CI/CD

```
                       ┌───────────────────────────┐
                       │        Developer          │
                       │        (Tatiana)          │
                       └──────────────┬────────────┘
                                      │  Push / PR
                                      ▼
                    ┌───────────────────────────────────┐
                    │       GitHub Repository           │
                    │  (Cod + Dockerfile + Compose)     │
                    └──────────────────┬────────────────┘
                                       │ Trigger
                                       ▼
            ┌─────────────────────────────────────────────────────┐
            │                GitHub Actions CI                    │
            │  .github/workflows/docker-ci.yml                   │
            │                                                     │
            │ - Checkout repository                               │
            │ - Build Docker images (bash + python)               │
            │ - Validate docker-compose.yml                       │
            │ - Rulează testele                                   │
            └──────────────────┬──────────────────────────────────┘
                               │  If CI Success
                               ▼
            ┌─────────────────────────────────────────────────────┐
            │                GitHub Actions CD                    │
            │  .github/workflows/docker-cd.yml                   │
            │                                                     │
            │ - Login to GHCR                                     │
            │ - Tag + build imagini                               │
            │ - Push imagini la:                                  │
            │   ghcr.io/<owner>/tatiana-dashboard                 │
            │   ghcr.io/<owner>/tatiana-bash                      │
            └───────────────┬─────────────────────────────────────┘
                            │ Deploy complet
                            ▼
           ┌──────────────────────────────────────────────────────┐
           │      GitHub Container Registry (GHCR)               │
           │   Stochează imaginile Docker                        │
           │   pentru deploy ulterior pe server / cloud          │
           └──────────────────────────────────────────────────────┘
```

---

(GitHub Actions)
Pentru a automatiza procesul de build și testare al proiectului, este inclus un workflow GitHub Actions.

### 📁 Fișier: `.github/workflows/docker-ci.yml`

Acest pipeline execută:

* verificarea codului
* build automat pentru imaginile Docker
* testarea aplicației Flask
* validarea fișierelor `docker-compose`

### 🔄 Fluxul CI/CD

1. **Trigger automat** la fiecare `push` sau `pull request` pe branch-ul `main`.
2. Acțiunile rulează pe runner Ubuntu.
3. Se construiesc ambele imagini Docker:

   * `bash-service`
   * `python-dashboard`
4. Dacă build-ul reușește → pipeline marcat ca *success*.
5. Pipeline pregătit pentru extensie CD (deploy pe AWS / Docker Hub).

### 📝 Exemplu workflow

```yaml
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
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2

    - name: Build Bash Service
      run: |
        docker build -f Dockerfile.bash -t tatiana-bash:latest .

    - name: Build Python Dashboard
      run: |
        docker build -f Dockerfile.python -t tatiana-dashboard:latest .

    - name: Validate docker-compose.yml
      run: docker compose config
```

---

## 🚀 CD – Deploy automat pe GitHub (GitHub Container Registry)

Pentru a finaliza pipeline-ul DevOps, proiectul include un sistem de **Continuous Deployment (CD)** folosind **GitHub Container Registry (GHCR)**.

Acest sistem permite:

* Build automat al imaginilor Docker
* Împingerea lor în **GitHub Container Registry**
* Folosirea imaginilor oriunde (Docker Desktop, server, cloud)

---

## 🧩 Cerințe pentru Deploy pe GitHub (GHCR)

1. În secțiunea **GitHub → Settings → Developer settings → Personal Access Tokens**:

   * Creezi un token cu permisiuni:

     * `write:packages`
     * `read:packages`
     * `delete:packages`

2. În depozitul GitHub mergi la:
   **Settings → Secrets and variables → Actions → New repository secret**

   * Creezi secretul:

     * **GHCR_TOKEN** — tokenul generat

---

## 📁 Workflow CD: `.github/workflows/docker-cd.yml`

Pipeline-ul rulează după build (CI) și împinge imaginile în GHCR.

### 🔽 Exemplu workflow CD

```yaml
name: CD – Deploy to GHCR

on:
  push:
    branches: [ "main" ]

jobs:
  push-images:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Log in to GHCR
      uses: docker/login-action@v2
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.GHCR_TOKEN }}

    - name: Build Bash Service image
      run: |
        docker build -f Dockerfile.bash -t ghcr.io/${{ github.repository_owner }}/tatiana-bash:latest .

    - name: Build Python Dashboard image
      run: |
        docker build -f Dockerfile.python -t ghcr.io/${{ github.repository_owner }}/tatiana-dashboard:latest .

    - name: Push Bash Service image
      run: docker push ghcr.io/${{ github.repository_owner }}/tatiana-bash:latest

    - name: Push Python Dashboard image
      run: docker push ghcr.io/${{ github.repository_owner }}/tatiana-dashboard:latest
```

---

## 🎉 Cum folosești imaginile din GHCR

După ce pipeline-ul rulează, imaginile sunt publicate în GHCR și pot fi descărcate cu:

```bash
docker pull ghcr.io/<username>/tatiana-dashboard:latest
docker pull ghcr.io/<username>/tatiana-bash:latest
```

---

