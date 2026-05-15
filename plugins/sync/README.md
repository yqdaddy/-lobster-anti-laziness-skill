# Sync Plugin

> **Purpose**: Cross-machine memory synchronization.
> **Dependency**: None for Git sync, mem9 client for mem9 bridge
> **Status**: Optional

---

## Option A: Git Sync (Recommended)

```bash
# One-time setup
git init
git add SOUL.md MEMORY.md memory/ rules/
git commit -m "Initial 龙虾超记忆防偷懒技能"
git remote add origin https://github.com/yourname/lobster-anti-laziness-skill.git

# Daily sync (add to cron or alias)
git add -A && git commit -m "Memory sync $(date)" && git push
```

## Option B: Syncthing / Dropbox / iCloud

Simply sync the lobster-anti-laziness-skill directory across devices.

## Option C: mem9 Bridge

```bash
cd plugins/sync
pip install mem9-client  # Optional dependency

# Configure
export MEM9_API_KEY="your-key"
export MEM9_API_URL="https://api.mem9.ai"

# Sync
python mem9-bridge.py --push  # Upload to mem9
python mem9-bridge.py --pull  # Download from mem9
```

## Conflict Resolution

When sync conflicts occur:
```
1. Git: Use merge tools, manual resolution
2. mem9: Last-write-wins + conflict log
3. File sync: Rename conflicting files, manual merge
```

## Best Practice

```bash
# Pre-sync checklist
□ Close all AI sessions (prevent write conflicts)
□ Run validation: python scripts/validate-memory.py
□ Commit with message: "Pre-sync audit"
□ Push/pull
□ Verify: Check MEMORY.md integrity
```
