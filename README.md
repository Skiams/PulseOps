# PulseOps

PulseOps is a web service monitoring application under development.
Its goal is to track availability, response times, and health check history.

## Current status

Repository setup only. The API, database, and dashboard are not implemented yet.

## Planned stack

- Backend: Python, FastAPI, SQLAlchemy, PostgreSQL
- Frontend: React, TypeScript, Vite, Tailwind CSS
- Infrastructure: Docker Compose, GitHub Actions
- Observability after the MVP: Prometheus and Grafana

## Repository layout

```text
backend/     Python API (to be implemented)
frontend/    React dashboard (to be implemented)
AGENTS.md    Project scope and learning workflow
```

## Local development

Setup and run commands will be added as each component becomes available.
The first milestone is a FastAPI application with `GET /health`, a local
PostgreSQL database running through Docker Compose, and a first Service model.

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
