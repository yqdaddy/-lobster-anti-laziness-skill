# Best Practices

> **Purpose**: Real-world tips from using 龙虾超记忆防偷懒技能 in production. Learn from others' mistakes.

---

## 1. Startup Discipline

### The "First Message" Rule

**Bad**:
```
User: "Fix this bug"
AI: "Sure, let me look at the code..."  ← DID NOT READ MEMORY
```

**Good**:
```
User: "Fix this bug"
AI: "[Reads MEMORY.md] Good morning! I see we have 2 active projects.
     Before we start, I notice you have a todo 'Fix auth bug' due today.
     Is this the same issue, or a new one?"
```

**Tip**: If AI skips reading, don't let it slide. Stop and insist. After 3-5 corrections, it becomes habit.

### The "Cold Start" Problem

If you haven't used the AI for a week:
```
User: "Continue where we left off"
AI: [Reads L0-L4] "Last time (May 7) we were working on Project Alpha.
     Since then, no new logs. Let me check if anything changed..."
```

**Tip**: After long gaps, ask AI to summarize what it remembers before starting new work.

---

## 2. Memory Writing

### Be Specific, Not Vague

**Bad**:
```markdown
- [preference] User likes clean code
```

**Good**:
```markdown
- [preference] User prefers early returns over nested if-statements
  `TTL: permanent` (confirmed 2026-05-14)
```

**Why**: "Clean code" is subjective. "Early returns" is actionable.

### Tag Immediately

Don't wait until end of session to tag entries:
```markdown
- User said they prefer dark mode  ← DON'T
- [preference] User prefers dark mode for all applications `TTL: permanent` ← DO
```

**Why**: Untagged entries are invisible to the recall system.

### Confidence Honesty

If you're not sure, mark it:
```markdown
- [unverified] User might prefer morning standups (inferred from 2 cancellations)
  `confidence: 0.7` — DO NOT USE AS FACT
```

**Why**: False confidence is worse than no memory. The [unverified] tag protects both you and the user.

---

## 3. Todo Management

### The "Parking Lot" Pattern

Don't let todos accumulate indefinitely:

```markdown
### 🔴 High Priority (Max 3)
- [todo] Fix critical bug `deadline: 2026-05-15`
- [todo] Deploy v2.0 `deadline: 2026-05-20`
- [todo] Security audit `deadline: 2026-05-25`

### 🟡 Medium Priority (Max 5)
... (move here if high priority is full)

### 🟢 Low Priority (Review weekly)
... (move here if medium priority is full)
```

