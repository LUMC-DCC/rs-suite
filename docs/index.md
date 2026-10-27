# RS suite

Guidance and connected tools for planning, building, publishing, and maintaining research software. **Use the components that fit your project.** You do not need to use the whole suite.

## How it fits together

A Software Management Plan (SMP) captures your project decisions. Its information can be exported as structured metadata and reused to generate project files and repository scaffolds.

<style>
.rs-home-flow{display:grid;grid-template-columns:1fr auto 1fr auto 1fr;align-items:center;gap:12px;max-width:780px;margin:1.5em 0 1.8em;font-size:.94em}
.rs-home-flow .flow-box{border:1px solid var(--md-default-fg-color--lightest,#ddd);border-radius:8px;padding:1em .6em;text-align:center;line-height:1.5}
.rs-home-flow .short-label{display:none}
@media(max-width:600px){.rs-home-flow{gap:8px;font-size:.88em}.rs-home-flow .long-label{display:none}.rs-home-flow .short-label{display:inline}}
</style>
<div class="rs-home-flow" role="img" aria-label="A Software Management Plan exports reusable RSM metadata, which drives the generation of project files and repository scaffolds.">
  <span class="flow-box"><span class="long-label">Software management plan</span><span class="short-label">SMP</span></span>
  <span aria-hidden="true">→</span>
  <span class="flow-box"><span class="long-label">RSM metadata (JSON)</span><span class="short-label">RSM JSON</span></span>
  <span aria-hidden="true">→</span>
  <span class="flow-box"><span class="long-label">Files &amp; repository scaffold</span><span class="short-label">Files &amp; repo</span></span>
</div>

Repository metadata can then be **validated**, **exchanged with registries**, and **compared and reconciled** using the tools below.

## Where to start

- **Learn the practices:** start with [RS guidelines](https://lumc-dcc.github.io/rs-guidelines/) for recommendations and practical guidance.
- **Write a plan:** follow the [planning guide](users/#plan-describe), or open [SciWiz](https://sciwiz.lumc.nl) (LUMC access). The [SMP template](https://github.com/LUMC-DCC/sciwiz-smp-km) can also be used in another Data Stewardship Wizard instance.
- **Generate files or a repository:** use [rs-tools](https://rs-tools.onrender.com/) to edit RSM metadata and generate project assets.
- **Check repository metadata:** [rs-metadata](https://lumc-dcc.github.io/rs-metadata/) validates the metadata profile and checks consistency across files.
- **Connect and reconcile records:** [Metadata bridge](https://github.com/bio-tools/metadata-bridge) supports exchange between repositories and registries; [Diff Fuse](https://github.com/bio-tools/diff-fuse) compares and merges JSON records. Synchronization back to SMPs is planned.

[Open the full user guide](users/) for all resources, tool links, and availability.

## Components at a glance

A quick reference to the tools, templates, and supporting resources. Repository links include source code and component documentation. Internal services link to their service pages.

| Component | What it provides | Repository or resource |
|---|---|---|
| LUMC software stewardship | Institutional information and support for research software. | [Internal page](https://www.albinusnet.nl/en/products-and-services/research/data-stewardship/research-software-stewardship/) |
| RS guidelines | Recommendations and practical software management guidance. | [Repository](https://github.com/LUMC-DCC/rs-guidelines) |
| Training materials | Research software development and management training. | [Repository](https://github.com/LUMC-DCC/research_software_training) |
| SciWiz | LUMC service for writing SMPs in Data Stewardship Wizard. | [LUMC service](https://sciwiz.lumc.nl) |
| SMP template | Knowledge model for creating software management plans. | [Repository](https://github.com/LUMC-DCC/sciwiz-smp-km) |
| Universal SMP export | Export questionnaire answers as a readable SMP document. | [Repository](https://github.com/LUMC-DCC/sciwiz-smp-doc-universal) |
| eScience / NWO SMP export | Export an SMP in the eScience Center / NWO format. | [Repository](https://github.com/LUMC-DCC/sciwiz-smp-doc-escience) |
| SMP JSON export | Export SMP answers as JSON following the RSM schema. | [Repository](https://github.com/LUMC-DCC/sciwiz-smp-rsmjson) |
| RSM schema | Shared metadata schema and Python models for project information. | [Repository](https://github.com/LUMC-DCC/rsm-schema) |
| rs-tools | Edit RSM metadata and generate project assets. | [Repository](https://github.com/LUMC-DCC/rs-tools) |
| File templates | Generate metadata, documentation and community files. | [Repository](https://github.com/LUMC-DCC/rs-files-templates) |
| Repository templates | Generate configurable project repository scaffolds. | [Repository](https://github.com/LUMC-DCC/rs-repo-templates) |
| rs-metadata | Metadata profile, validation and cross-file consistency checks. | [Repository](https://github.com/LUMC-DCC/rs-metadata) |
| Metadata bridge | Exchange repository and registry metadata. SMP synchronization is planned. | [Repository](https://github.com/bio-tools/metadata-bridge) |
| Diff Fuse | Compare and merge JSON metadata records. | [Repository](https://github.com/bio-tools/diff-fuse) |

## For developers and maintainers

See the [suite architecture and maintainer guide](developers/) for component relationships, project references, and maintenance information.
