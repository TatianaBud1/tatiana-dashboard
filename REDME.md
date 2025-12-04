# Tatiana Dashboard - Proiect Final DevOps

## Descriere
Acest proiect este realizat pentru examenul de absolvire la proba practică DevOps.  
Scopul proiectului este să creeze și să afișeze un dashboard care monitorizează resursele sistemului (CPU, RAM, Disk), folosind două scripturi:

- **Bash** (`monitor.sh`) – colectează și printează resursele în terminal.
- **Python/Flask** (`app.py`) – creează un dashboard local cu grafice animate.

Ambele scripturi sunt containerizate și rulate prin Docker Compose.

---

## Structura proiectului

ProiectResurse/
│
├─ bash_script/
│ └─ monitor.sh
├─ python_script/
│ ├─ app.py
│ └─ generate_data.py
├─ dashboard/
│ └─ index.html
├─ docker/
│ ├─ Dockerfile.bash
│ ├─ Dockerfile.python
│ └─ docker-compose.yml
└─ README.md

yaml
Копировать код

---

## Instrucțiuni de instalare și rulare

### 1. Cerințe
- Docker
- Docker Compose
- Python 3.x (opțional pentru test local fără Docker)

### 2. Clonare proiect

```bash
git clone https://github.com/<username>/tatiana-dashboard-devops.git
cd tatiana-dashboard-devops/docker