**Rule**: If a todo stays in "High Priority" for >7 days without progress, either:
1. Do it now
2. Downgrade to Medium
3. Delete it (it's not actually important)

### The "Done List" Motivation

Keep completed todos visible:
```markdown
### ✅ Completed (Last 30 Days)
- [todo] Setup CI/CD `completed: 2026-05-10`
- [todo] Write API docs `completed: 2026-05-12`
```

**Why**: Seeing progress motivates continued use. Empty "completed" lists feel like nothing was accomplished.

---

## 4. Pitfall Documentation

### The "Root Cause" Rule

**Bad**:
```markdown
- [mistake] Build failed → Fixed by reinstalling dependencies `TTL: 90 days`
```

**Good**:
```markdown
- [mistake] Build failed with "ModuleNotFoundError: No module named 'xyz'"
  → Root cause: xyz was in dev-requirements.txt but not requirements.txt
  → Solution: Always check both files when adding dependencies
  → Prevention: Run `pip install -r requirements.txt -r dev-requirements.txt`
  `TTL: 90 days` (2026-05-14)
```

**Why**: Next time, AI should recognize the pattern, not just the symptom.

### The "Pattern" Pitfall

If the same error happens 3+ times, it's not a pitfall — it's a process failure:

```markdown
- [mistake] Forgot to run migrations before testing (happened 3 times)
  → Root cause: No pre-test checklist
  → Solution: Added "Run migrations" to test script
  → Prevention: Test script now auto-runs migrations
  `TTL: permanent` (2026-05-14 — process fix)
```

---

## 5. User Audit Rituals

### The "Monday Morning" Audit

Make it a ritual:
```
Monday 9:00 AM:
  1. Open MEMORY.md
  2. Scan for [unverified] entries
  3. Check [user-vetoed] — delete or correct
  4. Review TTL-expired items
  5. Check if MEMORY.md needs archiving (>300 lines)
  6. Done. Usually takes 2 minutes.
```

**Tip**: Set a calendar reminder. The AI will also remind you, but don't rely solely on AI.

### The "Monthly Deep Clean"

Once a month:
```
1. Archive logs >30 days old
2. Review all [mistake] entries — still relevant?
3. Check if any projects can be moved to archive
4. Verify all [fact] entries are still accurate
5. Clean up accountability log (mark resolved issues)
```

---

## 6. Anti-Laziness Enforcement

### The "Show Your Work" Rule

For any non-trivial task, AI must show:
```
Before: "I fixed the bug"
After:  "I fixed the bug by:
        1. Identifying the null pointer in auth.py:47
        2. Adding null check: `if user is not None:`
        3. Testing with 3 test cases (all passed)
        4. See execution summary for details"
```

**Why**: If AI can't explain what it did, it probably didn't do it properly.

### The "Test Instead of Guess" Rule

**Bad**:
```
AI: "The issue is probably caused by the CORS configuration"
```

**Good**:
```
AI: "I suspect CORS configuration. Testing hypothesis:
     1. Checked current CORS settings → `allow_origins=['*']`
     2. Tested with curl → Got 403 error
     3. Added explicit origin → Test passed
     Confirmed: CORS was the issue"
```

---

## 7. Memory Hygiene

### The "One Fact Per Line" Rule

**Bad**:
```markdown
- [fact] User uses Python 3.11, prefers FastAPI, and deploys on AWS
```

**Good**:
```markdown
- [fact] User uses Python 3.11 `TTL: permanent`
- [preference] User prefers FastAPI over Flask `TTL: permanent`
- [fact] Project deploys on AWS ECS `TTL: 180 days`
```

**Why**: Easier to update, delete, or verify individual facts.

### The "Source" Rule

Always cite where the memory came from:
```markdown
- [fact] API base URL is https://api.example.com/v2
  `TTL: permanent` (confirmed 2026-05-13 — user explicitly stated)

- [preference] User prefers concise responses
  `TTL: permanent` (inferred from 5 sessions — confidence 0.8)
```

**Why**: Helps during audit. "Where did this come from?" should always be answerable.

---

## 8. Team Usage

### Shared Project Rules

For teams, keep project-specific rules in `rules/*.md`:
```
rules/
├── backend-api.md      (shared by all backend devs)
├── frontend-react.md   (shared by all frontend devs)
├── deployment.md       (shared by DevOps)
└── coding-standards.md (shared by everyone)
```

**Tip**: Store `rules/` in Git. Each team member pulls updates.

### Personal Memory Overlay

Each team member has their own:
```
MEMORY-jacky.md    (Jacky's personal memories)
MEMORY-alice.md    (Alice's personal memories)
```

**Tip**: Personal memories override shared rules. "I know the team uses tabs, but I prefer spaces."

---

## 9. Troubleshooting

### "AI Keeps Adding the Same Memory"

**Cause**: Deduplication not working.

**Fix**: Check if existing entry is tagged. Untagged entries are invisible to deduplication.

### "AI Forgets My Preferences"

**Cause**: Preference not in boot snapshot.

**Fix**: Move critical preferences to L0 (top of MEMORY.md):
```markdown
## ⚡ Boot Snapshot
**Who I Am**: ...
**Key Preferences**: Spaces over tabs | Dark mode | Concise responses
```

### "MEMORY.md is Unreadable"

**Cause**: Too much content, poor organization.

**Fix**: Use the "move" rule. Archive old content. Keep only "hot" memories in MEMORY.md.

### "AI is Getting Worse Over Time"

**Cause**: Memory pollution. False memories accumulated.

**Fix**: Emergency audit:
1. Read entire MEMORY.md
2. Identify false memories
3. Tag [user-vetoed]
4. Check for propagation
5. Add prevention entries

**Prevention**: Weekly audits. Don't skip them.

---

## 10. Advanced Patterns

### The "Decision Register"

For important technical decisions, create a dedicated section:
```markdown
## Decision Register

| Date | Decision | Alternatives | Rationale | Status |
|------|----------|--------------|-----------|--------|
| 2026-05-01 | Use PostgreSQL | SQLite, MySQL | Concurrency needs | Active |
| 2026-05-10 | Use JWT auth | Session, OAuth | Stateless requirement | Active |
```

**Why**: Decisions are easy to forget. A register makes them searchable and auditable.

### The "Skill Extraction"

When AI learns a new skill from pitfalls:
```markdown
## Extracted Skills

- **Skill**: Debugging CORS issues
  - **Pattern**: 403 errors on cross-origin requests
  - **Solution**: Check allow_origins, credentials, methods
  - **Source**: [mistake] entries from 2026-05-10 to 2026-05-14
  - **Created**: 2026-05-14
```

**Why**: Skills are higher-level than individual pitfalls. They enable pattern matching.

---

## Quick Wins

1. **Start small**: Use minimal setup (SOUL.md + MEMORY.md) for first week
2. **Be strict about Rule 0**: Never let AI skip memory read
3. **Audit weekly**: Set Monday calendar reminder
4. **Tag everything**: Untagged memories are invisible
5. **Show your work**: Demand execution summaries for non-trivial tasks
6. **Move, don't delete**: Archive old memories instead of losing them
7. **One fact per line**: Easier to manage and audit
8. **Cite sources**: Always know where memories came from
