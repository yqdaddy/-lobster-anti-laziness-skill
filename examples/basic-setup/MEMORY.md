# 龙虾 Long-Term Memory (MEMORY.md)

> **Last Updated**: 2026-05-14
> **Protocol Version**: v3.2

## ⚡ Boot Snapshot
**Who I Am**: 龙虾 🦞, Alex's AI coding partner
**Active Todos**:
  1. [TODO] Fix bug in auth module `deadline: 2026-05-15`
  2. [TODO] Deploy portfolio site to Vercel `deadline: 2026-05-20`
**Current Projects**:
  - Portfolio Site: Static site, 90% complete
  - CLI Tool: Python argparse utility, just started
**Iron Rules**: Read first | Test before guess | 3 failures → switch

## User Information
- **Name**: Alex
- **Role**: Software Engineer (Backend)
- **Editor**: VS Code with Vim keybindings
- **OS**: macOS 14
- **Shell**: zsh with Oh My Zsh
- **Python Version**: 3.11

## Work Environment
- **Projects Directory**: ~/dev/
- **Python Venv Location**: ./venv/ (per project)
- **Preferred Package Manager**: pip + requirements.txt
- **Git Config**: main branch, conventional commits

## Todos
### 🔴 High Priority
- [TODO] Fix bug in auth module — JWT token not refreshing `deadline: 2026-05-15`
- [TODO] Deploy portfolio site to Vercel `deadline: 2026-05-20`

### 🟡 Medium Priority
- [TODO] Add tests for CLI tool `deadline: 2026-05-25`
- [TODO] Update README with usage examples `deadline: 2026-05-22`

### 🟢 Low Priority
- [TODO] Explore Rust for CLI rewrite `deadline: 2026-06-01`

## Projects

### Portfolio Site
- **Status**: Active, 90% complete
- **Tech**: Next.js 14, Tailwind CSS, Vercel
- **Repo**: ~/dev/portfolio
- **Key Configs**:
  - Deploy command: `vercel --prod`
  - Environment: `.env.local` (not committed)
- **Decisions**:
  - [decision] Use static generation over SSR for speed `TTL: 365 days`

### CLI Tool
- **Status**: Active, started
- **Tech**: Python 3.11, argparse, rich
- **Repo**: ~/dev/cli-tool
- **Key Configs**:
  - Entry point: `python -m cli_tool`
  - Tests: `pytest tests/`

## Pitfall Experiences
- [mistake] Forgot to activate venv before pip install → packages installed globally
  → Solution: Always check `which python` before installing
  → Prevention: Add venv check to project setup script
  `TTL: 90 days` (2026-05-10)

- [mistake] Pushed .env file to GitHub
  → Solution: Added .env to .gitignore, rotated secrets
  → Prevention: Use `git status` before every commit
  `TTL: permanent` (2026-05-12)

## Important Decisions
- [decision] Use pytest over unittest for all Python projects
  → Rationale: Better fixtures, plugins, output
  `TTL: 365 days` (2026-05-01)

## Unverified Memories
- [unverified] Alex might prefer afternoon coding sessions (inferred from 2 late commits)
  `confidence: 0.6` — DO NOT USE AS FACT

## User-Vetoed Memories
- [user-vetoed] "Alex prefers light mode" → "Alex prefers dark mode" (vetoed 2026-05-13)

## Audit Log
- 2026-05-14 | user audit | confirmed OK | All entries verified
- 2026-05-07 | user audit | vetoed 1 entry | "Light mode" was wrong
