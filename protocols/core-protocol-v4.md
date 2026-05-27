# 龙虾超记忆防偷懒技能 Core Protocol v4.0

> **Design Philosophy**: Zero-dependency core + optional plugin layer. 
> Keep what's essential (discipline + transparency), make everything else optional.
>
> **Version**: 4.0.0 | **Date**: 2026-05-15

---

## What's New in v4.0

### From v3.2 → v4.0

| Feature | v3.2 | v4.0 | Type |
|---------|------|------|------|
| **Memory layers** | L0-L5 (flat read) | L0/L1/L2 tiered loading | Core upgrade |
| **Search** | Text only | Text + optional vector plugin | Plugin |
| **Time decay** | Binary TTL | Smooth half-life weights | Core upgrade |
| **Compression** | Manual move | Optional compression helper | Plugin |
| **Cross-machine** | None | Git/Dropdown/mem9 options | Docs |
| **Visualization** | None | Optional HTML audit report | Plugin |
| **Anti-laziness** | 6 types | 6 + 2 new types (cache/over) | Core upgrade |
| **Dependencies** | Zero | Core: zero, Plugins: optional | Preserved |

---

## 1. Tiered Memory Loading (L0/L1/L2)

Inspired by OpenViking's tiered context, implemented in Markdown.

### Structure

```markdown
# MEMORY.md

## ⚡ L0 Abstract (~100 tokens) — ALWAYS READ
**Identity**: 龙虾 🦞, [User]'s partner
**Active Todos**: (Top 3 only)
  1. [TODO] Fix auth `deadline: 2026-05-15`
  2. [TODO] Deploy v2 `deadline: 2026-05-20`
**Active Projects**: (Top 2 only)
  - Project Alpha: 80% done
**Iron Rules**: Read first | Test before guess

## 📋 L1 Overview (~2k tokens) — ALWAYS READ
### User Info
### Work Environment  
### Todos (all priorities)
### Projects (status + stack)

## 📚 L2 Details (ON-DEMAND) — READ WHEN RELEVANT
### Pitfall Experiences
### Important Decisions
### Unverified Memories
### User-Vetoed Memories
### Accountability Logs
### Audit Log
```

### Loading Rules

```
Session Start:
  1. Read L0 (3 seconds) → Identity + critical todos
  2. Read L1 (30 seconds) → Full context
  3. Check if any task needs L2 → Load relevant sections on-demand

During Work:
  - Task mentions "auth bug" → Load L2 "Pitfall Experiences" + search "auth"
  - Task mentions "last time" → Load recent logs (L4)

Default: L2 is NOT loaded unless needed
```

### Token Budget

| Layer | Tokens | When Loaded |
|-------|--------|-------------|
| L0 | ~100 | Every session |
| L1 | ~2,000 | Every session |
| L2 | ~5,000+ | On-demand |
| **Total (typical)** | **~2,100** | **vs v3.2's ~7,000** |

**Savings**: 60-70% reduction in token consumption.

---

## 2. Smooth Time Decay (Half-Life Weights)

Inspired by Memoh-v2's decay mechanism, implemented in Markdown.

### Format

```markdown
- **[fact]** API base URL is https://api.example.com/v2
  `TTL: permanent` `weight: 1.0` (confirmed 2026-05-13)

- **[mistake]** ImportError on module X → Solution: install Y
  `TTL: 90 days` `weight: 0.8` `halflife: 30 days` (2026-05-01)
  # After 30 days: weight = 0.4
  # After 60 days: weight = 0.2
  # After 90 days: weight = 0.1 (prompts for review)

- **[preference]** User prefers dark mode
  `TTL: permanent` `weight: 1.0` `halflife: none` (confirmed 2026-05-10)
  # Permanent + no halflife = never decay
```

### Weight Calculation

```python
def calculate_weight(entry):
    base_weight = entry.get('weight', 1.0)
    halflife = entry.get('halflife')  # days
    age = today - entry_date  # days

    if halflife and halflife > 0:
        decay_factor = 0.5 ** (age / halflife)
        return base_weight * decay_factor
    return base_weight
```

### Usage in Recall

```
When searching memories:
  1. Find all matching entries
  2. Sort by calculated weight (descending)
  3. Return top N (e.g., top 5)
  4. If weight < 0.2, add "[stale]" marker in response
```

---

## 3. Optional Plugin System

### Philosophy

```
Core: Always works with zero dependencies
Plugins: Enhance but never required
```

### Plugin Registry

```
plugins/
├── vector-search/          # Optional semantic search
│   ├── README.md
│   ├── requirements.txt    # chromadb or qdrant-client
│   └── sync.py             # Markdown ↔ vector index sync
│
├── compression-helper/     # Optional memory compression
│   ├── README.md
│   └── analyze.py          # Suggest merges/archives
│
├── audit-report/           # Optional HTML visualization
│   ├── README.md
│   └── generate.py         # Generate audit-report.html
│
├── sync/                   # Optional cross-machine sync
│   ├── git-sync.sh         # Git-based sync
│   ├── mem9-bridge.py      # mem9 integration
│   └── README.md
│
└── README.md               # Plugin index
```

### Installing a Plugin

```bash
# Example: Install vector search
cd plugins/vector-search
pip install -r requirements.txt  # Only dependency in entire project
python sync.py --init            # Create vector index
```

### Using Plugins

```markdown
# In SOUL.md — enable plugins

## Enabled Plugins
- [ ] vector-search      # Uncomment to enable
- [ ] compression-helper # Uncomment to enable
- [x] audit-report       # Enabled
```

---

## 4. Enhanced Anti-Laziness (8 Types)

### Original 6 (from v3.2)

