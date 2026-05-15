#!/usr/bin/env python3
"""
龙虾超记忆防偷懒技能 Protocol Tests

Tests to validate protocol compliance.
"""

import unittest
from pathlib import Path
import re


class TestMemoryStructure(unittest.TestCase):
    """Test MEMORY.md structure compliance."""

    def setUp(self):
        self.memory_path = Path("templates/MEMORY.md")
        if self.memory_path.exists():
            self.content = self.memory_path.read_text(encoding="utf-8")
        else:
            self.content = ""

    def test_has_boot_snapshot(self):
        """L0: Must have boot snapshot."""
        self.assertIn("## ⚡ Boot Snapshot", self.content)

    def test_has_required_sections(self):
        """L2: Must have all required sections."""
        required = [
            "## User Information",
            "## Todos",
            "## Pitfall Experiences",
            "## Important Decisions",
        ]
        for section in required:
            self.assertIn(section, self.content)

    def test_entry_tags_present(self):
        """Entries must have type tags."""
        tags = ["[fact]", "[preference]", "[todo]", "[mistake]", "[decision]"]
        found = any(tag in self.content for tag in tags)
        self.assertTrue(found, "No entry tags found")


class TestAntiLaziness(unittest.TestCase):
    """Test anti-laziness protocol compliance."""

    def test_six_questions_defined(self):
        """Must define 6 self-check questions."""
        protocol_path = Path("protocols/anti-laziness.md")
        if protocol_path.exists():
            content = protocol_path.read_text(encoding="utf-8")
            # Check for 6 questions
            questions = [
                "Steps done",
                "Tools passing",
                "Results validated",
                "Everything output",
                "Memory written",
                "Claims verified",
            ]
            for q in questions:
                self.assertIn(q, content)


class TestUserAudit(unittest.TestCase):
    """Test user audit protocol compliance."""

    def test_veto_mechanism_defined(self):
        """Must define user veto mechanism."""
        protocol_path = Path("protocols/user-audit.md")
        if protocol_path.exists():
            content = protocol_path.read_text(encoding="utf-8")
            self.assertIn("[user-vetoed]", content)
            self.assertIn("user audit", content.lower())


class TestTemplates(unittest.TestCase):
    """Test template files."""

    def test_soul_template_exists(self):
        """SOUL.md template must exist."""
        self.assertTrue(Path("templates/SOUL.md").exists())

    def test_memory_template_exists(self):
        """MEMORY.md template must exist."""
        self.assertTrue(Path("templates/MEMORY.md").exists())


if __name__ == "__main__":
    unittest.main()
