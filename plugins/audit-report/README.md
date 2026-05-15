# Audit Report Plugin

> **Purpose**: Generate HTML visualization of memory health.
> **Dependency**: None (pure Python)
> **Status**: Optional

---

## Installation

```bash
cd plugins/audit-report
```

## Usage

```bash
python generate.py ../MEMORY.md

# Generates: audit-report.html
# Auto-opens in browser (optional)
```

## Report Contents

```
┌─────────────────────────────────────────┐
│  Memory Health Dashboard                │
│  Score: 87/100 🟡                       │
├─────────────────────────────────────────┤
│  📊 Entry Distribution                  │
│  [fact] ████████ 20                     │
│  [preference] ████ 10                   │
│  [todo] ██ 5                            │
│  [mistake] ███ 8                        │
│  [unverified] ██ 4 ⚠️                   │
│  [user-vetoed] █ 2 🔴                   │
├─────────────────────────────────────────┤
│  ⏰ TTL Status                          │
│  Healthy: 35 ████████████████           │
│  Expiring soon: 8 ███                   │
│  Expired: 4 ██ ⚠️                       │
├─────────────────────────────────────────┤
│  📈 Growth Trend (30 days)              │
│  ████████████████████ (growing)           │
├─────────────────────────────────────────┤
│  🔍 Recommendations                     │
│  1. Confirm 4 [unverified] entries      │
│  2. Delete 2 [user-vetoed] entries      │
│  3. Archive 5 cold memories             │
└─────────────────────────────────────────┘
```

## Features

- Pure HTML/CSS/JS — no external dependencies
- Responsive design — works on mobile
- Export to PDF — print-friendly layout
- Historical tracking — compare with previous audits
