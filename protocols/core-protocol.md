# Core Protocol — 龙虾超记忆防偷懒技能 v3.2

> **Design Philosophy**: The simplest technology (Markdown files) + three-layer execution protocol (AI self-check + anti-laziness + user audit) outperforms the most advanced technology + poor execution.
>
> **Core Principle**: AI has memory *write* rights. **The user has final interpretation and veto rights.**

---

## Table of Contents

1. [Memory Layer Architecture](#1-memory-layer-architecture)
2. [Memory Lifecycle](#2-memory-lifecycle)
3. [Mandatory Execution Protocol](#3-mandatory-execution-protocol)
4. [User Audit Framework](#4-user-audit-framework)
5. [Memory Bloat Management](#5-memory-bloat-management)
6. [Error Memory Repair](#6-error-memory-repair)
7. [Integration with Native Memory](#7-integration-with-native-memory)

---

## 1. Memory Layer Architecture (6 Layers)

Inspired by Claude Code + Letta agent architecture:

```
┌─────────────────────────────────────────┐
│  L0 Boot Snapshot                       │  ← MEMORY.md top ⚡ Boot zone
├─────────────────────────────────────────┤
│  L1 Core Identity (SOUL.md)             │  ← Who am I, iron rules, values
├─────────────────────────────────────────┤
│  L2 Long-term Memory (MEMORY.md)        │  ← User info, projects, pitfalls, todos
├─────────────────────────────────────────┤
│  L3 Project Rules (rules/*.md)          │  ← Modular rules by topic
├─────────────────────────────────────────┤
│  L4 Daily Logs (memory/YYYY-MM-DD.md)   │  ← Daily work journal
├─────────────────────────────────────────┤
│  L5 Session Memory (system prompt)      │  ← Current context (automatic)
└─────────────────────────────────────────┘
```

### Read/Write Rules by Layer

| Layer | File | Write Trigger | Read Trigger |
|-------|------|---------------|--------------|
| L0 Boot | MEMORY.md top | Every todo change | **Every session start — MANDATORY** |
| L1 Identity | SOUL.md | Iron rule changes | Every session start (system injection) |
| L2 Long-term | MEMORY.md | Pitfall/preference/project changes | Every session start |
| L3 Rules | rules/*.md | New rule creation | On-demand by topic |
| L4 Logs | memory/YYYY-MM-DD.md | **Every substantial work completion** | Recent context lookup |
| L5 Session | System prompt | Automatic | Always in context |

---

## 2. Memory Lifecycle

### 2.1 Write Protocol (CRUD + Deduplication)

**What MUST go to MEMORY.md (long-term):**

| Priority | Content | Entry Type |
|----------|---------|------------|
| 🔴 Critical | User-stated preferences/requirements/decisions | [preference] |
| 🔴 Critical | Pitfall experiences and root causes | [mistake] |
| 🔴 Critical | Cross-session todo items | [todo] |
| 🔴 Critical | Project configs (paths, keys, versions) | [fact] |
| 🟡 Important | Technical decisions and rationale | [decision] |
| 🟡 Important | Deep knowledge about stocks/projects | [fact] |

**What goes to daily logs only (short-term):**
- Routine operation records ("read file X", "searched web")
- Intermediate results, temporary paths
- Daily stock analysis (distill to MEMORY.md after market close if still relevant)

### Write Rules (mem0-style deduplication):

```
① Read before write → Check if same/similar content exists
② Exact match → Skip (already exists)
③ Semantic similarity >80% → Merge/update existing entry
④ New content → Append to relevant section
⑤ MEMORY.md >300 lines → MOVE (not distill) to topic files (see §5)
⑥ Tag every entry: [fact/preference/todo/mistake/decision]
⑦ Tag with [TTL: X days] for expiration (AMS-style)
⑧ AI does NOT own final interpretation — user can veto anytime
```

### Structured Entry Format

```markdown
- **[fact]** Key fact description `TTL: permanent` (confirmed 2026-05-13)
- **[preference]** User preference description
- **[todo]** Todo content `deadline: YYYY-MM-DD`
- **[mistake]** Root cause → Solution `TTL: 90 days`
- **[decision]** Chose X because Y
- **[unverified]** Unverified info — AI must NOT use as fact until confirmed
```

### Memory Pollution Protection (v3.1+)

**The fatal flaw of AI self-constraint**: If AI remembers wrong, every session reinforces the error. Positive feedback loop of falsehood.

**Defense layers:**

1. **Uncertain info** → MUST tag `[unverified]`. Never cite as fact.
2. **User says "wrong"/"no"/"incorrect"** → IMMEDIATELY tag `[user-vetoed]`
   → Stop citing until user manually removes tag
3. **AI cannot remove** `[user-vetoed]` or `[unverified]` tags. Only user can.
4. **Consolidation ignores** `[unverified]` and `[user-vetoed]` entries.
5. **Every [fact] cites source**: user-confirmed / behavior-inferred / external.
   - Inferred confidence defaults to 0.7. Requires user confirmation to upgrade.

### 2.2 Auto-Extraction (AMS-style)

**Post-task extraction checklist:**

```
□ Scan conversation for these patterns:
  - User says "remember"/"save" → [preference] HIGH confidence
  - User mentions "todo"/"TODO"/"need to" → [todo]
  - Error occurred and was resolved → [mistake] root cause + fix
  - Technical decision made → [decision]
  - New fact/config discovered → [fact]
  - User expresses habit/preference → [preference]

□ If found → Write to MEMORY.md relevant section
□ If none → Write to log only
```

**Confidence scoring:**
- User explicitly says "remember" → 0.95 (direct write)
- Contains specific dates/paths/versions → 0.85+
- Behavior-inferred preference → 0.7 (mark [unverified] pending confirmation)
- Contains "maybe"/"probably"/"should" → -0.1 confidence penalty

**Deduplication (mem0 + AMS):**
```
Before writing to MEMORY.md:
① Exact match → Exists, skip
② Semantic similarity >80% → Merge/update
③ New → Append
```

### 2.3 Consolidation (Gemini Always-On style)

**End-of-session consolidation:**

```
① Today's log → Worth keeping long-term? → Distill to MEMORY.md
② MEMORY.md → Outdated entries? → Update or mark expired
③ Todos → Completed? → Mark done or remove. Expired? → Mark reason.
④ Logs >30 days old → Distill essence to MEMORY.md → Keep original file
⑤ TTL-expired entries → Assess need → Mark [TTL-expired: pending review]
   → NEVER auto-delete. Wait for user audit.
```

### 2.4 Recall (mem0 hybrid search)

**Session start recall order:**

```
① Read MEMORY.md ⚡ Boot Snapshot (L0) → Restore identity + todos
② Read MEMORY.md full content (L2) → Restore detailed context
③ Read yesterday + today logs (L4) → Restore recent work context
④ Check todo section → Unfinished items? → Proactively report to user
```

**Task-specific recall:**
```
Domain-specific task → Search MEMORY.md relevant sections
Similar error encountered → Search "Pitfall Experiences" section
User says "last time"/"before" → Search logs for context
```

---

## 3. Mandatory Execution Protocol

### 3.1 Session Start Self-Check (Iron Rule 0 — Highest Priority)

**Before responding to the first message of every new session:**

```
Step 1: Read MEMORY.md
  → Confirm identity: I am [Name], user is [Name]
  → Confirm todos: Any unfinished items?
  → Confirm preferences: User style, habits

Step 2: Read recent logs (today + yesterday)
  → Confirm context: What was being worked on?

Step 3: Check and report
  → Have todos? → "Last time we had X unfinished. Continue?"
  → No todos? → Normal response
```

**Speaking without reading memory = amnesia = negligence**

### 3.2 Post-Task Write Check (Mandatory after every substantial work)

```
□ Did I write today's log?
□ Did I run the auto-extraction checklist? (see §2.2)
□ Any new todos/pitfalls/preferences to write to MEMORY.md?
□ Is MEMORY.md boot snapshot todo list updated?
□ Did I deduplicate new content? (see §2.1 write rules)
→ ALL checked? → Then reply to user
```

---

## 4. User Audit Framework

### The Self-Supervision Paradox

All iron rules are AI self-constraint. If AI "forgets" the checklist, "judges" something unimportant, or "decides" something expired should be deleted — the entire system lacks external enforcement.

**Solution: User holds ultimate authority.**

### Hard Rule 1 — User Audit Right

```
User can view/modify/delete ANY entry in MEMORY.md at any time.
AI cannot refuse deletion/modification with "this is important memory."
User says delete = delete. No negotiation.
```

### Hard Rule 2 — Weekly Audit Reminder

```
Every Monday startup: If last user audit >7 days ago, AI MUST remind:
"⚡ Suggest spending 2 minutes scanning MEMORY.md to confirm no bias or false memories."
```

**Why 7 days:**
- Too frequent (daily) → User annoyance, becomes noise
- Too rare (monthly) → False memories may pollute for 4 weeks
- Every Monday → Weekly ritual, 2 minutes sufficient

### Hard Rule 3 — User Veto Mechanism

```
User points out memory error → AI MUST:
① Immediately tag entry [user-vetoed]
② Log to accountability: What was vetoed → What is correct
③ Stop citing this entry in future sessions (unless user manually restores)
```

### Hard Rule 4 — Audit Log

Maintained in MEMORY.md:
```markdown
## Audit Log
- YYYY-MM-DD | user audit | confirmed OK / vetoed XX / added YY
```

---

## 5. Memory Bloat Management

### Problem Diagnosis

200-line hard limit is unrealistic. Active users easily exceed with projects + pitfalls + todos. "Distill" when exceeding — but distillation is AI judgment, and wrong judgment loses information.

### Solution: Move, Don't Distill

```
MEMORY.md always holds "hot memory" (currently active, recently needed).
When >300 lines, move cold content to topic files:

Move rules:
① Pitfalls >20 entries → Move to memory/lessons-learned.md
② Completed project records → Move to memory/projects-archive.md
③ Expired but retained decisions → Move to memory/decisions-archive.md
④ Leave reference line in MEMORY.md original location:
   "See memory/lessons-learned.md for details"

⑤ AI cannot decide WHAT to move — move list needs user confirmation
   (Handle during weekly audit)
⑥ Moving does NOT delete info — Source file retained, just removed from MEMORY.md
```

---

## 6. Error Memory Repair

**Symptom**: AI remembers wrong and keeps citing the false memory in subsequent sessions (positive feedback loop of falsehood).

**Repair Protocol (v3.1 enhanced):**

```
① User points out error → Immediately mark [user-vetoed], stop citing
② AI discovers possible error → Mark [unverified], remind user to confirm next startup
③ Log to accountability: Wrong content → Correct content → Discovery cause
④ Check if logs/other files cite same error → Mark all instances
⑤ User correction → Write to pitfalls: "[mistake] User corrected, never repeat"
⑥ If error cited multiple times → List all citation locations, wait for user to confirm fixes

Key principles:
- AI can suspect its memory but cannot "correct" confirmed info on its own
- All corrections require user confirmation to take effect
- Better to over-tag [unverified] than confidently spread false info
```

---

## 7. Integration with Native Memory Systems

龙虾超记忆防偷懒技能 does NOT replace platform-native memory mechanisms. It **strengthens execution discipline**:

| System | Responsibility |
|--------|--------------|
| Platform native | File paths, read/write timing |
| 龙虾超记忆防偷懒技能 | Standard structure, execution protocol, auto-extraction, accountability, TTL |

**Example integration:**
- WorkBuddy defines `working_memory_files` paths in system prompt
- 龙虾超记忆防偷懒技能 provides the content structure and enforcement rules
- Both coexist; 龙虾超记忆防偷懒技能 adds the discipline layer

---

## Protocol Summary

```
STARTUP:   Read L0 → L2 → L4 → Report todos
WORK:      Execute task + Run anti-laziness checklist
END:       Write log → Auto-extract → Update MEMORY.md → Consolidate
WEEKLY:    User audit reminder → Move cold memories → Deduplicate
ONGOING:   User veto → [user-vetoed] tag → Accountability log
```
