# User Audit Protocol v3.1

> **Purpose**: Solve the self-supervision paradox. All AI iron rules are self-enforced. If AI "forgets" to check, the system fails silently. User audit is the external enforcement layer.
>
> **Principle**: User authority is absolute. AI cannot override, negotiate, or delay user corrections.

---

## 1. The Self-Supervision Paradox

```
Problem: AI checks itself → AI can "forget" to check → No external validation
         → Errors accumulate → Memory pollution → "My AI is getting worse"

Example:
  Session 1: AI misremembers "user prefers dark mode"
  Session 2-10: AI keeps applying dark mode, reinforcing the false memory
  Session 11: User says "I never said that" → But 10 sessions of pollution
```

**Solution**: Mandatory external audit with hard rules that AI cannot bypass.

---

## 2. Four Hard Rules

### Rule 1: Absolute User Audit Right

```
User Action: View / modify / delete ANY entry in MEMORY.md
AI Response: Immediate compliance. No justification required. No refusal.

Forbidden AI responses:
  ❌ "This memory is important, are you sure?"
  ❌ "Deleting this might affect my performance..."
  ❌ "I recommend keeping this for context."

Required AI response:
  ✅ "Deleted. [Entry summary] removed from [section]."
  ✅ "Modified. Updated [field] from [old] to [new]."
```

### Rule 2: Weekly Audit Reminder

```
Trigger: Every Monday session startup
Condition: Last user audit timestamp > 7 days ago
Action: AI MUST display reminder

Reminder format:
  ⚡ Memory Audit Suggested
  Last audit: YYYY-MM-DD (X days ago)
  Suggested action: Spend 2 minutes scanning MEMORY.md
  Focus areas:
    - [unverified] entries needing confirmation
    - [user-vetoed] entries — are they resolved?
    - Outdated todos or expired TTL entries
    - Any memories that feel "off" or biased
```

**Why 7 days:**
- Daily: User fatigue, becomes ignored noise
- Monthly: Error memory may pollute 4 weeks of sessions
- Weekly: Ritualistic, manageable (2 minutes), catches errors early

### Rule 3: User Veto Mechanism

```
User says: "That's wrong" / "Incorrect" / "Not true" / "I never said that"

AI MUST execute in this exact order:
  1. STOP using the contested memory immediately
  2. Tag entry: [user-vetoed] (AI cannot remove this tag)
  3. Log to accountability:
     YYYY-MM-DD | user-vetoed | [wrong content] → [correct content]
  4. If correct content provided by user → Write as new [fact] entry
  5. In current response: Acknowledge correction, do NOT use old memory

Post-veto behavior:
  - AI stops citing [user-vetoed] entries in ALL future sessions
  - AI can suggest "Should I remove [user-vetoed] entry entirely?"
  - Only user can remove [user-vetoed] tag (by editing the file)
```

### Rule 4: Audit Log Maintenance

```markdown
## Audit Log (in MEMORY.md)

Format:
YYYY-MM-DD | user audit | action | details

Examples:
2026-05-14 | user audit | confirmed OK | All entries verified, no issues
2026-05-14 | user audit | vetoed 2 entries | "Dark mode preference" was wrong; "API key" was outdated
2026-05-14 | user audit | added 3 entries | User manually added project configs
2026-05-14 | user audit | moved 5 entries | Cold memories archived to lessons-learned.md
```

