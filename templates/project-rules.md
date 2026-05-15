# Project Rules — [Project Name]

> **Purpose**: Domain-specific rules for this project. Loaded on-demand when project is mentioned.
> **Location**: rules/[project-name].md

---

## Project Overview

- **Name**: [Project name]
- **Description**: [One-line description]
- **Status**: [Active / Paused / Maintenance]
- **Started**: YYYY-MM-DD

## Tech Stack

- **Language**: [e.g., Python 3.11]
- **Framework**: [e.g., FastAPI]
- **Database**: [e.g., PostgreSQL 15]
- **Key Dependencies**: [e.g., pydantic, sqlalchemy]

## Architecture Decisions

- **[decision]** [Decision] because [Rationale] `TTL: 365 days`
- **[decision]** [Decision] because [Rationale] `TTL: 365 days`

## Coding Standards

- [e.g., Use type hints everywhere]
- [e.g., Max function length: 50 lines]
- [e.g., Test coverage minimum: 80%]

## Environment Setup

```bash
# Clone
git clone [repo-url]
cd [project-name]

# Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
python main.py
```

## Key Paths

- **Source**: `./src/`
- **Tests**: `./tests/`
- **Config**: `./config/`
- **Docs**: `./docs/`

## Known Issues

- **[mistake]** [Issue] → [Workaround] `TTL: 90 days`

## API / Interface

- **Base URL**: `http://localhost:8000`
- **Auth**: [Bearer token / API key / None]
- **Key Endpoints**:
  - `GET /health` — Health check
  - `POST /api/v1/...` — [Description]

## Deployment

- **Platform**: [e.g., Docker, AWS, Vercel]
- **CI/CD**: [e.g., GitHub Actions]
- **Environment Variables**: [List critical ones]

---

> **Last Updated**: YYYY-MM-DD
> **Next Review**: YYYY-MM-DD
