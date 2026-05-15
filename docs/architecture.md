# Architecture Deep Dive

> **Purpose**: Explain the 6-layer memory architecture, design decisions, and trade-offs.

---

## Why 6 Layers?

The 6-layer architecture balances **speed** (how fast can AI recover context?) with **depth** (how much context is available?).

```
Speed:    ⚡ Fast ────────────────────────────────> Slow 🐢
          L0    L1      L2        L3      L4      L5
Depth:    📝 Shallow ────────────────────────────> Deep 📚
```

| Layer | Read Time | Content Depth | Use Case |
|-------|-----------|---------------|----------|
| L0 | 3 seconds | Ultra-shallow | "Who am I, what are my todos?" |
| L1 | 10 seconds | Shallow | "What are my iron rules?" |
| L2 | 30 seconds | Medium | "What do I know about the user?" |
| L3 | On-demand | Medium-Deep | "What are the project-specific rules?" |
| L4 | 1-2 minutes | Deep | "What did we do yesterday?" |
| L5 | Instant | Full context | Current conversation |

---

## Layer Details

### L0: Boot Snapshot

**Location**: Top of MEMORY.md

**Purpose**: 3-second identity recovery. If AI only reads this, it can function.

**Content**:
- AI name and role
- Top 3-5 active todos
- Top 2-3 active projects
- Iron rules reminder

**Update Trigger**: Every todo change

**Example**:
```markdown
## ⚡ Boot Snapshot
**Who I Am**: 龙虾 🦞, Jacky's AI partner
**Active Todos**:
  1. [TODO] Fix auth bug `deadline: 2026-05-15`
  2. [TODO] Deploy v2.0 `deadline: 2026-05-20`
**Current Projects**:
  - Project Alpha: Backend API (80% complete)
  - Project Beta: Frontend refactor (started)
**Iron Rules**: Read first | Test before guess | 3 failures → switch
```

### L1: Core Identity (SOUL.md)

**Location**: SOUL.md

**Purpose**: Define WHO the AI is. This is the "soul" that persists across all sessions.

**Content**:
- Name, role, user
- Core values (non-negotiable)
- Iron rules (numbered, mandatory)
- Prohibited behaviors
- Emergency protocol

**Update Trigger**: Only when core values change (rare)

**Why separate from MEMORY.md?**
- SOUL.md changes rarely (monthly or less)
- MEMORY.md changes daily
- Separation prevents accidental modification of core rules

### L2: Long-Term Memory (MEMORY.md)

**Location**: MEMORY.md

**Purpose**: The main memory store. Everything that matters across sessions.

**Sections**:
1. Boot Snapshot (L0)
2. User Information
3. Work Environment
4. Todos (tracked across sessions)
5. Projects & Skills
6. Pitfall Experiences
7. Important Decisions
8. Unverified Memories
9. User-Vetoed Memories
10. Accountability Logs

**Update Trigger**: After every substantial task + weekly consolidation

**Bloat Management**: When >300 lines, move cold content to archive files

### L3: Project Rules (rules/*.md)

**Location**: `rules/[project-name].md`

**Purpose**: Domain-specific knowledge. Loaded only when relevant project is mentioned.

**Content**:
- Tech stack and versions
- Architecture decisions
- Coding standards
- Environment setup
- Known issues
- API documentation

**Why modular?**
- Prevents MEMORY.md from growing too large
- Allows project-specific rules without cluttering main memory
- Enables "load on demand" — only read when needed

**Example file tree**:
```
rules/
├── auth-service.md
├── payment-gateway.md
├── frontend-react.md
└── deployment.md
```

### L4: Daily Logs (memory/YYYY-MM-DD.md)

**Location**: `memory/2026-05-14.md`

**Purpose**: Granular record of daily work. Used for recent context recovery.

**Content**:
- Task-by-task breakdown
- Key parameters and configs
- Conclusions and outcomes
- Auto-extraction notes

**Retention**:
- Recent 7 days: Keep full detail
- 7-30 days: Distill to MEMORY.md, keep file
- 30+ days: Archive or delete (user decision)

**Why daily logs?**
- Provides "what did we do yesterday?" context
- Serves as audit trail
- Enables pattern detection ("You always have this error on Mondays")

### L5: Session Memory (System Prompt)

**Location**: AI's context window / system prompt

**Purpose**: Current conversation context. Automatic, no user action needed.

**Limitations**:
- Limited by token budget (varies by model)
- Lost when session ends
- Can override file memories if not careful

**Mitigation**:
- L0-L4 are explicitly read at startup
- Session memory supplements, doesn't replace, file memory

---

## Data Flow

### Session Start

```
User sends message
    ↓
AI reads L0 (3s) → "I am Claw, user is Jacky, 2 todos pending"
    ↓
AI reads L1 (10s) → "My rules are: read first, test before guess..."
    ↓
AI reads L2 (30s) → "Jacky prefers spaces, uses VS Code, works on Project Alpha..."
    ↓
AI reads L4 (1-2min) → "Yesterday we fixed the auth bug, today we need to deploy..."
    ↓
AI checks todos → "2 unfinished: auth bug (due today), deploy (due Friday)"
    ↓
AI responds → "Good morning! We have 2 todos today. Start with auth bug?"
```

### During Work

```
User: "Fix the CORS issue"
    ↓
AI recalls L3 (on-demand) → loads rules/frontend-react.md
    ↓
AI recalls L2 pitfalls → "Last CORS issue was due to missing header..."
    ↓
AI fixes issue
    ↓
AI runs anti-laziness checklist
    ↓
AI updates L4 (today's log)
    ↓
AI extracts memories → updates L2 (MEMORY.md)
```

