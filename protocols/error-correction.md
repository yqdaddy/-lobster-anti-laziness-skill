# Error Memory Correction Protocol v3.1

> **Purpose**: Prevent the "positive feedback loop of falsehood" — where AI remembers wrong, keeps using the wrong memory, and progressively pollutes all subsequent reasoning.
>
> **Core principle**: AI can suspect its memory but cannot "correct" confirmed information on its own. All corrections require user confirmation.

---

## 1. The False Memory Feedback Loop

```
Session 1: AI misremembers "User prefers tabs over spaces"
           ↓
Session 2: AI uses tabs, user doesn't object (user didn't notice)
           ↓
Session 3-10: AI keeps using tabs, memory reinforced 9 more times
           ↓
Session 11: User says "Why are you using tabs? I prefer spaces!"
           ↓
Problem: 10 sessions of polluted code, 10 reinforced false memories
         → User trust degraded → "My AI is getting worse"
```

**Root cause**: AI has no mechanism to:
1. Detect its own false memories
2. Quarantine them immediately
3. Prevent reinforcement across sessions

---

## 2. Correction Protocol

### Detection Triggers

| Trigger | Source | Priority |
|---------|--------|----------|
| User explicitly says "wrong"/"incorrect"/"not true" | User | 🔴 Critical |
| User contradicts previous memory without saying "wrong" | User | 🟡 High |
| AI finds internal inconsistency (two memories conflict) | AI | 🟡 High |
| AI realizes previous inference was weak | AI | 🟢 Medium |

### Immediate Response (User-Triggered)

```
User: "That's wrong. I never said I prefer tabs."

AI response (MUST follow this exact order):

1. ACKNOWLEDGE (immediate)
   "You're absolutely right. I apologize for the incorrect memory."

2. QUARANTINE (immediate)
   - Locate the false entry in MEMORY.md
   - Tag: [user-vetoed]
   - Add: → Correct info: "User prefers spaces over tabs" (if provided)
   - AI CANNOT remove [user-vetoed] tag ever

3. STOP USING (immediate)
   - Do not use the false memory in current response
   - Do not use it in any future session

4. LOG (within same session)
   Add to accountability log:
   YYYY-MM-DD | user-vetoed | "tabs preference" → "spaces preference" | User corrected

5. PREVENT (within same session)
   Write to pitfalls:
   - **[mistake]** Previously believed user prefers tabs. User corrected: prefers spaces.
     `TTL: permanent` (2026-05-14 user-confirmed)
```

### Follow-Up (Next Sessions)

```
Session N+1 startup:
  - Read [user-vetoed] entries
  - Verify not using them
  - Check if user removed [user-vetoed] tag (if so, restore)

Session N+1 work:
  - If similar topic arises, consult [mistake] entry first
  - "Previously made this error, user corrected to X"

Weekly audit:
  - List all [user-vetoed] entries
  - Check for resolution (user deleted or corrected)
  - If unresolved >30 days, ask user: "Should I delete this vetoed memory?"
```

---

## 3. AI Self-Correction (Internal Detection)

When AI detects possible error WITHOUT user trigger:

```
Scenario: AI notices "User prefers dark mode" but last 5 sessions
          user always worked during daytime with light mode screenshots.

AI action:
  1. DO NOT "correct" the memory
  2. DO NOT silently update it
  3. TAG: [unverified] (if not already)
  4. NEXT SESSION STARTUP: Remind user
     "I noticed my memory 'you prefer dark mode' may be outdated.
      You've been using light mode recently. Should I update this?"
  5. WAIT for user confirmation
  6. If user confirms → Update entry, remove [unverified]
  7. If user says no → Tag [user-vetoed], log correction
```

**Why AI cannot self-correct:**
- AI's "detection" might itself be wrong (second-order error)
- User might have context AI doesn't know ("I use dark mode at home, light at work")
- Self-correction bypasses user authority, violating core principle

---

## 4. Propagation Check

When a memory is vetoed, check if it spread to other files:

