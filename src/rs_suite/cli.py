from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .diagram import diagram_context, dot_string
from .model import (
    add_display_paths,
    display_name,
    project_tree,
    walk_projects,
)

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "suite.yml"
DOCS = ROOT / "docs"
ASSETS = DOCS / "assets"
DIAGRAMS = ROOT / "diagrams"


def load_data() -> dict:
    with DATA.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    validate(data)
    return data


def validate(data: dict) -> None:
    project_sources = data.get("projects", {})
    stages = data.get("stages", {})
    maintainers = data.get("maintainers", {})
    if not project_sources or not stages:
        raise ValueError("suite.yml must define stages and projects")
    for stage_id, stage in stages.items():
        if not stage.get("user_guidance"):
            raise ValueError(f"{stage_id}: must define user guidance")

    if "relations" in data or "maintenance" in data:
        raise ValueError(
            "relations and maintenance must be defined on their source project"
        )

    projects = project_tree(data)
    all_projects = list(walk_projects(projects))
    project_ids = [project["id"] for project in all_projects]
    duplicates = sorted({pid for pid in project_ids if project_ids.count(pid) > 1})
    if duplicates:
        raise ValueError(f"project IDs must be globally unique: {duplicates}")
    index = {project["id"]: project for project in all_projects}

    for project in all_projects:
        pid = project["id"]
        if project.get("stage") not in stages:
            raise ValueError(f"{pid}: unknown stage {project.get('stage')!r}")
        if project["parent_id"] and project["stage"] != index[project["parent_id"]]["stage"]:
            raise ValueError(f"{pid}: nested projects must use their parent's stage")
        owners = project.get("maintained_by", [])
        if not owners:
            raise ValueError(f"{pid}: must define at least one maintainer")
        unknown_owners = set(owners) - set(maintainers)
        if unknown_owners:
            raise ValueError(f"{pid}: unknown maintainers {sorted(unknown_owners)}")

        for relation in project.get("relations", []):
            unexpected = set(relation) - {"to", "label", "type", "bidirectional"}
            if unexpected:
                raise ValueError(
                    f"{pid}: relation has unexpected keys {unexpected}: {relation}"
                )
            if relation.get("to") not in index:
                raise ValueError(f"{pid}: relation target is unknown: {relation}")
            if not relation.get("label"):
                raise ValueError(f"{pid}: relation is missing a label: {relation}")

        for item in project.get("maintenance", []):
            unexpected = set(item) - {"project", "reason"}
            if unexpected:
                raise ValueError(
                    f"{pid}: maintenance item has unexpected keys {unexpected}: {item}"
                )
            if item.get("project") not in index:
                raise ValueError(f"{pid}: maintenance target is unknown: {item}")
            if not item.get("reason"):
                raise ValueError(f"{pid}: maintenance item is missing a reason: {item}")


def link(project: dict, *, hierarchical: bool = False) -> str:
    url = project.get("url") or project.get("repository")
    name = display_name(project) if hierarchical else project["name"]
    return f"[{name}]({url})" if url else name


