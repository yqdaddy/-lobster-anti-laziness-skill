# Memory Lifecycle Protocol v3.2

> **Purpose**: Define the complete CRUD (Create, Read, Update, Delete) lifecycle for memories, including auto-extraction, consolidation, and TTL management.
>
> **Philosophy**: Memories are living documents. They are born from conversation, mature through verification, and retire through expiration or user decision.

---

## 1. Memory States

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   BORN      │───>│   ACTIVE    │───>│   EXPIRED   │
│ (extracted) │    │ (confirmed) │    │ (TTL ended) │
└─────────────┘    └─────────────┘    └──────┬──────┘
       │                    │                 │
       │                    │                 │
       ▼                    ▼                 ▼
  [unverified]         [fact] etc.      [TTL-expired]
                                              │
                                              ▼
                                         ┌─────────────┐
                                         │   DEAD      │
                                         │ (user-deleted│
                                         │  or archived)│
                                         └─────────────┘
```

---

## 2. Creation (Auto-Extraction)

### Trigger Patterns

| Pattern | Example | Entry Type | Confidence |
|---------|---------|------------|------------|
| "Remember..." | "Remember I prefer dark mode" | [preference] | 0.95 |
| "TODO..." | "TODO: Fix the auth bug by Friday" | [todo] | 0.90 |
| Error + Fix | "The build failed because of X, fixed by Y" | [mistake] | 0.85 |
| Decision | "Let's use PostgreSQL instead of SQLite" | [decision] | 0.85 |
| Fact | "The API endpoint is /v2/users" | [fact] | 0.85 |
| Preference (inferred) | User always cancels suggestions with emoji | [preference] | 0.70 |

### Extraction Checklist (Post-Task)

```
□ Scan conversation for trigger patterns
□ Assess confidence level
□ Check MEMORY.md for duplicates (exact + semantic)
□ Determine entry type and TTL
□ Write to appropriate section
□ Update boot snapshot if todos changed
□ Log extraction in daily journal
```

### TTL Assignment Rules

| Entry Type | Default TTL | Rationale |
|------------|-------------|-----------|
| [fact] — config | Permanent | Rarely changes |
| [fact] — environment | 180 days | May change quarterly |
| [preference] | Permanent | Core user identity |
| [todo] | Until deadline | Or 30 days if no deadline |
| [mistake] | 90 days | Review if still relevant |
| [decision] | 365 days | Revisit annually |
| [unverified] | 14 days | Confirm or expire quickly |

---

## 3. Reading (Recall Strategy)

### Session Start Recall

```
Priority 1: L0 Boot Snapshot (3-second recovery)
  → Identity, active todos, current projects

Priority 2: L2 Long-term Memory (full context)
  → User info, environment, all entries

Priority 3: L4 Recent Logs (continuity)
  → Yesterday + today work context

Priority 4: L3 Project Rules (on-demand)
  → Load when specific domain mentioned
```

### Task-Specific Recall

```
User mentions "auth bug" → Search:
  1. MEMORY.md "Pitfall Experiences" for "auth"
  2. Recent logs for "auth" tasks
  3. rules/auth.md if exists

User says "like last time" → Search:
  1. Logs for similar task patterns
  2. MEMORY.md for related decisions
```

### Recall Constraints

```
DO NOT recall:
  ❌ [user-vetoed] entries (permanently quarantined)
  ❌ [unverified] entries (not confirmed)
  ❌ [TTL-expired] entries (pending user review)
  ❌ Entries from archived files unless explicitly requested

DO recall:
  ✅ [fact], [preference], [mistake], [decision] — verified
  ✅ [todo] — active
  ✅ Boot snapshot — always
```

---

## 4. Updating (Consolidation)

### Daily Consolidation (End of Session)

```
① Log distillation
   Today's log → Long-term value? → Move to MEMORY.md

② Todo maintenance
   Completed → Mark done or remove
   Expired → Mark reason, suggest removal

③ Boot snapshot sync
   Ensure top-of-file summary matches actual state

④ TTL check
   Expired entries → Mark [TTL-expired: pending review]
   NEVER auto-delete
```

### Weekly Consolidation (With User Audit)

```
① Archive old logs
   7+ day old logs → Distill essence → Keep file, mark "archived"

