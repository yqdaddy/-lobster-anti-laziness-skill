# Frequently Asked Questions

---

## General Questions

### Q: Is 龙虾超记忆防偷懒技能 a software or a protocol?

**A**: It's primarily a **protocol/framework** — a set of rules and templates for organizing AI memory using Markdown files. We include optional helper scripts, but the core value is the execution discipline, not the code.

### Q: Do I need to install anything?

**A**: No. 龙虾超记忆防偷懒技能 is zero-dependency. You need:
- A text editor (VS Code, Vim, Notepad, anything)
- An AI assistant that can read/write files
- That's it.

### Q: How is this different from Mem0 or LangChain Memory?

**A**: 

| Feature | 龙虾超记忆防偷懒技能 | Mem0 | LangChain |
|---------|-------------|------|-----------|
| Setup | Zero | pip install + config | Framework integration |
| Storage | Markdown files | Vector database | Variable |
| Scale | Personal (10-1000 entries) | Enterprise (10K+) | Medium |
| Human readable | Native | Requires export | Serialized |
| Anti-laziness | Built-in | No | No |
| User audit | Hard rules | Partial | Partial |

**Use 龙虾超记忆防偷懒技能** if you want simplicity, transparency, and discipline.
**Use Mem0** if you need enterprise scale or vector search.

---

## Setup Questions

### Q: Can I use this with ChatGPT (web interface)?

**A**: Limited. ChatGPT web can't read/write local files. Options:
1. **Custom GPT**: Upload SOUL.md and MEMORY.md as knowledge files
2. **ChatGPT Plus with Code Interpreter**: AI can generate file updates, you manually apply them
3. **API**: Use OpenAI API with file tools (requires coding)

Best experience: Claude (Claude Code), Cursor, or WorkBuddy.

### Q: Can I use this with local LLMs (Ollama, etc.)?

**A**: Yes! As long as your setup supports:
- System prompt injection (for startup protocol)
- File read/write capabilities

You may need to manually trigger memory reads/writes since local LLMs often lack autonomous file tools.

### Q: Where should I put the files?

**A**: Recommended structure:
```
~/my-project/
├── SOUL.md              # AI identity
├── MEMORY.md            # Main memory
├── memory/              # Daily logs
│   ├── 2026-05-14.md
│   └── 2026-05-15.md
└── rules/               # Project rules
    └── my-project.md
```

Or in your home directory for global AI memory:
```
~/
├── SOUL.md
├── MEMORY.md
└── memory/
```

---

## Usage Questions

### Q: What if AI refuses to read memory at startup?

**A**: Be strict. Say:
```
"Stop. You didn't read MEMORY.md. This is Rule 0. Read it now before responding."
```

If AI still refuses, that's a platform limitation. Consider:
- Adding stronger instructions in system prompt
- Using a platform with better file tool support (Claude Code, Cursor)
- Opening an issue with the AI platform

### Q: What if AI adds false memories?

**A**: Say "That's wrong" or "I never said that." The AI must:
1. Tag the entry [user-vetoed]
2. Stop using it
3. Log the correction

If AI keeps making the same error, add a [mistake] entry about it.

### Q: Can I delete memories?

**A**: **Absolutely.** You have absolute authority. AI cannot refuse deletion requests.

If AI says "This memory is important, are you sure?", respond:
```
"Delete it. This is not a suggestion. Do it now."
```

### Q: How often should I audit?

**A**: Weekly (Monday mornings). Takes 2 minutes.

If you skip audits, false memories accumulate. If you audit too often, it becomes annoying.

### Q: What if I have multiple projects?

**A**: Use the modular rules system:
```
rules/
├── project-alpha.md
├── project-beta.md
└── shared-standards.md
```

MEMORY.md tracks cross-project todos and global preferences.
Project-specific rules are loaded on-demand.

---

## Technical Questions

### Q: Won't Markdown get slow at scale?

**A**: At 10-1000 entries, no. Text search is instant.

At 1000+ entries:
- Use archive files (built-in "move" rule)
- Use `ripgrep` for search
- Consider migrating to Mem0

### Q: Can I use Git for version control?

