# API (Backend)

Python + FastAPI backend for the AI Travel Planner.

Generates itineraries with the Gemini API, fetches places from Geoapify,
and persists data in Supabase (PostgreSQL).

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) for dependency management

## Setup

From `apps/api`:

```bash
uv sync                 # creates .venv and installs locked dependencies
cp .env.example .env    # optional: override default settings
```

## Run locally

```bash
uv run uvicorn app.main:app --reload
```

Or activate the virtualenv first and run uvicorn directly:

```bash
source .venv/bin/activate
uvicorn app.main:app --reload
```

- API: http://localhost:8000
- Health check: http://localhost:8000/health
- OpenAPI docs: http://localhost:8000/docs

## Run tests

```bash
uv run pytest
```

## Project structure

```
apps/api/
├── app/
│   ├── main.py            # App factory, router + exception handler registration
│   ├── api/
│   │   ├── router.py      # Aggregates all route modules
│   │   └── routes/        # HTTP endpoints (thin, delegate to services)
│   ├── core/
│   │   ├── config.py      # Settings (pydantic-settings, reads env / .env)
│   │   └── exceptions.py  # AppError + global exception handlers
│   ├── schemas/           # Pydantic request/response models
│   └── services/          # Business logic
├── tests/                 # pytest suite (TestClient fixture in conftest.py)
├── pyproject.toml
└── uv.lock
```

## Managing dependencies

```bash
uv add <package>          # runtime dependency
uv add --dev <package>    # dev/test dependency
```
