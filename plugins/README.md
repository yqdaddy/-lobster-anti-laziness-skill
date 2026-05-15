# 龙虾超记忆防偷懒技能 Plugins

> **Philosophy**: Core is zero-dependency. Plugins are optional enhancements.
> **Rule**: Uninstalling any plugin must never break core functionality.

---

## Available Plugins

| Plugin | Purpose | Dependencies | Size Impact |
|--------|---------|--------------|-------------|
| **vector-search** | Semantic memory search | chromadb (pip) | +50MB |
| **compression-helper** | Memory analysis & suggestions | None | +0MB |
| **audit-report** | HTML health dashboard | None | +0MB |
| **sync** | Cross-machine sync | git (system) | +0MB |

## Installing Plugins

```bash
# Install single plugin
cd plugins/vector-search
pip install -r requirements.txt

# Or install all
./scripts/install-plugins.sh
```

## Enabling Plugins

In `SOUL.md`:
```markdown
## Enabled Plugins
- [x] vector-search
- [x] compression-helper
- [ ] audit-report      # Disabled
- [x] sync
```

AI reads this section and adjusts behavior accordingly.

## Creating Custom Plugins

```bash
mkdir plugins/my-plugin
cat > plugins/my-plugin/README.md << 'EOF'
# My Plugin

> **Purpose**: [Description]
> **Dependency**: [If any]
> **Hook**: [When it runs]

## API

def hook_startup(memory_file):
    # Called at AI startup
    pass

def hook_post_task(memory_file, task_result):
    # Called after each task
    pass

def hook_audit(memory_file):
    # Called during weekly audit
    pass
EOF
```

## Plugin Hooks

| Hook | When Called | Use Case |
|------|-------------|----------|
| `startup` | AI session start | Load external context |
| `pre_task` | Before task execution | Inject relevant memories |
| `post_task` | After task completion | Extract to external system |
| `audit` | Weekly audit | Generate external reports |
| `sync` | Manual trigger | Cross-machine sync |

## Security Note

Plugins run with same permissions as AI. Only install plugins from trusted sources.
