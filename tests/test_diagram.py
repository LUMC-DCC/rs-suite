from pathlib import Path
import subprocess
from unittest import TestCase

import yaml

from rs_suite.diagram import diagram_context, normalize_relations
from rs_suite.model import project_index, project_relations, project_tree, walk_projects


ROOT = Path(__file__).resolve().parents[1]


class DiagramTemplateTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = yaml.safe_load((ROOT / "data" / "suite.yml").read_text(encoding="utf-8"))
        cls.context = diagram_context(cls.data)

    def test_every_project_is_in_exactly_one_category(self) -> None:
        project_ids = [
            project["id"]
            for stage in self.context["stages"]
            for project in walk_projects(stage["projects"])
        ]
        self.assertCountEqual(project_ids, project_index(self.data))

    def test_every_relationship_has_a_renderable_edge(self) -> None:
        relations = normalize_relations(project_relations(project_tree(self.data)))
        self.assertEqual(len(self.context["relations"]), len(relations))
        self.assertEqual(
            {relation["id"] for relation in self.context["relations"]},
            {f"relation-{index}" for index in range(len(relations))},
        )

    def test_lifecycle_edges_constrain_the_layout_in_their_forward_direction(self) -> None:
        stage_order = {
            stage_id: stage["order"] for stage_id, stage in self.data["stages"].items()
        }
        project_stage = {
            project_id: project["stage"]
            for project_id, project in project_index(self.data).items()
        }
        for relation in self.context["relations"]:
            expected = (
                stage_order[project_stage[relation["from"]]]
                <= stage_order[project_stage[relation["to"]]]
            )
            self.assertEqual(relation["forward"], expected)
        self.assertTrue(
            all(
                relation["label_html"] and relation["tooltip"]
                for relation in self.context["relations"]
            )
        )

    def test_projects_with_urls_remain_clickable(self) -> None:
        source_projects = project_index(self.data)
        for stage in self.context["stages"]:
            for project in walk_projects(stage["projects"]):
                source = source_projects[project["id"]]
                self.assertEqual(
                    project["url"], source.get("url") or source.get("repository")
                )

    def test_nested_projects_inherit_stage_and_maintainers(self) -> None:
        projects = project_index(self.data)
        bridge = projects["bridge"]
        for project_id in ("github-biotools-bridge", "github-rsm-bridge"):
            child = projects[project_id]
            self.assertEqual(child["parent_id"], "bridge")
            self.assertEqual(child["stage"], bridge["stage"])
            self.assertEqual(child["maintained_by"], bridge["maintained_by"])

    def test_generated_svg_contains_categories_edges_and_project_links(self) -> None:
        subprocess.run(
            ["poetry", "run", "suite-docs", "generate"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        svg = (ROOT / "docs" / "assets" / "suite.svg").read_text(encoding="utf-8")
        self.assertIn('role="img"', svg)
        architecture = (ROOT / "docs" / "developers" / "index.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("### How to read the map", architecture)
        self.assertIn("Dashed arrow", architecture)
        self.assertIn("Arrowheads at both ends", architecture)
        for stage in self.context["stages"]:
            self.assertIn(f'id="stage&#45;{stage["id"]}"', svg)
        self.assertIn('id="project&#45;bridge"', svg)
        self.assertIn('id="project&#45;github&#45;biotools&#45;bridge"', svg)
        self.assertIn('id="project&#45;github&#45;rsm&#45;bridge"', svg)
        for relation in self.context["relations"]:
            self.assertIn(f'id="a_relation&#45;{relation["id"].split("-")[-1]}"', svg)
        for stage in self.context["stages"]:
            for project in walk_projects(stage["projects"]):
                if project["url"]:
                    self.assertIn(project["url"], svg)
