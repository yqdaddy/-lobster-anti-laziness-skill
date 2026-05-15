# Vector Search Plugin

> **Purpose**: Add semantic search capability to 龙虾超记忆防偷懒技能.
> **Dependency**: chromadb (or qdrant-client)
> **Status**: Optional — core works without this

---

## Installation

```bash
cd plugins/vector-search
pip install chromadb  # or: pip install qdrant-client
python sync.py --init
```

## Usage

```bash
# Sync all memories to vector index
python sync.py --sync

# Search memories semantically
python sync.py --query "user authentication preferences"

# Results:
# 1. [0.92] "User prefers JWT over session cookies" (MEMORY.md:45)
# 2. [0.85] "Auth module uses OAuth2" (rules/backend.md:12)
```

## How It Works

1. Parses all Markdown files (MEMORY.md, rules/*.md, memory/*.md)
2. Extracts tagged entries ([fact], [preference], etc.)
3. Generates embeddings using lightweight model (all-MiniLM-L6-v2)
4. Stores in local ChromaDB (SQLite backend, no server needed)
5. Searches with cosine similarity + metadata filtering

## Integration with Core

In SOUL.md:
```markdown
## Enabled Plugins
- [x] vector-search
```

AI behavior:
```
When searching for context:
  1. First: Text search in current files (fast)
  2. If no results: Vector search (semantic)
  3. If still no results: Ask user
```

## Storage

```
plugins/vector-search/
├── chroma/              # Local ChromaDB (SQLite)
│   └── chroma.sqlite3
├── sync.py              # Sync script
└── search.py            # Search script
```

**Note**: `chroma/` is gitignored. Each machine rebuilds index from Markdown.