**A**: **Highly recommended.** Git provides:
- History of memory changes
- Rollback to previous states
- Diff view for audits
- Backup

```bash
git init
git add SOUL.md MEMORY.md memory/ rules/
git commit -m "Initial 龙虾超记忆防偷懒技能 setup"
```

### Q: What about sensitive data (API keys, passwords)?

**A**: **Never store sensitive data in MEMORY.md.**

Safe alternatives:
- Environment variables (`.env` file, gitignored)
- Password managers (1Password, Bitwarden)
- Encrypted vaults

In MEMORY.md, reference by name only:
```markdown
- [fact] API key stored in environment variable `API_KEY`
```

### Q: Can multiple AIs share the same memory?

**A**: Yes, but with caveats:
- All AIs must follow the same protocol version
- Use Git for conflict resolution
- Each AI should identify itself in logs

For multi-user teams, consider separate personal memories + shared project rules.

---

## Troubleshooting

### Q: AI says "I don't have file access"

**A**: Your platform doesn't support file tools. Options:
1. Switch to Claude Code, Cursor, or WorkBuddy
2. Use API-based setup with file tools
3. Manually copy-paste memory content into context

### Q: MEMORY.md is getting too long

**A**: This is normal. Use the "move" rule:
```
MEMORY.md >300 lines → Move cold content to archive files
```

Archive files:
- `memory/lessons-learned.md` (old pitfalls)
- `memory/projects-archive.md` (completed projects)
- `memory/decisions-archive.md` (old decisions)

### Q: AI keeps forgetting my preferences

**A**: Check:
1. Is the preference tagged? `[preference]` not just plain text
2. Is it in boot snapshot? Critical preferences should be in L0
3. Is AI reading memory? Verify Rule 0 compliance

### Q: AI is getting worse over time

**A**: Memory pollution. Emergency steps:
1. Full audit of MEMORY.md
2. Tag all false memories [user-vetoed]
3. Check for propagation to other files
4. Add prevention entries
5. Resume weekly audits

---

## Philosophy Questions

### Q: Why "anti-laziness"? Isn't that insulting to AI?

**A**: "Laziness" is a technical term for "shortcut-taking behavior." All LLMs exhibit this:
- Skipping verification
- Merging steps
- Guessing instead of testing

The framework names the behavior so we can detect and correct it. It's not personal.

### Q: Why does the user need to audit? Shouldn't AI be self-correcting?

**A**: The "self-supervision paradox": AI checking itself is like a student grading their own exam. Without external validation, errors accumulate.

User audit is the external validation layer. It's 2 minutes per week for significantly better AI performance.

### Q: Why Markdown and not a database?

**A**: Three reasons:
1. **Transparency**: You can read and edit your AI's memory
2. **Simplicity**: No setup, no dependencies, no infrastructure
3. **Version control**: Git tracks every change

At personal scale (10-1000 entries), Markdown is sufficient. At enterprise scale, use Mem0.

### Q: Will this work with future AI models?

**A**: The protocol is model-agnostic. It relies on:
- File read/write capabilities
- Instruction following
- Structured output

These capabilities are improving, not degrading, across models.

---

## Contributing Questions

### Q: Can I modify the protocol for my use case?

**A**: Absolutely! The MIT license allows modification. We encourage:
- Domain-specific adaptations (medical, legal, education)
- Cultural adaptations
- Platform-specific integrations

Share your adaptations back to the community!

### Q: How do I report a bug?

**A**: Open an issue with:
- Protocol version
- Platform (Claude, GPT, etc.)
- What happened
- What should have happened
- Your MEMORY.md structure (anonymized)

### Q: Can I add new laziness types?

**A**: Yes! The 6 types are a starting point. If you discover a new pattern:
1. Open an issue describing the pattern
2. Provide examples
3. Suggest detection and fix strategies

---

## Still Have Questions?

- **Read the docs**: [getting-started.md](getting-started.md), [architecture.md](architecture.md), [best-practices.md](best-practices.md)
- **Check examples**: [examples/](../examples/)
- **Open an issue**: We respond to all questions
- **Join discussions**: Share your setup and learn from others
