from __future__ import annotations

from collections.abc import Iterator, Mapping


def project_tree(data: dict) -> list[dict]:
    """Return projects as a normalized recursive tree with inherited metadata."""

    def build(
        projects: Mapping[str, dict],
        *,
        parent: dict | None = None,
        path: tuple[str, ...] = (),
    ) -> list[dict]:
        nodes = []
        for project_id, source in projects.items():
            node = {
                **source,
                "id": project_id,
                "parent_id": parent["id"] if parent else None,
                "path": (*path, project_id),
                "depth": len(path),
                "stage": source.get("stage", parent and parent["stage"]),
                "maintained_by": source.get(
                    "maintained_by", parent and parent["maintained_by"]
                ),
            }
            node["projects"] = build(
                source.get("projects", {}), parent=node, path=node["path"]
            )
            nodes.append(node)
        return nodes

    return build(data.get("projects", {}))


def walk_projects(projects: list[dict]) -> Iterator[dict]:
    """Yield every project in display order, parents before their children."""
    for project in projects:
        yield project
        yield from walk_projects(project["projects"])


def project_index(data: dict) -> dict[str, dict]:
    """Index all projects, including nested projects, by their globally unique ID."""
    return {project["id"]: project for project in walk_projects(project_tree(data))}


def project_relations(projects: list[dict]) -> list[dict]:
    """Collect project-local outgoing relationships into full edge records."""
    relations = []
    for project in walk_projects(projects):
        for relation in project.get("relations", []):
            relations.append({"from": project["id"], **relation})
    return relations


def display_name(project: dict) -> str:
    """Show enough ancestry to distinguish nested projects in flat views."""
    return " › ".join(project.get("display_path", [project["name"]]))


def add_display_paths(projects: list[dict], parent_names: tuple[str, ...] = ()) -> None:
    """Attach human-readable ancestry to an already-normalized project tree."""
    for project in projects:
        names = (*parent_names, project["name"])
        project["display_path"] = names
        add_display_paths(project["projects"], names)
