# Compression Helper Plugin

> **Purpose**: Analyze MEMORY.md and suggest compression opportunities.
> **Dependency**: None (pure Python standard library)
> **Status**: Optional

---

## Installation

```bash
# No dependencies needed
cd plugins/compression-helper
```

## Usage

```bash
python analyze.py ../MEMORY.md

# Output:
# 📊 Memory Analysis Report
# ─────────────────────────
# Total entries: 47
# Similarity clusters found: 3
# 
# 💡 Suggestions:
# 1. Merge 3 [mistake] entries about "ImportError"
#    → Create single comprehensive entry
# 2. Archive 5 completed project entries
#    → Move to memory/projects-archive.md
# 3. Remove 2 [unverified] entries >30 days old
#    → User confirmation needed
# 
# 📈 Health Impact:
# Current: 280 lines
# After compression: ~180 lines (-36%)
# Health score: 72 → 89
```

## Features

- **Similarity detection**: Jaccard + TF-IDF hybrid
- **Cluster analysis**: Groups related entries
- **Archive suggestions**: Identifies cold memories
- **Health impact preview**: Shows before/after scores

## Safety

- Only provides suggestions — never auto-modifies
- User must confirm each action
- Creates `.backup` before any change
