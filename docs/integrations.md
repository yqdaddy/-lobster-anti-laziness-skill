# Platform Integration Guides

> **Purpose**: Step-by-step setup instructions for different AI platforms and tools.

---

## Claude (Claude Code)

### Setup

1. Install Claude Code:
```bash
npm install -g @anthropic-ai/claude-code
```

2. Create project files:
```bash
# In your project directory
cp lobster-anti-laziness-skill/templates/SOUL.md ./SOUL.md
cp lobster-anti-laziness-skill/templates/MEMORY.md ./MEMORY.md
mkdir -p memory rules
```

3. Configure Claude Code:

Create `.claude.md` in project root:
```markdown
# 龙虾超记忆防偷懒技能 Protocol v3.2

You are following the 龙虾超记忆防偷懒技能 protocol.

## Identity
Read SOUL.md for your identity and iron rules.

## Startup Protocol (MANDATORY)
Before first response:
1. Read SOUL.md
2. Read MEMORY.md (full file)
3. Read memory/YYYY-MM-DD.md (today and yesterday)
4. Check todos in MEMORY.md
5. Report unfinished todos to user

## Work Protocol
- Follow iron rules from SOUL.md
- Run anti-laziness checklist after every task
- Use execution summary template for substantial work
- Extract memories to MEMORY.md after every task

## Memory Rules
- User has absolute authority over all memories
- Tag uncertain info as [unverified]
- Tag user corrections as [user-vetoed]
- Never remove [user-vetoed] or [unverified] tags
- Weekly audit reminder if unaudited for 7+ days
```

4. Start Claude Code:
```bash
claude
```

### Usage

Claude Code will automatically read `.claude.md` at startup. It has full file access, so memory read/write works seamlessly.

### Tips

- Use `/memory` command to quickly check memory status
- Claude Code can edit files directly, so memory updates are automatic
- Use `/todo` to manage todos within the chat interface

---

## ChatGPT / GPT-4

### Method 1: Custom GPT (Recommended for Plus Users)

