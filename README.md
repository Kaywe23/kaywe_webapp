# DJ KAYWE Webapp

Modern full-stack web app for DJ KAYWE with Vue + Tailwind frontend and FastAPI backend.

## Stack

- **Frontend:** Vue 3, Vite 7, Tailwind CSS 4
- **Backend:** FastAPI, Uvicorn, Pydantic Settings
- **Python package manager:** `uv`
- **Container orchestration:** Docker Compose

## Project structure

```text
.
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── api.py
│   ├── pyproject.toml
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   │   └── main.css
│   │   ├── components/
│   │   │   ├── BookingCard.vue
│   │   │   ├── HeroSection.vue
│   │   │   ├── Navbar.vue
│   │   │   └── SetListCard.vue
│   │   ├── App.vue
│   │   └── main.js
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile
└── docker-compose.yml
```

## Local development

### Backend (uv)

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

## Docker Compose

```bash
docker compose up --build
```

- Frontend: http://localhost:5173
- Backend API docs: http://localhost:8000/docs

## VS Code: Deployen und Testen (Schritt-für-Schritt)

### 1) Voraussetzungen installieren

- **VS Code**
- **Docker Desktop** (inkl. `docker compose`)
- **Node.js 22+** und **npm**
- **Python 3.12+**
- **uv** (`pip install uv`)

### 2) Projekt in VS Code öffnen

```bash
git clone <DEIN-REPO-URL>
cd kaywe_webapp
code .
```

### 3) Empfohlene VS Code Extensions

- Vue - Official (`Vue.volar`)
- Tailwind CSS IntelliSense
- Python (ms-python.python)
- Docker

### 4) Lokal starten (ohne Docker)

Öffne in VS Code **zwei Terminals**.

**Terminal 1 (Backend):**
```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

Danach im Browser öffnen:
- Frontend: `http://localhost:5173`
- Backend Swagger: `http://localhost:8000/docs`
- Healthcheck: `http://localhost:8000/api/health`

### 5) Mit Docker deployen/testen

Im VS Code Terminal im Projekt-Root:

```bash
docker compose up --build
```

Danach:
- Frontend: `http://localhost:5173`
- Backend: `http://localhost:8000`
- API-Doku: `http://localhost:8000/docs`

Stoppen mit:

```bash
docker compose down
```

### 6) Typischer Test-Workflow in VS Code

1. Frontend anpassen (`frontend/src/...`)
2. Backend anpassen (`backend/app/...`)
3. API-Endpunkt testen über Swagger (`/docs`)
4. UI im Browser responsive testen (DevTools)
5. Optional finaler Docker-Test mit `docker compose up --build`

### 7) Häufige Fehler und Lösungen

- **`npm install` Fehler**: Prüfe Proxy/Firewall und npm Registry Zugriff.
- **`docker: command not found`**: Docker Desktop installieren/starten.
- **Port bereits belegt**: Prozesse auf `5173` oder `8000` stoppen oder Ports anpassen.
