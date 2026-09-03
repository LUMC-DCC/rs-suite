# Suite architecture

This section is for people developing, operating, or maintaining the suite. **`data/suite.yml` is the source of truth** for projects, relationships, skills, maintainers, and maintenance review triggers.

## Suite map

<div class="suite-diagram-frame">
  <object class="suite-diagram" data="../assets/suite.svg" type="image/svg+xml" aria-label="Map of RS suite projects grouped into lifecycle categories">
    <a href="../assets/suite.svg">Open the suite map</a>
  </object>
</div>

### How to read the map

| Appearance | Meaning |
|---|---|
| Blue, purple, green, and peach containers | The **Discover**, **Plan**, **Build**, and **Publish/reuse** lifecycle stages, respectively |
| Light-blue project | Suite component |
| Light-grey project | Support resource |
| Pink project | Community activity |
| Orange project | Externally maintained project |
| Grey project | Artifact or external registry |
| Solid project border | Active project |
| Dashed project border | In-progress or planned project |
| Solid arrow | Primary relationship |
| Dashed arrow | Supporting relationship |
| Arrowhead at one end | One-way relationship, read in the arrow's direction |
| Arrowheads at both ends | Bidirectional relationship |

Parent projects are containers around their child projects. Every relationship and its label is shown without hovering, and linked projects are clickable.

## Projects by stage

<!-- generated:start -->
### Discover & learn

| Project | Purpose | Status |
|---|---|---|
| [Albinusnet - Research Software Stewardship (internal)](https://www.albinusnet.nl/en/products-and-services/research/data-stewardship/research-software-stewardship/) | General information and overview on research software stewardship at LUMC. | active |
| [rs-guidelines](https://lumc-dcc.github.io/rs-guidelines/) | Definitions, resources, and best practices for research software. | active |
| [Research software training](https://lumc-dcc.github.io/research_software_training/) | Training material that supports the other suite components. | active |
| ↳ Coding Cafe | Community meetups. | active |

### Plan & describe

| Project | Purpose | Status |
|---|---|---|
| [SciWiz](https://sciwiz.lumc.nl) | LUMC instance of Data Stewardship Wizard for filling in software management plans and exports. | active |
| [research-smp](https://github.com/LUMC-DCC/sciwiz-smp-km) | SciWiz Knowledge Model for creating Software Management Plans. | in-progress |
| [.md KM export](https://github.com/LUMC-DCC/sciwiz-smp-doc-universal) | Question-answer Markdown export from the Software Management Plan. | in-progress |
| [.md eScience/NWO KM export](https://github.com/LUMC-DCC/sciwiz-smp-doc-escience) | Markdown export from the SMP for the eScience Center / NWO template. | in-progress |
| [.json KM export adhering to RSM schema](https://github.com/LUMC-DCC/sciwiz-smp-rsmjson) | JSON export from the SMP in the form of RSM schema data | in-progress |
| [rsm-schema](https://lumc-dcc.github.io/rsm-schema/) | Structured metadata schema and Python representation for Research Software Management. | active |

### Build the software project

| Project | Purpose | Status |
|---|---|---|
| [rs-tools](https://rs-tools.onrender.com/) | Web tool to edit RSM metadata and generate project assets. | in-progress |
| [rs-files-templates](https://lumc-dcc.github.io/rs-files-templates/) | Generate repository and metadata files from RSM data. | active |
| [rs-repo-templates](https://github.com/LUMC-DCC/rs-repo-templates) | Repository templates for starting projects with FAIR and FOSS practices baked in. | in-progress |
| [rs-metadata](https://lumc-dcc.github.io/rs-metadata/) | Validate the LUMC CodeMeta profile and keep repository metadata consistent. | active |

### Publish, connect & reuse

| Project | Purpose | Status |
|---|---|---|
| Repository | A research software repository produced and maintained using the suite. | active |
| [Metadata bridge](https://github.com/bio-tools/metadata-bridge) | Bidirectional metadata bridge; RSM sync is planned. | in-progress |
| ↳ GitHub ↔ bio.tools bridge | Synchronize software metadata bidirectionally between GitHub repositories and bio.tools. | active |
| ↳ GitHub ↔ RSM bridge | Synchronize repository metadata with the Research Software Metadata schema. | planned |
| [bio.tools registry](https://bio.tools/) | External registry for software metadata. | active |
| [Diff Fuse](https://github.com/bio-tools/diff-fuse) | Compare equivalent JSON documents side by side and merge them interactively. | active |
<!-- generated:end -->