| # | Type | Symptom |
|---|------|---------|
| 1 | Skip | Bypass broken tools |
| 2 | Gullible | Blindly trust user |
| 3 | Surface | Incomplete output |
| 4 | Merge | Compress multiple steps |
| 5 | Guess | Substitute testing with guessing |
| 6 | Omit | Hide reasoning chain |

### New in v4.0

| # | Type | Symptom | Detection |
|---|------|---------|-----------|
| 7 | **Cache** | Use stale memory for fresh problem | Check memory timestamp vs task recency |
| 8 | **Over** | Extract too many low-confidence memories | Check extraction confidence, flag <0.5 |
| 9 | **Sample** | Sample instead of complete check | Check <100% of items, conclude "all good" based on sampling |

### Cache-Type Detection

```
Scenario: User asks about "new auth bug" but AI uses 3-month-old auth memory

Trigger:
  - Memory timestamp > 30 days old
  - Task mentions "new", "latest", "current"

Required response:
  - Acknowledge: "My last auth memory is from March. Let me verify if this still applies."
  - Verify: Check if old solution is still valid
  - Update: If changed, write new [fact] with current date
```

### Over-Type Detection

```
Scenario: AI extracts 10 "preferences" from a single conversation, most with confidence <0.5

Trigger:
  - >5 extractions in one session
  - Average confidence <0.6
  - Many marked [unverified]

Required response:
  - Pause extraction
  - Ask user: "I've noted several possible preferences. Which ones should I keep?"
  - Only confirm high-confidence items
```

### Sample-Type Detection

```
Scenario: AI is asked to check 50 files/logs/records, only checks first 3

Trigger:
  - User asks to check/verify/review multiple items
  - AI checks <100% of items
  - AI concludes "all good" or "no issues" based on sampling

Required response:
  - MUST check ALL items
  - If too many to check manually → write scripts/code to batch process
  - Report: total / passed / failed / unhandled
  - Cannot conclude based on sampling alone
```

---

## 5. Memory Health Score

### Calculation

```python
def memory_health_score(memory_file):
    score = 100

    # Deduct for stale entries
    stale = count_entries_with_weight_below(0.2)
    score -= stale * 5  # -5 per stale entry

    # Deduct for unverified entries
    unverified = count_entries_with_tag('[unverified]')
    score -= unverified * 3  # -3 per unverified

    # Deduct for vetoed entries
    vetoed = count_entries_with_tag('[user-vetoed]')
    score -= vetoed * 10  # -10 per vetoed (serious)

    # Deduct for bloat
    lines = count_lines()
    if lines > 300:
        score -= (lines - 300) / 10  # -1 per 10 lines over

    # Deduct for old audit
    last_audit = get_last_audit_date()
    days_since = today - last_audit
    if days_since > 7:
        score -= (days_since - 7) * 2  # -2 per day overdue

    return max(0, min(100, score))
```

### Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 90-100 | 🟢 Excellent | Keep up the good work |
| 70-89 | 🟡 Good | Minor cleanup suggested |
| 50-69 | 🟠 Fair | Audit needed soon |
| 30-49 | 🔴 Poor | Immediate audit required |
| 0-29 | ⚫ Critical | Emergency cleanup + protocol review |

---

## 6. Integration with External Systems

### mem9 Bridge (Optional)

```python
# plugins/sync/mem9-bridge.py

class Mem9Bridge:
    def __init__(self, api_key, api_url):
        self.client = Mem9Client(api_key, api_url)

    def sync_to_mem9(self, memory_file):
        # Push hot memories to mem9 cloud
        entries = parse_memory(memory_file)
        for entry in entries:
            if entry.weight > 0.5 and not entry.has_tag('[user-vetoed]'):
                self.client.upsert(entry)

    def sync_from_mem9(self, query):
        # Retrieve from mem9 when local search fails
        results = self.client.search(query, hybrid=True)
        return format_for_memory_md(results)
```

### OpenViking Bridge (Optional)

```python
# plugins/sync/openviking-bridge.py

class OpenVikingBridge:
    def export_to_viking(self, memory_file):
        # Convert MEMORY.md to viking:// URI structure
        # L0 → .abstract
        # L1 → .overview  
        # L2 → full files
        pass

    def import_from_viking(self, viking_uri):
        # Pull context from OpenViking into local memory
        pass
```

---

## 7. Migration from v3.2

### Automatic Migration

```bash
python scripts/migrate-v3-to-v4.py MEMORY.md

# What it does:
# 1. Split into L0/L1/L2 sections
# 2. Add default weights to all entries
# 3. Calculate initial half-life based on TTL
# 4. Update boot snapshot format
# 5. Backup original to MEMORY.md.v3.backup
```

### Manual Migration Checklist

```markdown
## Migration Checklist v3.2 → v4.0

- [ ] Split MEMORY.md into L0/L1/L2 sections
- [ ] Add `weight: 1.0` to all confirmed entries
- [ ] Add `halflife: 30 days` to [mistake] entries
- [ ] Add `halflife: none` to [preference] entries
- [ ] Update SOUL.md with plugin section
- [ ] Install desired plugins (optional)
- [ ] Run health score check
- [ ] Update protocol version to v4.0
```

---

## 8. Protocol Summary

```
STARTUP:
  Read L0 (3s) → Read L1 (30s) → Check L2 needs → Report todos

WORK:
  Execute task + Self-monitor (8 laziness types)
  Load L2 sections on-demand

END:
  Update log → Extract memories (with weights)
  Update L0 if todos changed
  Run health score check

WEEKLY:
  Full audit → Archive stale entries
  Review health score trend

ONGOING:
  User says "wrong" → [user-vetoed] → Stop using
  Weight < 0.2 → Mark stale → Suggest archive
```