1. Go to [chatgpt.com](https://chatgpt.com) → "Explore GPTs" → "Create"

2. In "Instructions", paste:
```markdown
You are following the 龙虾超记忆防偷懒技能 protocol v3.2.

## Startup (Before every conversation)
1. Check your knowledge files for SOUL.md and MEMORY.md
2. Read both files completely
3. Summarize: Who is the user? What are active todos? Any preferences?
4. Report todos to user if found

## During Work
- Follow all instructions in SOUL.md
- After every task, run the 6-question anti-laziness checklist
- Provide execution summaries for substantial work

## Memory Management
- User has absolute authority over memories
- Tag uncertain info as [unverified]
- Tag corrections as [user-vetoed]
- Never remove these tags
- Suggest weekly audits
```

3. In "Knowledge", upload:
   - `SOUL.md` (customized)
   - `MEMORY.md` (customized)

4. Enable "Code Interpreter" for file generation

5. Save and use your Custom GPT

### Method 2: Manual (Free Tier)

Since free ChatGPT can't access local files:

1. At start of each conversation, paste:
```
Please follow my memory protocol. Here are my memory files:

[Paste contents of SOUL.md]

[Paste contents of MEMORY.md]
```

2. At end of conversation, ask:
```
Please generate updated MEMORY.md and today's log based on our conversation.
```

3. Copy-paste the generated files back to your local storage

**Note**: This is tedious. Consider upgrading to Plus or using Claude Code instead.

---

## Cursor

### Setup

1. Install Cursor from [cursor.sh](https://cursor.sh)

2. Create `.cursorrules` in project root:
```markdown
# 龙虾超记忆防偷懒技能 Protocol v3.2

## Startup (MANDATORY)
Before responding:
1. Read SOUL.md
2. Read MEMORY.md
3. Read memory/YYYY-MM-DD.md (today and yesterday)
4. Check todos
5. Report unfinished todos

## Work Rules
- Follow SOUL.md iron rules
- Anti-laziness checklist after every task
- Execution summaries for substantial work
- Memory extraction after every task

## User Authority
- User can delete/modify any memory
- Tag uncertain info as [unverified]
- Tag corrections as [user-vetoed]
- Weekly audit reminders
```

3. Create memory files:
```bash
cp lobster-anti-laziness-skill/templates/SOUL.md ./SOUL.md
cp lobster-anti-laziness-skill/templates/MEMORY.md ./MEMORY.md
mkdir -p memory rules
```

### Usage

Cursor reads `.cursorrules` automatically. Use the AI chat panel for memory-related tasks.

### Tips

- Cursor's "Composer" feature can edit multiple files, useful for memory updates
- Use "@" mentions to reference specific memory files
- Enable "Yolo mode" for automatic file edits (with caution)

---

## WorkBuddy

### Setup

1. Copy skill files:
```bash
mkdir -p .workbuddy/skills/lobster-anti-laziness-skill
cp lobster-anti-laziness-skill/protocols/*.md .workbuddy/skills/lobster-anti-laziness-skill/
cp lobster-anti-laziness-skill/templates/*.md .workbuddy/skills/lobster-anti-laziness-skill/
```

2. Reference in WorkBuddy config:
```json
{
  "skills": [
    {
      "name": "lobster-anti-laziness-skill",
      "path": ".workbuddy/skills/lobster-anti-laziness-skill",
      "version": "3.2"
    }
  ]
}
```

3. WorkBuddy will automatically inject the protocol into system prompts

### Usage

WorkBuddy handles memory file paths and read/write timing. The skill provides the structure and execution rules.

---

## Local LLMs (Ollama, LM Studio, etc.)

### Setup

Local LLMs often lack autonomous file tools. Use this workaround:

1. Create a "memory prompt" file:
```bash
cat > memory-prompt.txt << 'EOF'
# MEMORY PROTOCOL

Before responding, you MUST read these files:
- SOUL.md
- MEMORY.md
- memory/YYYY-MM-DD.md

After responding, you MUST:
- Update memory/YYYY-MM-DD.md
- Extract memories to MEMORY.md

Follow all rules in SOUL.md.
EOF
```

2. At start of each session, paste the memory prompt + file contents:
```bash
# Combine prompt and files
cat memory-prompt.txt SOUL.md MEMORY.md > context.txt
```

3. Paste `context.txt` into your local LLM UI

4. After conversation, manually update files based on LLM's output

### Advanced: API Integration

If using Ollama API or similar:

```python
import ollama

def load_memory():
    with open("SOUL.md") as f:
        soul = f.read()
    with open("MEMORY.md") as f:
        memory = f.read()
    return f"{soul}

{memory}"

response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "system", "content": load_memory()},
        {"role": "user", "content": "Fix the auth bug"}
    ]
)
```

---

## VS Code + Extensions

### With Continue.dev

1. Install [Continue.dev](https://continue.dev) extension

2. Configure in `.continue/config.json`:
```json
{
  "system_message": "Follow 龙虾超记忆防偷懒技能 protocol. Read SOUL.md and MEMORY.md before responding."
}
```

3. Use the Continue chat panel with memory-aware prompts

### With GitHub Copilot

Limited integration (Copilot doesn't read arbitrary files):

1. Add to `.github/copilot-instructions.md`:
```markdown
# Copilot Instructions

Follow 龙虾超记忆防偷懒技能 protocol when generating code:
- Check MEMORY.md for user preferences
- Avoid patterns in [mistake] entries
- Follow decisions in [decision] entries
```

2. Copilot will use these instructions for code generation

---

## Obsidian / Logseq (PKM Tools)

### Obsidian

1. Create a vault for AI memory:
```
AI-Memory/
├── SOUL.md
├── MEMORY.md
├── memory/
│   ├── 2026-05-14.md
│   └── 2026-05-15.md
└── rules/
    └── project-alpha.md
```

2. Use Obsidian's search for memory retrieval:
- `tag:preference` to find preferences
- `tag:mistake` to find pitfalls
- `path:memory` to find logs

3. Use templates plugin for daily logs:
```markdown
---
date: {{date:YYYY-MM-DD}}
---

# {{date:YYYY-MM-DD}} Work Log

## Task 1
- What: 
- Key params: 
- Conclusion: 

## Auto-extraction
- [ ] fact
- [ ] preference
- [ ] mistake
- [ ] decision
- [ ] todo
```

### Logseq

1. Create a graph for AI memory
2. Use page properties for entry types:
```markdown
- type:: preference
- ttl:: permanent
- User prefers dark mode
```

3. Use queries to filter memories:
```clojure
#+BEGIN_QUERY
{:title "All Preferences"
 :query [:find (pull ?b [*])
         :where
         [?b :block/properties ?p]
         [(get ?p :type) ?t]
         [(= ?t "preference")]]}
#+END_QUERY
```

---

## GitHub Actions (CI/CD Integration)

### Memory Validation

Add to `.github/workflows/memory-check.yml`:
```yaml
name: Memory Check
on: [push]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Validate MEMORY.md structure
        run: |
          python scripts/validate-memory.py
      - name: Check for orphaned memories
        run: |
          bash scripts/check-integrity.sh
```

---

## Platform Comparison

| Platform | File Access | Automation | Best For |
|----------|-------------|------------|----------|
| Claude Code | ✅ Full | ✅ High | Power users, developers |
| Cursor | ✅ Full | ✅ Medium | Developers, IDE users |
| WorkBuddy | ✅ Full | ✅ High | WorkBuddy ecosystem |
| ChatGPT Plus | ⚠️ Upload only | ⚠️ Manual | Casual users |
| Local LLMs | ❌ None | ❌ Manual | Privacy-focused, tinkerers |
| Obsidian/Logseq | ✅ Full | ❌ Manual | PKM enthusiasts |

---

## Choosing Your Platform

**For developers**: Claude Code or Cursor
**For non-technical users**: ChatGPT Custom GPT (manual file management)
**For privacy**: Local LLM with manual file management
**For PKM integration**: Obsidian or Logseq
**For enterprise**: WorkBuddy or custom API integration
