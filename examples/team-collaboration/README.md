# Team Collaboration Example

This example shows how a small team (3-5 people) can share project rules while keeping personal memories private.

## Structure

```
team-project/
├── .lobster-anti-laziness-skill/           # Shared team memory
│   ├── rules/
│   │   ├── backend.md
│   │   ├── frontend.md
│   │   └── devops.md
│   └── shared-decisions.md
├── MEMORY-alex.md          # Alex's personal memory
├── MEMORY-sam.md           # Sam's personal memory
├── MEMORY-jordan.md        # Jordan's personal memory
└── SOUL.md                 # Team-wide AI identity
```

## Shared Rules (Git-Tracked)

`rules/backend.md`:
```markdown
# Backend Rules

## Tech Stack
- Python 3.11
- FastAPI
- PostgreSQL 15
- SQLAlchemy 2.0

## Standards
- All endpoints must have OpenAPI docs
- All functions must have type hints
- Test coverage minimum 80%

## Environment
- Database URL: postgresql://localhost:5432/teamdb
- Run: `uvicorn main:app --reload`
```

## Personal Memories (Git-Ignored)

`MEMORY-alex.md`:
```markdown
## Alex's Preferences
- [preference] Prefers async/await over threading
- [preference] Likes detailed docstrings

## Alex's Todos
- [TODO] Refactor auth module
```

`MEMORY-sam.md`:
```markdown
## Sam's Preferences
- [preference] Prefers functional programming style
- [preference] Likes minimal docstrings

## Sam's Todos
- [TODO] Optimize database queries
```

## Workflow

1. **Shared rules** are committed to Git
   - Team agrees on standards
   - Everyone gets updates via `git pull`

2. **Personal memories** are .gitignored
   - Each person's preferences stay private
   - No merge conflicts on personal todos

3. **AI loads both**:
   - Shared rules for project context
   - Personal memory for individual preferences

## Conflict Resolution

When personal preference conflicts with team rule:
```
Team rule: "Use 4 spaces for indentation"
Alex's preference: "Use 2 spaces"

Resolution: Team rule wins for shared code.
            Alex can use 2 spaces for personal projects.
```

## Setup

```bash
# Clone repo
git clone https://github.com/team/project.git
cd project

# Copy your personal memory template
cp MEMORY-template.md MEMORY-$(whoami).md

# AI reads both shared rules and your personal memory
```

## Benefits

- ✅ Consistent project standards across team
- ✅ Personal preferences respected for individual work
- ✅ No memory pollution from teammates' habits
- ✅ Git provides audit trail for shared rules
