# Getting Started with 龙虾超记忆防偷懒技能

> **Time to setup**: 5 minutes
> **Time to first value**: Immediate (next AI session)
> **Prerequisites**: Any AI assistant that can read/write files

---

## Step 1: Choose Your Setup Method

### Method A: Minimal (Recommended for Beginners)

Just 2 files. That's it.

```bash
# 1. Create your AI identity
cat > SOUL.md << 'EOF'
# Agent Identity

**Name**: Claw
**Role**: AI coding partner
**User**: [Your name]
**Language**: English

## Iron Rules
1. Read MEMORY.md before every session
2. Run anti-laziness checklist after every task
3. User owns all memory interpretation rights
EOF

# 2. Create your memory file
cat > MEMORY.md << 'EOF'
# My AI Memory

## ⚡ Boot Snapshot
**Who I Am**: Claw, [Your name]'s AI partner
**Active Todos**: (none yet)
**Current Projects**: (none yet)

## User Information
- **Name**: [Your name]
- **Preferences**: (AI will fill this in)

## Todos
### 🔴 High Priority
### 🟡 Medium Priority
### 🟢 Low Priority

## Pitfall Experiences
## Important Decisions
## Unverified Memories
## User-Vetoed Memories
EOF

# 3. Create logs directory
mkdir -p memory
```

### Method B: Full Setup (Recommended for Power Users)

Use the templates from this repository:

```bash
# Clone or download this repo
git clone https://github.com/yourusername/lobster-anti-laziness-skill.git

# Copy templates to your project
cp lobster-anti-laziness-skill/templates/SOUL.md ./SOUL.md
cp lobster-anti-laziness-skill/templates/MEMORY.md ./MEMORY.md
cp lobster-anti-laziness-skill/templates/daily-log.md ./memory/2026-05-14.md

# Customize the files
# (Edit SOUL.md and MEMORY.md with your details)
```

---

## Step 2: Configure Your AI

### For Claude (Claude Code)

Add to your system prompt or `.claude.md`:

```markdown
# 龙虾超记忆防偷懒技能 Protocol

You are following the 龙虾超记忆防偷懒技能 protocol v3.2.

## Startup (MANDATORY — Before first response)
1. Read SOUL.md
2. Read MEMORY.md (full file)
3. Read memory/YYYY-MM-DD.md (today and yesterday)
4. Check for unfinished todos
5. Report todos to user if found

## During Work
- Follow all instructions in SOUL.md
- Apply anti-laziness checklist after every task
- Use execution summary template for substantial work

## After Work
1. Update memory/YYYY-MM-DD.md
2. Run auto-extraction checklist
3. Update MEMORY.md if new memories found
4. Update boot snapshot if todos changed

## Rules
- User has absolute authority over all memories
- Tag uncertain info as [unverified]
- Tag user corrections as [user-vetoed]
- Never remove [user-vetoed] or [unverified] tags
- Weekly audit reminder if unaudited for 7+ days
```

### For ChatGPT / GPT-4

1. Create a Custom GPT
2. In "Instructions", paste the startup protocol above
3. In "Knowledge", upload your SOUL.md and MEMORY.md files
4. Enable "Code Interpreter" for file updates

### For WorkBuddy

1. Copy the protocol files to `.workbuddy/skills/lobster-anti-laziness-skill/`
2. Reference the skill in your WorkBuddy configuration
3. The system will automatically inject the protocol into prompts

### For Cursor

1. Create `.cursorrules` in your project root
2. Add the startup protocol
3. Cursor will read it at the start of every session

---

## Step 3: Your First Session

### What to Say

Start your first conversation with:

```
I'm setting up 龙虾超记忆防偷懒技能. Please:
1. Read SOUL.md
2. Read MEMORY.md
3. Confirm you understand the protocol
4. Ask me anything you need to know about my preferences
```

### What Should Happen

The AI should:
1. ✅ Acknowledge reading both files
2. ✅ Confirm understanding of iron rules
3. ✅ Ask about your preferences (editor, language, style)
4. ✅ Write your answers to MEMORY.md