```
Search scope:
  - All memory/YYYY-MM-DD.md files
  - All rules/*.md files
  - Any project documentation
  - Any generated code comments referencing the false memory

For each found instance:
  1. Mark [user-vetoed] at that location too
  2. Add reference: "See MEMORY.md line X for correct info"
  3. If instance is in generated code → Suggest user review file

Report to user:
  "I found this false memory in 3 other locations. I've marked them all.
   Please review: [list of files]"
```

---

## 5. Confidence Scoring & Escalation

### Entry Confidence Levels

| Level | Source | AI Can Use? | User Action Required? |
|-------|--------|-------------|----------------------|
| 0.95 | User explicitly said "remember this" | ✅ Yes | No |
| 0.85 | Specific data (dates, paths, versions) | ✅ Yes | No |
| 0.7 | Behavior-inferred | ⚠️ With [unverified] tag | Confirm to upgrade |
| 0.5 | Single mention, no confirmation | ❌ No | Must confirm first |
| [user-vetoed] | User corrected | ❌ NEVER | User removes tag |

### Escalation Rules

```
Inferred (0.7) → User confirms → Upgrade to 0.95, remove [unverified]
Inferred (0.7) → User silent for 3 sessions → Keep [unverified], remind
Inferred (0.7) → User contradicts → [user-vetoed], log mistake

Confirmed (0.95) → User contradicts → [user-vetoed], log mistake
Confirmed (0.95) → User updates → Update entry, keep confirmed
```

---

## 6. Correction Templates

### For AI (When User Points Out Error)

```markdown
## Memory Correction — YYYY-MM-DD

**False memory quarantined:**
- Location: MEMORY.md line 45
- Content: "User prefers tabs for indentation"
- Tag: [user-vetoed]

**Correct information:**
- Source: User correction (2026-05-14)
- Content: "User prefers 4 spaces for indentation"
- Tag: [fact] `TTL: permanent`

**Propagation check:**
- Checked: 12 log files, 3 rule files
- Found in: memory/2026-05-10.md (line 8), rules/python-style.md (line 3)
- Action: Marked [user-vetoed] in all locations

**Prevention:**
- Added to pitfalls: "[mistake] Indentation preference — always confirm before applying"
- TTL: permanent
```

### For User (When Correcting AI)

```markdown
## My Correction — YYYY-MM-DD

**What AI got wrong:**
___________

**The correct information:**
___________

**Where I found the error:**
- [ ] MEMORY.md
- [ ] Today's response
- [ ] Previous session
- [ ] Other: ___________

**Severity:**
- [ ] Minor (preference, style)
- [ ] Major (technical fact, config)
- [ ] Critical (security, API keys, paths)

**Should AI:**
- [ ] Update the existing entry
- [ ] Delete the wrong entry
- [ ] Add a new corrected entry
- [ ] Check if this error spread elsewhere
```

---

## 7. Recovery Metrics

Track correction effectiveness:

```markdown
## Error Recovery Metrics (maintained in MEMORY.md)

| Month | False Memories Detected | User-Vetoed | Self-Detected | Repeat Errors | Recovery Time |
|-------|------------------------|-------------|---------------|---------------|---------------|
| 2026-04 | 3 | 2 | 1 | 0 | <1 session |
| 2026-05 | 1 | 1 | 0 | 0 | Immediate |

Trend: ↓ Decreasing = AI learning from corrections
       ↑ Increasing = Need protocol adjustment
```

---

## 8. Integration with Core Protocol

```
STARTUP:
  Read [user-vetoed] entries → Verify not using them
  Read [unverified] entries → Remind user to confirm

WORK:
  Before using any memory → Check state (confirmed/vetoed/unverified)
  If uncertain → Mark [unverified], don't use

POST-WORK:
  If user corrected anything → Run full correction protocol
  If AI suspected error → Mark [unverified], remind next session

WEEKLY:
  List all [user-vetoed] → Ask user if resolved
  List all [unverified] >7 days → Ask user to confirm or delete
  Update error metrics
```