② Memory bloat check
   MEMORY.md >300 lines → Generate move list → Wait for user confirmation

③ Deduplication
   Jaccard similarity >0.8 → Merge entries

④ Trigger user audit reminder
```

### Monthly Consolidation

```
① 30+ day old logs
   → Remind user: "Archive or delete?"
   → AI cannot delete without user approval

② Accountability log cleanup
   → Mark resolved issues as "closed"
   → Keep for pattern analysis

③ Skill assessment
   → Worthy experiences → Create standalone skill file
   → Link in MEMORY.md

④ TTL-expired summary
   → List all expired entries
   → User confirms: keep/update/delete for each
```

---

## 5. Deletion (User-Controlled)

### Deletion Rules

| Who | Can Delete | Cannot Delete |
|-----|-----------|---------------|
| **User** | ANYTHING | Nothing — absolute authority |
| **AI** | [todo] when marked done | Everything else |

### Deletion Process

```
User requests deletion:
  1. AI immediately complies
  2. Log: YYYY-MM-DD | deleted | [entry summary] | user request
  3. If entry was [user-vetoed] → Also remove from all propagation locations
  4. Update boot snapshot if affected

AI suggests deletion (TTL-expired, completed todos):
  1. Present list to user: "These entries may be outdated. Delete?"
  2. Wait for user confirmation for EACH entry
  3. Never bulk-delete without explicit per-item approval
```

### Soft Delete vs Hard Delete

```
Soft delete (recommended):
  - Mark [deleted: YYYY-MM-DD]
  - Keep in file for audit trail
  - AI stops using it
  - User can "undelete" by removing tag

Hard delete (user request):
  - Remove line entirely
  - Log the deletion
  - Irreversible
```

---

## 6. Deduplication Strategy

### Exact Match Detection

```
Before writing new entry:
  Search MEMORY.md for identical text
  If found → Skip (already exists)
```

### Semantic Similarity (Jaccard > 0.8)

```
Example:
  Existing: "User prefers dark mode for all applications"
  New: "User likes dark theme in IDEs and browsers"

  Similarity: High (both = dark mode preference)
  Action: Merge → Update existing entry with broader scope
```

### Merge Rules

```
When merging:
  1. Keep earlier timestamp (original discovery date)
  2. Combine details from both entries
  3. Update confidence to higher of the two
  4. If one is [unverified] and one confirmed → Use confirmed
  5. Log merge in daily journal
```

---

## 7. Entry Format Specification

### Standard Entry

```markdown
- **[TYPE]** Content `TTL: duration` (metadata)
```

### Examples

```markdown
- **[fact]** API base URL is https://api.example.com/v2 `TTL: permanent` (confirmed 2026-05-13)
- **[preference]** User prefers concise responses without emojis `TTL: permanent` (user stated 2026-05-10)
- **[todo]** Refactor auth module to use JWT `deadline: 2026-05-20` (added 2026-05-14)
- **[mistake]** ImportError on module X → Solution: install package Y first `TTL: 90 days` (resolved 2026-05-12)
- **[decision]** Use PostgreSQL over SQLite for user data, because: concurrency requirements `TTL: 365 days` (decided 2026-05-11)
- **[unverified]** User might prefer morning meetings (inferred from 2 cancellations) `confidence: 0.7` — DO NOT USE AS FACT
```

### Special States

```markdown
- **[user-vetoed]** Wrong info: "User prefers tabs" → Correct: "User prefers spaces" (vetoed 2026-05-14, user-confirmed)
- **[TTL-expired: pending]** Old API key, expired 2026-05-01 — awaiting user review
```

---

## 8. Lifecycle Integration

```
CONVERSATION → Auto-extract → [unverified] → User confirms → [fact/etc.]
                                                      ↓
                                              User contradicts → [user-vetoed]
                                                      ↓
                                              User silent 14 days → [TTL-expired]
                                                      ↓
                                              User reviews → Keep / Update / Delete
```

**Read the full core protocol →** [core-protocol.md](core-protocol.md)
**Read user audit framework →** [user-audit.md](user-audit.md)
**Read anti-laziness enforcement →** [anti-laziness.md](anti-laziness.md)