### If It Doesn't

```
"You didn't read MEMORY.md. Please stop and read it before continuing."
```

This is Rule 0 enforcement. Don't let the AI skip it.

---

## Step 4: Daily Usage

### Morning Routine

```
User: "Good morning, let's continue yesterday's work."

AI: [Reads MEMORY.md] "Good morning! Last time we were working on [project].
     You have 2 unfinished todos:
     1. Fix auth bug (due today)
     2. Update documentation (due Friday)
     Should we start with the auth bug?"
```

### During Work

Just work normally. The AI should:
- Remember your preferences (e.g., "You prefer spaces over tabs")
- Avoid previous pitfalls (e.g., "Last time we had this ImportError, the fix was...")
- Track todos automatically

### End of Session

```
User: "That's all for today."

AI: [Updates log] "Got it. I've logged today's work:
     - Fixed auth bug (completed)
     - Extracted 2 new memories to MEMORY.md
     - Created 1 new todo: 'Write tests for auth'

     ⚡ Reminder: You have 1 todo due tomorrow.
     See you next session!"
```

---

## Step 5: Weekly Audit (Critical!)

Every Monday (or when AI reminds you):

```
AI: "⚡ Memory Audit Suggested
     Last audit: 7 days ago

     Memory Health:
     - 47 active entries
     - 3 [unverified] awaiting confirmation
     - 1 [user-vetoed] unresolved

     Suggested: Spend 2 minutes scanning MEMORY.md."

User: "Let's audit."

AI: [Presents summary] "Here are items needing attention:

     [unverified]:
     1. 'You prefer Vim' (confidence 0.7) — Confirm or delete?
     2. 'Project uses Python 3.11' — Confirm or delete?

     [user-vetoed]:
     1. 'Dark mode preference' — Delete or correct?

     What would you like to do?"
```

**This 2-minute ritual prevents memory pollution.**

---

## Common Issues

### "AI Keeps Forgetting to Read Memory"

**Cause**: AI's session memory (L5) overrides file memory.

**Fix**: Be strict. Every time AI skips reading, say:
```
"Stop. You didn't read MEMORY.md. Read it now before responding."
```

After 3-5 corrections, most AIs learn.

### "MEMORY.md is Getting Too Long"

**Cause**: Normal growth. Active users hit 300 lines in 2-4 weeks.

**Fix**: During weekly audit, move cold memories to archive files:
```
memory/lessons-learned.md    (for old pitfalls)
memory/projects-archive.md   (for completed projects)
memory/decisions-archive.md  (for old decisions)
```

Leave a reference line in MEMORY.md:
```
- See memory/lessons-learned.md for older pitfalls
```

### "AI Added False Memories"

**Cause**: AI inferred incorrectly or misunderstood.

**Fix**: Say "That's wrong" → AI tags [user-vetoed] → Stops using it.

If AI keeps making the same error, add to pitfalls:
```
- [mistake] AI incorrectly assumed X. Always confirm Y before acting.
```

### "AI Won't Let Me Delete Memories"

**Cause**: AI not following Rule 1 (user authority absolute).

**Fix**: Be explicit:
```
"Delete that entry. This is not a suggestion. Do it now."
```

If AI still refuses, that's a protocol violation. Report it as a bug.

---

## Next Steps

1. **Read the full protocol**: [protocols/core-protocol.md](../protocols/core-protocol.md)
2. **Understand anti-laziness**: [protocols/anti-laziness.md](../protocols/anti-laziness.md)
3. **Set up user audit**: [protocols/user-audit.md](../protocols/user-audit.md)
4. **Browse examples**: [examples/](../examples/)

---

## Quick Reference

```
STARTUP:    Read SOUL.md → MEMORY.md → Logs → Report todos
WORK:       Normal work + self-monitor for laziness
END:        Update log → Extract memories → Update MEMORY.md
WEEKLY:     Audit memory → Move cold items → Confirm unverified
ONGOING:    User says "wrong" → [user-vetoed] → Stop using
```