### Session End

```
User: "That's all for today"
    ↓
AI consolidates L4 → "Today's work worth keeping long-term?"
    ↓
AI updates L0 → "Boot snapshot now shows auth bug as completed"
    ↓
AI checks TTLs → "Any expired entries to mark?"
    ↓
AI checks bloat → "MEMORY.md at 280 lines, no move needed yet"
    ↓
AI says goodbye → "Logged today's work. See you tomorrow!"
```

---

## Design Decisions

### Why Markdown?

| Criterion | Markdown | JSON | YAML | Database |
|-----------|----------|------|------|----------|
| Human readable | ✅ Excellent | ⚠️ Okay | ⚠️ Okay | ❌ No |
| AI readable | ✅ Excellent | ✅ Excellent | ✅ Excellent | ⚠️ Requires API |
| Version control | ✅ Native | ✅ Native | ✅ Native | ❌ Complex |
| Edit anywhere | ✅ Any text editor | ⚠️ IDE | ⚠️ IDE | ❌ Client needed |
| Zero dependencies | ✅ Yes | ✅ Yes | ✅ Yes | ❌ Infrastructure |
| Structured queries | ⚠️ Text search | ✅ Excellent | ✅ Good | ✅ Excellent |

**Trade-off**: We lose structured queries but gain simplicity and transparency.

At 10-1000 entries, text search is sufficient. At 10,000+ entries, consider migrating to Mem0 or SimpleMem.

### Why No Vector Database?

**The scale argument**:
- Personal AI assistant: 50-500 memories
- Small team: 500-2000 memories
- Enterprise chatbot: 10,000+ memories

龙虾超记忆防偷懒技能 targets the first two. For the third, use Mem0 (37k+ GitHub stars).

**The transparency argument**:
- Vector DB: "AI retrieved memory #47 based on cosine similarity 0.82"
- Markdown: "AI read line 23: 'User prefers dark mode'"

The latter is auditable. The former is a black box.

### Why User Veto Instead of AI Self-Correction?

**The paradox**: If AI can correct its own memories, it can also "correct" correct memories into false ones.

**The solution**: User is the ultimate authority. AI can suspect, suggest, but never unilaterally change.

This adds friction (user must confirm corrections) but prevents the "positive feedback loop of falsehood."

---

## Performance Considerations

### Read Performance

| Layer | File Size | Read Time | Frequency |
|-------|-----------|-----------|-----------|
| L0 | ~20 lines | 3s | Every session |
| L1 | ~50 lines | 10s | Every session |
| L2 | ~200 lines | 30s | Every session |
| L3 | ~100 lines | 15s | On-demand |
| L4 | ~50 lines | 1-2min | Every session (recent 2 days) |

**Total startup time**: ~2-3 minutes of reading

**Mitigation**: Asynchronous reading, parallel file access

### Write Performance

| Operation | Frequency | Time |
|-----------|-----------|------|
| Log update | Every task | 10s |
| Memory extraction | Every task | 20s |
| Consolidation | End of session | 1-2min |
| Weekly audit | Weekly | 5min |

**Total daily overhead**: ~5-10 minutes of AI time

**Trade-off**: 5 minutes of discipline → Hours of saved context-recovery time

---

## Scaling Beyond 1000 Entries

When you outgrow 龙虾超记忆防偷懒技能:

### Phase 1: Archive Files (Built-in)
- Move cold memories to `memory/*.md` files
- Keep "hot" memories in MEMORY.md
- Cost: Zero. Still Markdown.

### Phase 2: Hybrid (Claw + Simple Search)
- Keep 龙虾超记忆防偷懒技能 for hot memories
- Add `ripgrep` or `fd` for full-text search across archive files
- Cost: One CLI tool.

### Phase 3: Migrate to Vector DB
- Export Markdown to Mem0 / Chroma
- Keep 龙虾超记忆防偷懒技能 protocol for execution discipline
- Cost: Infrastructure setup.

**Rule of thumb**: When `grep` across your memory files takes >5 seconds, it's time for Phase 2 or 3.

---

## Security Considerations

### Sensitive Data

**NEVER store in MEMORY.md**:
- Passwords
- API keys (unless encrypted)
- Personal identification numbers
- Financial account details

**Safe to store**:
- API endpoint URLs (without keys)
- Project configurations
- User preferences
- Pitfall experiences

**Best practice**: Store sensitive data in environment variables or encrypted vaults. Reference them in MEMORY.md by name only.

### Multi-User Scenarios

龙虾超记忆防偷懒技能 is designed for single-user or small-team use.

For multi-user:
- Each user has their own `MEMORY-[username].md`
- Shared project rules in `rules/*.md`
- Use Git for conflict resolution

For enterprise multi-tenant: Use Mem0 or MemOS instead.

---

## Comparison with Human Memory

| Aspect | Human | 龙虾超记忆防偷懒技能 |
|--------|-------|-------------|
| Capacity | ~1000 active concepts | 10-1000 entries (scalable) |
| Decay | Exponential forgetting | TTL-based expiration |
| Error correction | Slow, biased | Fast, user-vetoed |
| Context recovery | Minutes-hours | 2-3 minutes |
| Auditability | Impossible | Full log |
| Sharing | Verbal, lossy | Git-tracked, exact |

龙虾超记忆防偷懒技能 doesn't replace human memory. It augments it with persistence, auditability, and discipline.
