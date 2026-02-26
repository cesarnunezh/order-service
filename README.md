# Order service

FastAPI service for the e-commerce platform.

## Local Development
- Create venv and install deps with `uv`.
- Run: `uvicorn src.main:app --reload`
- Test: `pytest`

## Docker
- Build: `docker build -t order-service:local .`
- Run: `docker run -p 8000:8000 order-service:local`

## Git Flow
See `docs/git-flow.md`.

## Jenkins
See Jenkinsfile for CI pipeline.

## Design Decisions
See docs/decisions.md.
