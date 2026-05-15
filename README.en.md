# 🦞 Lobster Anti-Laziness Skill — AI Execution Discipline Framework

> **Core Difference**: This is NOT another "make AI remember stuff" tool. This is an **AI execution discipline framework that prevents laziness**.
> 
> **Design Philosophy**: The most advanced memory technology + poor execution = garbage. The simplest Markdown + strict anti-laziness discipline = gets better with use.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-4.0.0-blue.svg)](CHANGELOG.md)
[![Skill Type](https://img.shields.io/badge/skill-anti--laziness-red.svg)](protocols/anti-laziness.md)

[中文](./README.md) | **English**

---

## Why "Anti-Laziness"?

All AI memory tools solve the "remembering" problem, but **none solve the "execution" problem**.

| Problem | Other Memory Tools | Lobster Skill |
|---------|-------------------|---------------|
| AI skips memory reading | ❌ Can't detect | ✅ **6-question self-check, missing one = laziness** |
| AI bypasses errors without fixing | ❌ Can't detect | ✅ **Skip-type detection, switch only after 3 failures** |
| AI believes user blindly | ❌ Can't detect | ✅ **Gullible-type detection, must cross-verify** |
| AI does work but omits key output | ❌ Can't detect | ✅ **Surface-type detection, mandatory execution summary** |
| AI compresses multiple steps into one | ❌ Can't detect | ✅ **Merge-type detection, step-by-step output required** |
| AI guesses instead of testing | ❌ Can't detect | ✅ **Guess-type detection, test instead of guess** |
| AI gives conclusions without derivation | ❌ Can't detect | ✅ **Omit-type detection, full reasoning chain required** |
| AI uses stale memory for fresh problems | ❌ Can't detect | ✅ **Cache-type detection, must verify timeliness** |
| AI extracts too many low-confidence memories | ❌ Can't detect | ✅ **Over-type detection, pause and ask user** |

**Lobster = Always working, never lazy.**

---

## This is NOT a Memory Tool, This is AI's "Labor Discipline"

### Three-Layer Protection System

```
┌─────────────────────────────────────────┐
│  Layer 1: Memory Not Lost (6-layer arch)  │  ← Others have this
├─────────────────────────────────────────┤
│  Layer 2: Execution Not Lazy (8 types)    │  ← Only Lobster has ✅
├─────────────────────────────────────────┤
│  Layer 3: User Can Audit (veto + logs)    │  ← Only Lobster has ✅
└─────────────────────────────────────────┘
```

**Other tools = Layer 1 (memory storage)**
**Lobster Skill = Layer 1 + Layer 2 + Layer 3 (memory + execution + audit)**

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Create Memory Files

```bash
cp templates/SOUL.md ./SOUL.md
cp templates/MEMORY.md ./MEMORY.md
mkdir -p memory rules
```

### Step 2: Configure AI Identity (SOUL.md)

```markdown
# Agent Identity

**Name**: Lobster 🦞
**Role**: AI Anti-Laziness Supervisor + Coding Partner
**User**: [Your name]
**Language**: [Your language]

## Core Iron Rules
1. Read MEMORY.md before every session (amnesia = negligence)
2. Run 6-question self-check after every task (missing one = laziness)
3. User owns final interpretation of all memories
4. Tag uncertain info as [unverified]
5. Tag corrections as [user-vetoed] and permanently stop using
```

### Step 3: Start Using

Tell your AI: *"You are now the Lobster Anti-Laziness Supervisor. After every task, you must answer the 6 questions. Missing one is laziness."*

---

## 🦞 Anti-Laziness Framework v4.0 (8 Types)

| # | Laziness Type | Typical Behavior | Does Your AI Do This? | Fix Strategy |
|---|--------------|------------------|----------------------|--------------|
| 1 | **Skip** | Bypass broken tools/APIs | "This API seems down, let me try another way" | Diagnose first, switch after 3 failures |
| 2 | **Gullible** | Believe user blindly without verification | "You're right, I'll do exactly that" | Cross-verify, official docs > user claims |
| 3 | **Surface** | Do work but omit key output | Only give conclusions without process | Mandatory execution summary |
| 4 | **Merge** | Compress multiple steps into one sentence | "Then processed it and it worked" | Step-by-step output, each verifiable |
| 5 | **Guess** | Guess instead of testing | "It should be because of X" | Test instead of guess, script validation |
| 6 | **Omit** | Only results, no derivation | Give answer directly | Must show full reasoning chain |
| 7 | **Cache** | Use stale memory for fresh problems | "Based on previous experience..." (3 months old) | Verify timeliness, mark [stale] if outdated |
| 8 | **Over** | Extract too many low-confidence memories | Extract 10 "preferences" at once | Pause extraction, ask user to confirm |

### 6-Question Self-Check (Mandatory After Every Task)

```
□ Are all steps completed?     → Checklist item-by-item
□ Are all tools passing?       → Check for unhandled errors
□ Are results validated?       → No "should be fine" mentality
□ Is everything output?        → Done = said
□ Is memory written?           → Today's log updated
□ Are user claims verified?    → Independent confirmation

All pass = qualified, missing one = laziness
```

---

## 🛡️ User Audit Mechanism (External Defense)

### The Self-Supervision Paradox

> All AI iron rules are AI self-constrained. If AI "forgets" the checklist, "judges" something unimportant, or "decides" something expired should be deleted — the entire system lacks external enforcement.

**Solution: User holds ultimate authority.**

### Four Hard Rules

| Hard Rule | Description |
|-----------|-------------|
| **Audit Right** | User can view/modify/delete ANY entry. AI cannot refuse. |
| **Weekly Reminder** | Every Monday if unaudited for 7+ days, AI must remind. |
| **Veto Mechanism** | User says "wrong" → AI marks [user-vetoed], stops using forever. |
| **Audit Log** | Maintained in MEMORY.md: `YYYY-MM-DD | user audit | confirmed/vetoed/added` |

---

## 📊 Comparison with "Pure Memory" Tools

| Dimension | Pure Memory Tools (Mem0/Chroma) | Lobster Anti-Laziness Skill |
|-----------|--------------------------------|----------------------------|
| **Core Goal** | Make AI "remember" | Make AI "remember AND execute without laziness" |
| **Memory Storage** | ✅ Vector database | ✅ Markdown files |
| **Memory Reading** | ⚠️ Depends on AI's consciousness | ✅ **Mandatory reading, skipping = negligence** |
| **Execution Supervision** | ❌ None | ✅ **8-type laziness detection** |
| **Process Verification** | ❌ None | ✅ **6-question self-check** |
| **Error Correction** | ❌ AI judges itself | ✅ **User veto hard rule** |
| **Audit Trail** | ❌ None | ✅ **Accountability log + audit records** |
| **Transparency** | ❌ Black-box database | ✅ **Every line readable and editable** |
| **Dependencies** | ❌ Requires infrastructure | ✅ **Zero dependencies** |

**Analogy**:
- Pure memory tools = Give AI a notebook (whether they use it is up to them)
- Lobster skill = Give AI a notebook + a supervisor (must write, must read, must verify, user can audit anytime)

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

> **Statement**: This is an **execution discipline framework**, not software. The "code" is the discipline of execution. The files are the memory. The user is the ultimate authority.

---

## 💬 Community

- **Issues**: Bug reports, feature requests, protocol discussions
- **Discussions**: Share your setup, ask questions, show examples

**Star ⭐ this repo if it makes your AI less lazy!**
