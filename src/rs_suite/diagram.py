from __future__ import annotations

from html import escape
import json
import textwrap

from .model import project_relations, project_tree, walk_projects


STAGE_STYLES = [
    {"border": "#5787a5", "fill": "#f3f9fd"},
    {"border": "#7864b0", "fill": "#f8f5fd"},
    {"border": "#4f9374", "fill": "#f3faf6"},
    {"border": "#b67a5d", "fill": "#fff7f1"},
]

KIND_FILLS = {
    "component": "#dceffc",
    "support": "#eeeeef",
    "community": "#f7dced",
    "external": "#ffe2d2",
    "artifact": "#e6e6e9",
}

def normalize_relations(relations: list[dict]) -> list[dict]:
    """Collapse reciprocal pairs into one labelled, bidirectional edge."""
    reverse_indexes = {
        (relation["from"], relation["to"]): index
        for index, relation in enumerate(relations)
        if not relation.get("bidirectional")
    }
    normalized = []
    consumed: set[int] = set()
    for index, relation in enumerate(relations):
        if index in consumed:
            continue
        reverse_index = reverse_indexes.get((relation["to"], relation["from"]))
        if reverse_index is None or reverse_index == index:
            normalized.append(dict(relation))
            continue

        reverse = relations[reverse_index]
        consumed.add(reverse_index)
        merged = dict(relation)
        merged["bidirectional"] = True
        merged["label"] = f"{relation['label']} / {reverse['label']}"
        merged["tooltip"] = (
            f"{relation['from']} → {relation['to']}: {relation['label']}; "
            f"{reverse['from']} → {reverse['to']}: {reverse['label']}"
        )
        if relation.get("type") != reverse.get("type"):
            merged.pop("type", None)
        normalized.append(merged)
    return normalized


def dot_string(value: object) -> str:
    """Quote a value safely for a DOT attribute."""
    return json.dumps(str(value), ensure_ascii=False)


def html_label(value: object, width: int = 28) -> str:
    """Create a wrapped Graphviz HTML label without allowing markup."""
    lines = textwrap.wrap(
        str(value),
        width=width,
        break_long_words=False,
        break_on_hyphens=False,
    ) or [""]
    return "<BR/>".join(escape(line) for line in lines)


def diagram_context(data: dict) -> dict:
    """Prepare semantic YAML data for the maintainable DOT template."""
    tree = project_tree(data)
    flat_projects = list(walk_projects(tree))
    project_stage = {
        project["id"]: project["stage"] for project in flat_projects
    }
    project_containers = {
        project["id"]: bool(project["projects"]) for project in flat_projects
    }
    stages = []
    ordered_stages = sorted(
        data["stages"].items(), key=lambda item: item[1]["order"]
    )
    stage_order = {
        stage_id: stage["order"] for stage_id, stage in data["stages"].items()
    }
    for index, (stage_id, stage) in enumerate(ordered_stages):
        def prepare(project: dict) -> dict:
            return {
                **project,
                "label": html_label(project["name"]),
                "url": project.get("url") or project.get("repository"),
                "status": project.get("status", "active"),
                "fill": KIND_FILLS.get(project.get("kind", "component"), "#dceffc"),
                "projects": [prepare(child) for child in project["projects"]],
                "container": bool(project["projects"]),
            }

        projects = [
            prepare(project) for project in tree if project["stage"] == stage_id
        ]
        stages.append(
            {
                **stage,
                "id": stage_id,
                "projects": projects,
                **STAGE_STYLES[index % len(STAGE_STYLES)],
            }
        )

    relations = []
    for index, relation in enumerate(
        normalize_relations(project_relations(tree))
    ):
        relations.append(
            {
                **relation,
                "id": f"relation-{index}",
                "label_html": html_label(relation["label"], width=24),
                "tooltip": relation.get("tooltip", relation["label"]),
                "type": relation.get("type", "primary"),
                "bidirectional": relation.get("bidirectional", False),
                "same_stage": project_stage[relation["from"]]
                == project_stage[relation["to"]],
                "forward": stage_order[project_stage[relation["from"]]]
                <= stage_order[project_stage[relation["to"]]],
                "source_container": project_containers[relation["from"]],
                "target_container": project_containers[relation["to"]],
            }
        )

    return {"stages": stages, "relations": relations}
