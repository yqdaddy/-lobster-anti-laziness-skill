#!/usr/bin/env python3
"""
龙虾超记忆防偷懒技能 Validator

Validates MEMORY.md structure and integrity.
Usage: python validate-memory.py [path/to/MEMORY.md]
"""

import sys
import re
from pathlib import Path
from datetime import datetime


def validate_memory_file(filepath: str) -> list:
    """Validate a MEMORY.md file and return list of issues."""
    issues = []
    path = Path(filepath)

    if not path.exists():
        return [f"File not found: {filepath}"]

    content = path.read_text(encoding="utf-8")
    lines = content.split("
")

    # Check 1: Has boot snapshot
    if "## ⚡ Boot Snapshot" not in content:
        issues.append("Missing '⚡ Boot Snapshot' section (L0)")

    # Check 2: Has required sections
    required_sections = [
        "## User Information",
        "## Todos",
        "## Pitfall Experiences",
        "## Important Decisions",
        "## Unverified Memories",
        "## User-Vetoed Memories",
        "## Audit Log",
    ]
    for section in required_sections:
        if section not in content:
            issues.append(f"Missing required section: {section}")

    # Check 3: Entries have proper tags
    entry_pattern = r"^- \*\[(fact|preference|todo|mistake|decision|unverified|user-vetoed)\]\*"
    untagged_entries = []
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("- ") and not re.match(entry_pattern, line.strip()):
            if any(keyword in line for keyword in ["preference", "todo", "mistake", "fact", "decision"]):
                untagged_entries.append(f"Line {i}: {line.strip()[:60]}...")

    if untagged_entries:
        issues.append(f"Found {len(untagged_entries)} potentially untagged entries")
        issues.extend(untagged_entries[:5])  # Show first 5

    # Check 4: TTL format
    ttl_pattern = r"`TTL: (permanent|\d+ days)`"
    entries_without_ttl = []
    for i, line in enumerate(lines, 1):
        if re.match(entry_pattern, line.strip()) and "TTL:" not in line and "deadline:" not in line:
            if "[todo]" not in line:  # Todos use deadline instead
                entries_without_ttl.append(f"Line {i}: {line.strip()[:60]}...")

    if entries_without_ttl:
        issues.append(f"Found {len(entries_without_ttl)} entries without TTL")
        issues.extend(entries_without_ttl[:5])

    # Check 5: Date format in audit log
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    audit_section = False
    for i, line in enumerate(lines, 1):
        if "## Audit Log" in line:
            audit_section = True
        elif audit_section and line.startswith("## "):
            audit_section = False
        elif audit_section and line.strip().startswith("-"):
            if not re.search(date_pattern, line):
                issues.append(f"Line {i}: Audit log entry missing date format")

    # Check 6: File size warning
    if len(lines) > 300:
        issues.append(f"WARNING: File has {len(lines)} lines. Consider archiving (>300).")

    # Check 7: Last updated date
    if "**Last Updated**:" not in content:
        issues.append("Missing 'Last Updated' timestamp")

    return issues


def main():
    filepath = sys.argv[1] if len(sys.argv) > 1 else "MEMORY.md"

    print(f"Validating: {filepath}")
    print("=" * 50)

    issues = validate_memory_file(filepath)

    if not issues:
        print("✅ All checks passed!")
        return 0

    print(f"❌ Found {len(issues)} issue(s):
")
    for issue in issues:
        print(f"  • {issue}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
