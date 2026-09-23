# PulseOps

PulseOps is a web service monitoring application under development.
Its goal is to track availability, response times, and health check history.

## Current status

A first FastAPI endpoint is available: `GET /health` returns `{"status":"ok"}`.
It confirms that the API responds; it does not check a database or other services.
The database and dashboard are not implemented yet.

## Planned stack

- Backend: Python, FastAPI, SQLAlchemy, PostgreSQL
- Frontend: React, TypeScript, Vite, Tailwind CSS
- Infrastructure: Docker Compose, GitHub Actions
- Observability after the MVP: Prometheus and Grafana

## Repository layout

```text
backend/     Python API and dependencies
frontend/    React dashboard (to be implemented)
```

## Local development

The backend currently uses Python 3.14. Run these commands from the repository root:

```bash
python3 -m venv backend/.venv
source backend/.venv/bin/activate
python -m pip install -r backend/requirements.txt
fastapi dev backend/main.py
```

On Ubuntu, if environment creation fails because `ensurepip` is missing,
install the venv package matching your Python version (for example,
`sudo apt install python3.14-venv`) and retry.

In a second terminal:

```bash
curl -i http://127.0.0.1:8000/health
```

Expected response: HTTP `200 OK` with the JSON body `{"status":"ok"}`.
Interactive API documentation is available at <http://127.0.0.1:8000/docs>.
Stop the server with `Ctrl+C`.

The virtual environment is created once. Activate it again in each new terminal
used to run the backend. Dependencies are pinned in `backend/requirements.txt`
from the current Linux development environment.

Next milestone: PostgreSQL through Docker Compose and a first Service model.

## Development workflow

Keep `main` working and use a short-lived branch for each focused change:

- `chore/project-setup`
- `feat/health-endpoint`
- `feat/postgres-setup`
- `fix/<short-description>`

Open a pull request against `main`, describe the change and how it was checked,
review the diff, then squash and merge. Delete the merged branch and start the
next branch from an updated `main`.

Use descriptive commit messages, for example:

```text
chore(repo): initialize project structure
feat(api): add health endpoint
```

Commit environment variable examples with dummy values in `.env.example`.
Keep real credentials, `.env` files, virtual environments, and generated
dependencies out of Git.
