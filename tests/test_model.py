from copy import deepcopy
from pathlib import Path
from unittest import TestCase

import yaml

from rs_suite.cli import validate
from rs_suite.model import project_index, project_relations, project_tree


ROOT = Path(__file__).resolve().parents[1]


class ProjectModelTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = yaml.safe_load(
            (ROOT / "data" / "suite.yml").read_text(encoding="utf-8")
        )

    def test_current_data_is_valid(self) -> None:
        validate(self.data)
        self.assertNotIn("relations", self.data)
        self.assertNotIn("maintenance", self.data)

    def test_project_owned_relations_include_nested_sources(self) -> None:
        relations = project_relations(project_tree(self.data))
        self.assertIn(
            {
                "from": "github-biotools-bridge",
                "to": "biotools",
                "label": "extract & suggest",
                "bidirectional": True,
            },
            relations,
        )

    def test_duplicate_nested_id_is_rejected(self) -> None:
        data = deepcopy(self.data)
        data["projects"]["bridge"]["projects"]["rs-tools"] = {
            "name": "Duplicate",
            "kind": "component",
            "summary": "Duplicate ID for validation coverage.",
        }
        with self.assertRaisesRegex(ValueError, "globally unique"):
            validate(data)

    def test_nested_maintenance_target_is_resolved(self) -> None:
        projects = project_index(self.data)
        targets = {
            item["project"]
            for project in projects.values()
            for item in project.get("maintenance", [])
        }
        self.assertIn("github-biotools-bridge", targets)
        self.assertIn("github-rsm-bridge", targets)

    def test_nested_project_cannot_leave_its_parent_stage(self) -> None:
        data = deepcopy(self.data)
        data["projects"]["bridge"]["projects"]["github-rsm-bridge"]["stage"] = "plan"
        with self.assertRaisesRegex(ValueError, "parent's stage"):
            validate(data)