def render_diagram(data: dict) -> None:
    environment = Environment(
        loader=FileSystemLoader(DIAGRAMS),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    environment.filters["dot"] = dot_string
    dot = environment.get_template("suite.dot.j2").render(**diagram_context(data))
    dot_path = ASSETS / "suite.dot"
    dot_path.write_text(dot, encoding="utf-8")
    result = subprocess.run(
        ["node", "scripts/render-diagram.mjs", str(dot_path)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    (ASSETS / "suite.svg").write_text(result.stdout, encoding="utf-8")


def render_overview(data: dict) -> str:
    projects = project_tree(data)
    add_display_paths(projects)
    stages = sorted(data["stages"].items(), key=lambda item: item[1]["order"])
    out = []
    for stage_id, stage in stages:
        out += [f"### {stage['title']}", "", "| Project | Purpose | Status |", "|---|---|---|"]
        for project in walk_projects(projects):
            if project["stage"] == stage_id:
                prefix = "↳ " * project["depth"]
                out.append(
                    f"| {prefix}{link(project)} | {project['summary']} | "
                    f"{project.get('status', 'active')} |"
                )
        out.append("")
    return "\n".join(out) + "\n"


def render_user_guide(data: dict) -> str:
    """Render a practical catalogue without exposing maintenance internals."""
    projects = project_tree(data)
    stages = sorted(data["stages"].items(), key=lambda item: item[1]["order"])
    out = []
    for stage_id, stage in stages:
        out.extend(
            [
                f"## {stage['title']}",
                "",
                stage["user_guidance"],
                "",
                "| Resource | What it helps with | Availability |",
                "|---|---|---|",
            ]
        )
        for project in walk_projects(projects):
            if project["stage"] != stage_id:
                continue
            prefix = "↳ " * project["depth"]
            status = project.get("status", "active").replace("-", " ").title()
            if not (project.get("url") or project.get("repository")):
                status += "; link not available yet"
            out.append(
                f"| {prefix}{link(project)} | {project['summary']} | {status} |"
            )
        out.append("")
    return "\n".join(out) + "\n"


def render_projects(data: dict) -> str:
    projects = project_tree(data)
    out = []
    stages = sorted(data["stages"].items(), key=lambda item: item[1]["order"])

    def render_project(project: dict) -> None:
        heading = "#" * min(3 + project["depth"], 6)
        out.extend([f"{heading} {project['name']}", "", project["summary"], ""])
        meta = []
        if project.get("status"):
            meta.append(f"**Status:** {project['status']}")
        if project.get("url"):
            meta.append(f"**Link:** {project['url']}")
        if project.get("repository") and project.get("repository") != project.get("url"):
            meta.append(f"**Repository:** {project['repository']}")
        if project.get("note"):
            meta.append(f"**Note:** {project['note']}")
        if meta:
            out.extend(["  ".join(meta), ""])
        if project.get("outputs"):
            out.extend(["**Produces:** " + ", ".join(project["outputs"]), ""])
        for child in project["projects"]:
            render_project(child)
        if project["depth"] == 0:
            out.append("---")

    for stage_id, stage in stages:
        out += [f"## {stage['title']}", ""]
        for project in projects:
            if project["stage"] != stage_id:
                continue
            render_project(project)
    return "\n".join(out) + "\n"


def render_impact(data: dict) -> str:
    projects = project_tree(data)
    add_display_paths(projects)
    index = {project["id"]: project for project in walk_projects(projects)}
    out = []
    for project in walk_projects(projects):
        items = project.get("maintenance", [])
        if not items:
            continue
        out += [f"## When {display_name(project)} changes", ""]
        for item in items:
            out.append(
                f"- **{link(index[item['project']], hierarchical=True)}**: {item['reason']}"
            )
        out.append("")
    return "\n".join(out) + "\n"


def normalized_skills(project: dict) -> dict[str, list[str]]:
    categories = {"domain": [], "development": [], "operations": []}
    aliases = {
        "content": "domain",
        "documentation": "development",
        "integration": "development",
        "release": "development",
    }
    for category, skills in project.get("skills", {}).items():
        target = aliases.get(category, category)
        categories.setdefault(target, []).extend(skills)
    return {category: skills for category, skills in categories.items() if skills}


def maintainers(data: dict, project: dict) -> str:
    return ", ".join(data["maintainers"][owner]["name"] for owner in project["maintained_by"])


def render_maintenance(data: dict) -> str:
    projects = project_tree(data)
    add_display_paths(projects)
    categories: dict[str, list[tuple[dict, list[str]]]] = {}
    for project in walk_projects(projects):
        for category, skills in normalized_skills(project).items():
            categories.setdefault(category, []).append((project, skills))
    preferred = ["domain", "development", "operations"]
    out = ["## By maintenance area", ""]
    for category in preferred + sorted(set(categories) - set(preferred)):
        rows = categories.get(category)
        if not rows:
            continue
        out += [f"### {category.replace('-', ' ').title()}", "", "| Project | Useful skills |", "|---|---|"]
        for project, skills in rows:
            out.append(f"| {link(project, hierarchical=True)} | {', '.join(skills)} |")
        out.append("")
    out += ["## By project", "", "| Project | Maintained by | Maintenance areas |", "|---|---|---|"]
    for project in walk_projects(projects):
        skills = normalized_skills(project)
        areas = "; ".join(
            f"**{category.title()}:** {', '.join(values)}" for category, values in skills.items()
        ) or "—"
        out.append(
            f"| {link(project, hierarchical=True)} | {maintainers(data, project)} | {areas} |"
        )
    return "\n".join(out) + "\n"


def insert_generated_content(page: Path, content: str) -> None:
    template = page.read_text(encoding="utf-8")
    start = "<!-- generated:start -->"
    end = "<!-- generated:end -->"
    pattern = rf"({re.escape(start)}\n)(.*?)(\n{re.escape(end)})"
    updated, count = re.subn(pattern, rf"\1{content.rstrip()}\3", template, flags=re.DOTALL)
    if count != 1:
        raise ValueError(
            f"{page.relative_to(ROOT)} must contain exactly one generated region: "
            f"{start} {{ content }} {end}"
        )
    page.write_text(updated, encoding="utf-8")


def generate() -> None:
    data = load_data()
    ASSETS.mkdir(parents=True, exist_ok=True)
    insert_generated_content(DOCS / "users" / "index.md", render_user_guide(data))
    insert_generated_content(DOCS / "developers" / "index.md", render_overview(data))
    insert_generated_content(DOCS / "developers" / "projects.md", render_projects(data))
    insert_generated_content(DOCS / "developers" / "impact.md", render_impact(data))
    insert_generated_content(
        DOCS / "developers" / "maintenance.md", render_maintenance(data)
    )
    render_diagram(data)


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate and build the research software suite site")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("generate", help="Generate Markdown regions and the suite diagram")
    sub.add_parser("build", help="Generate everything and build the Zensical site")
    sub.add_parser("serve", help="Generate everything and start the Zensical preview server")
    args = parser.parse_args()

    if args.command == "generate":
        generate()
    elif args.command == "build":
        generate()
        run(["zensical", "build", "--clean"])
    elif args.command == "serve":
        generate()
        run(["zensical", "serve"])


if __name__ == "__main__":
    main()
