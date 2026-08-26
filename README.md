# RS suite

Site that explains how LUMC research software projects fit together, what depends on what, and who maintains them.

## Source of truth

The repo intentionally separates **semantics** from **presentation**:

- `data/suite.yml`: projects, maintainers, lifecycle stages, links, relationships, maintenance skills, and review triggers. Relationships and review triggers live on their source project.
- `diagrams/suite.dot.j2`: the readable Graphviz template that controls category boxes, node styling, and relationship presentation.
- `docs/**/*.md`: Markdown pages, split into user and developer/maintainer sections. Their `<!-- generated:start -->` regions are refreshed from the YAML, while all content around them is hand written.

The build uses Graphviz at build time to lay out any number of projects and relationships, route edges, place labels, and keep category boxes together. Generated diagram assets should not be edited by hand.

## Local setup

Requirements: Python 3.12+, Node.js 22+, and Poetry.

```bash
poetry install
npm ci
poetry run suite-docs serve
```

A production build generates and renders the diagram automatically:

```bash
poetry run suite-docs build
```

## Updating the site

1. Edit `data/suite.yml` for structured data.
2. Edit the Markdown pages for narrative and layout outside generated regions.
3. Change `diagrams/suite.dot.j2` only when the diagram's structure or styling needs to change.
4. Run `poetry run suite-docs build`.