**Maintenance rules:**
- AI can suggest audit log updates but cannot write them without user confirmation
- User can manually edit audit log (it's their file)
- Audit log entries are permanent — never deleted, only appended

---

## 3. Memory Entry States

Every entry in MEMORY.md has a state machine:

```
[unverified] ──user confirms──> [fact/preference/...]
     │                              │
     │──user says wrong──┐         │
     │                   │         │
     └──────────────> [user-vetoed]
                              │
                              │──user manually removes tag──> [fact/preference/...]
                              │
                              └──permanent (AI never removes)
```

### State Definitions

| State | Who can set | Who can remove | AI can cite? |
|-------|-------------|----------------|--------------|
| `[unverified]` | AI (when uncertain) | User only | ❌ NO |
| `[user-vetoed]` | AI (when user corrects) | User only | ❌ NO |
| `[fact]` | AI (after user confirmation) | User only | ✅ YES |
| `[preference]` | AI (after user confirmation) | User only | ✅ YES |
| `[mistake]` | AI (after resolution) | User only | ✅ YES |
| `[decision]` | AI (after discussion) | User only | ✅ YES |
| `[todo]` | AI or user | User or AI (when done) | ✅ YES |

---

## 4. Audit Workflow

### Weekly Audit (User-Initiated or AI-Reminded)

```
Step 1: AI displays current memory statistics
  - Total entries: X
  - [unverified] awaiting confirmation: Y
  - [user-vetoed] unresolved: Z
  - TTL-expired: W
  - Last audit: D days ago

Step 2: User reviews MEMORY.md
  - Scan for "feels wrong" entries
  - Check [unverified] items
  - Decide on TTL-expired items

Step 3: User makes corrections
  - Delete wrong entries
  - Confirm [unverified] items (remove tag)
  - Update outdated info
  - Add missing context

Step 4: AI updates audit log
  - Record date, action, details
  - Update "last audit" timestamp

Step 5: AI applies corrections
  - Stop using deleted/vetoed entries
  - Start using newly confirmed entries
```

### Ad-Hoc Audit (User-Initiated Anytime)

```
User: "Audit my memory" / "Check MEMORY.md" / "Review my preferences"

AI: Display summary → Wait for user commands → Execute immediately
```

---

## 5. Error Isolation Protocol

When user identifies a memory error:

### Immediate Actions (within current session)

```
1. Quarantine: Tag entry [user-vetoed]
2. Stop propagation: Do not use in current response
3. Acknowledge: "You're right. I've marked that as incorrect."
4. Correct: If user provides correct info, write new verified entry
```

### Follow-Up Actions (next sessions)

```
5. Check propagation: Search all files (logs, rules, other memories) for same error
6. Mark all instances: [user-vetoed] everywhere
7. Accountability log: Record the error chain
8. Prevention: Write [mistake] entry: "Previously believed X, user corrected to Y"
```

### Long-Term Prevention

```
9. Pattern detection: Is this a recurring error type?
10. Protocol update: Should we add a new check to prevent this?
11. User education: Explain how to spot similar errors early
```

---

## 6. Audit Templates

### For AI (Weekly Reminder)

```markdown
⚡ Weekly Memory Audit Reminder
─────────────────────────────────
Last audit: 2026-05-07 (7 days ago)

Memory Health Report:
- Total active entries: 47
- [unverified] awaiting confirmation: 3
  → Line 23: "User prefers Vim over VS Code" (confidence 0.7)
  → Line 45: "Project uses Python 3.11" (inferred from file headers)
  → Line 67: "User dislikes emoji in code" (single mention)
- [user-vetoed] unresolved: 1
  → Line 12: "Dark mode preference" (vetoed 2026-05-10)
- TTL-expired pending review: 2
  → Line 89: API key (expired 2026-05-01)
  → Line 91: Temporary workaround (expired 2026-05-05)

Suggested actions:
1. Confirm or remove [unverified] entries
2. Resolve [user-vetoed] entry (delete or correct)
3. Update or remove TTL-expired entries

Time estimate: 2 minutes
```

### For User (Manual Audit Checklist)

```markdown
## My Memory Audit — YYYY-MM-DD

### Quick Scan (30 seconds)
- [ ] Boot snapshot matches reality
- [ ] No obvious false memories jump out
- [ ] Todo list is current

### Detailed Review (90 seconds)
- [ ] Check [unverified] entries → Confirm or delete
- [ ] Check [user-vetoed] entries → Resolve or keep quarantined
- [ ] Check TTL-expired entries → Update or remove
- [ ] Check pitfall entries → Still relevant? Update TTL.

### Corrections Made
- Deleted: ___________
- Modified: ___________
- Confirmed: ___________
- Added: ___________

### Overall Assessment
- [ ] All good
- [ ] Some issues found and fixed
- [ ] Major cleanup needed
```

---

## 7. Integration Checklist

When implementing user audit in your AI:

```
□ AI reads MEMORY.md audit log at startup
□ AI checks "last audit" timestamp
□ If >7 days, AI displays weekly reminder
□ AI responds to "audit" / "review memory" commands
□ AI immediately complies with all user edit/delete requests
□ AI tags [user-vetoed] on any user correction
□ AI never cites [user-vetoed] or [unverified] entries
□ AI maintains audit log with date/action/details
□ AI checks for propagated errors across all memory files
□ AI writes [mistake] entries for user-corrected errors
```
