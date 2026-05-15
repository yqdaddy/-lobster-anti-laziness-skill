# Multi-Project Setup Example

This example shows how to manage multiple projects with 龙虾超记忆防偷懒技能.

## Structure

```
workspace/
├── SOUL.md                 # Global identity
├── MEMORY.md               # Global memory (todos, preferences)
├── memory/                 # Daily logs
├── rules/                  # Project-specific rules
│   ├── backend-api.md
│   ├── mobile-app.md
│   └── data-pipeline.md
└── projects/               # Project directories
    ├── backend-api/
    ├── mobile-app/
    └── data-pipeline/
```

## Key Insight

MEMORY.md tracks **cross-project** concerns:
- Global todos ("Update all READMEs")
- User preferences ("Prefer TypeScript")
- Shared pitfalls ("Always check Node version")

Project rules track **project-specific** concerns:
- Backend API: "Use FastAPI, PostgreSQL"
- Mobile App: "Use Flutter, Firebase"
- Data Pipeline: "Use Airflow, BigQuery"

## Usage

When working on backend API:
```
AI: [Reads MEMORY.md] "You have 3 global todos..."
AI: [Loads rules/backend-api.md] "Backend uses FastAPI..."
```

When switching to mobile app:
```
AI: [MEMORY.md already loaded] "Global context known..."
AI: [Loads rules/mobile-app.md] "Mobile uses Flutter..."
```

This prevents MEMORY.md from becoming a massive file while keeping project context available.
