#!/bin/bash
# 龙虾超记忆防偷懒技能 Integrity Checker
# Checks for orphaned memories and cross-file consistency

echo "龙虾超记忆防偷懒技能 Integrity Check"
echo "==========================="

# Check 1: MEMORY.md exists
if [ ! -f "MEMORY.md" ]; then
    echo "❌ MEMORY.md not found"
    exit 1
fi

echo "✅ MEMORY.md found"

# Check 2: SOUL.md exists
if [ ! -f "SOUL.md" ]; then
    echo "⚠️  SOUL.md not found (optional but recommended)"
else
    echo "✅ SOUL.md found"
fi

# Check 3: Memory directory exists
if [ ! -d "memory" ]; then
    echo "⚠️  memory/ directory not found (creating...)"
    mkdir -p memory
else
    LOG_COUNT=$(ls memory/*.md 2>/dev/null | wc -l)
    echo "✅ memory/ directory found ($LOG_COUNT log files)"
fi

# Check 4: Rules directory
if [ ! -d "rules" ]; then
    echo "⚠️  rules/ directory not found (optional)"
else
    RULE_COUNT=$(ls rules/*.md 2>/dev/null | wc -l)
    echo "✅ rules/ directory found ($RULE_COUNT rule files)"
fi

# Check 5: Check for broken references
echo ""
echo "Checking references..."
if grep -n "See memory/" MEMORY.md > /dev/null 2>&1; then
    grep -n "See memory/" MEMORY.md | while read line; do
        REF=$(echo "$line" | grep -o 'memory/[^`]*')
        if [ ! -f "$REF" ]; then
            echo "❌ Broken reference: $REF"
        fi
    done
fi

# Check 6: Check for [user-vetoed] propagation
echo ""
echo "Checking [user-vetoed] propagation..."
VETOED_COUNT=$(grep -c "\[user-vetoed\]" MEMORY.md 2>/dev/null || echo "0")
echo "Found $VETOED_COUNT [user-vetoed] entries in MEMORY.md"

if [ -d "memory" ]; then
    for file in memory/*.md; do
        if [ -f "$file" ]; then
            COUNT=$(grep -c "\[user-vetoed\]" "$file" 2>/dev/null || echo "0")
            if [ "$COUNT" -gt 0 ]; then
                echo "  Found $COUNT [user-vetoed] in $(basename $file)"
            fi
        fi
    done
fi

# Check 7: Line count warning
LINE_COUNT=$(wc -l < MEMORY.md)
if [ "$LINE_COUNT" -gt 300 ]; then
    echo ""
    echo "⚠️  WARNING: MEMORY.md has $LINE_COUNT lines (>300)"
    echo "   Consider archiving old entries"
fi

echo ""
echo "Integrity check complete"
