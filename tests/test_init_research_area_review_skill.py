from __future__ import annotations

import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "init_research_area_review_skill.py"
SPEC = importlib.util.spec_from_file_location("init_research_area_review_skill", SCRIPT)
assert SPEC is not None
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class InitResearchAreaReviewSkillTest(unittest.TestCase):
    def test_rejects_path_traversal_skill_name(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            spec_path = tmp_path / "spec.json"
            bank_path = tmp_path / "bank.md"
            logic_path = tmp_path / "logic.md"
            output_dir = tmp_path / "out"

            spec_path.write_text('{"area_name": "Test Area"}', encoding="utf-8")
            bank_path.write_text("# Bank\n", encoding="utf-8")
            logic_path.write_text("# Logic\n", encoding="utf-8")

            with self.assertRaises(ValueError):
                MODULE.main(
                    [
                        "--spec",
                        str(spec_path),
                        "--output-dir",
                        str(output_dir),
                        "--skill-name",
                        "../outside",
                        "--bank",
                        str(bank_path),
                        "--subtle-logic",
                        str(logic_path),
                    ]
                )

            self.assertFalse((tmp_path / "outside").exists())

    def test_accepts_slug_skill_name(self) -> None:
        self.assertEqual(
            MODULE.validate_skill_name("graph-reviewer-openreview"),
            "graph-reviewer-openreview",
        )

    def test_generates_skill_with_valid_name(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            spec_path = tmp_path / "spec.json"
            bank_path = tmp_path / "bank.md"
            logic_path = tmp_path / "logic.md"
            output_dir = tmp_path / "out"

            spec_path.write_text('{"area_name": "Test Area"}', encoding="utf-8")
            bank_path.write_text("# Bank\n", encoding="utf-8")
            logic_path.write_text("# Logic\n", encoding="utf-8")

            with redirect_stdout(io.StringIO()):
                result = MODULE.main(
                    [
                        "--spec",
                        str(spec_path),
                        "--output-dir",
                        str(output_dir),
                        "--skill-name",
                        "test-area-reviewer",
                        "--bank",
                        str(bank_path),
                        "--subtle-logic",
                        str(logic_path),
                    ]
                )

            skill_dir = output_dir / "test-area-reviewer"
            self.assertEqual(result, 0)
            self.assertTrue((skill_dir / "SKILL.md").exists())
            self.assertTrue(
                (skill_dir / "references" / "openreview_review_response_bank.md").exists()
            )


if __name__ == "__main__":
    unittest.main()
