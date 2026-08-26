# Maintenance impact

These are **review triggers**: an upstream change means the listed downstream project should be reviewed, but does not necessarily require a release.

<!-- generated:start -->
## When Albinusnet - Research Software Stewardship changes

- **[rs-guidelines](https://lumc-dcc.github.io/rs-guidelines/)**: Align definitions, recommendations and links when stewardship policy/guidance changes.
- **[Research software training](https://lumc-dcc.github.io/research_software_training/)**: Update teaching material when the stewardship model or recommended practices change.
- **[SciWiz](https://sciwiz.lumc.nl)**: Review SMP workflow guidance when high-level stewardship requirements change.
- **[rsmp-km](https://github.com/LUMC-DCC/sciwiz-smp-km)**: Review SMP questions/guidance when high-level stewardship requirements change.

## When rs-guidelines changes

- **[Research software training](https://lumc-dcc.github.io/research_software_training/)**: Keep teaching material aligned with recommended practices.
- **Coding Cafe**: Keep support material aligned with recommended practices.
- **[SciWiz](https://sciwiz.lumc.nl)**: Review questionnaire guidance and recommendations.
- **[rsmp-km](https://github.com/LUMC-DCC/sciwiz-smp-km)**: Review questionnaire guidance and recommendations.
- **[rs-repo-templates](https://github.com/LUMC-DCC/rs-repo-templates)**: Update generated repository defaults when recommended practices change.
- **[rs-files-templates](https://github.com/LUMC-DCC/rs-files-templates)**: Update generated files when recommended practices change.
- **[rs-metadata](https://github.com/LUMC-DCC/rs-metadata)**: Review validation rules when metadata recommendations change.

## When Research software training changes

- **Coding Cafe**: Refresh exercises and support material as training changes.

## When Coding Cafe changes

- **[Research software training](https://lumc-dcc.github.io/research_software_training/)**: Feed recurring support problems back into training material when useful.
- **[rs-guidelines](https://lumc-dcc.github.io/rs-guidelines/)**: Feed recurring support problems back into guidance when useful.

## When SciWiz changes

- **[rsmp-km](https://github.com/LUMC-DCC/sciwiz-smp-km)**: Check Knowledge Model compatibility after DSW/SciWiz upgrades.
- **.md KM export**: Review export integration if questionnaire/export APIs or template behavior changes.
- **[rsm-schema](https://github.com/LUMC-DCC/rsm-schema)**: Verify that SciWiz output can still be converted into RSM metadata.
- **[Research software training](https://lumc-dcc.github.io/research_software_training/)**: Refresh screenshots/workflow instructions after UI or process changes.
- **[rs-guidelines](https://lumc-dcc.github.io/rs-guidelines/)**: Refresh workflow instructions after UI or process changes.

## When rsmp-km changes

- **.md KM export**: Update question-to-Markdown mapping when questions, identifiers or answer structures change.
- **[rsm-schema](https://github.com/LUMC-DCC/rsm-schema)**: Update conversion/mapping for new or changed questionnaire concepts.
- **[SciWiz](https://sciwiz.lumc.nl)**: Publish/import the new Knowledge Model version and migrate questionnaires when needed.
- **[rs-guidelines](https://lumc-dcc.github.io/rs-guidelines/)**: Update user-facing terminology/concepts when needed.
- **[Research software training](https://lumc-dcc.github.io/research_software_training/)**: Update user-facing terminology/concepts when needed.

## When .md KM export changes

- **[rsmp-km](https://github.com/LUMC-DCC/sciwiz-smp-km)**: Review only if exporter changes require question identifiers/structure to change.
- **[rs-guidelines](https://lumc-dcc.github.io/rs-guidelines/)**: Update examples/instructions if generated Markdown changes materially.
- **[Research software training](https://lumc-dcc.github.io/research_software_training/)**: Update examples/instructions if generated Markdown changes materially.

## When rsm-schema changes

- **[rsmp-km](https://github.com/LUMC-DCC/sciwiz-smp-km)**: Update import/export mapping for added, renamed, removed or constrained schema fields.
- **rs-tools**: Update forms, payload generation, validation and schema version handling.
- **[rs-files-templates](https://github.com/LUMC-DCC/rs-files-templates)**: Update model/template bindings if generated files consume changed RSM fields.
- **[rs-metadata](https://github.com/LUMC-DCC/rs-metadata)**: Review mappings/validation where RSM fields correspond to repository metadata.
- **Metadata bridge › GitHub ↔ RSM bridge**: Update repository ↔ RSM field extraction/mapping.
- **[Diff Fuse](https://github.com/bio-tools/diff-fuse)**: Test compatibility if schema-aware reconciliation rules are introduced.

## When rs-tools changes

- **[rs-repo-templates](https://github.com/LUMC-DCC/rs-repo-templates)**: Update integration if generator inputs/outputs or invocation conventions change.
- **[rs-files-templates](https://github.com/LUMC-DCC/rs-files-templates)**: Update integration if file-generation APIs, variables or output contracts change.
- **[rsm-schema](https://github.com/LUMC-DCC/rsm-schema)**: Propose schema changes if rs-tools introduces genuinely new structured concepts.
- **[Research software training](https://lumc-dcc.github.io/research_software_training/)**: Refresh usage instructions after UI/workflow changes.
- **[rs-guidelines](https://lumc-dcc.github.io/rs-guidelines/)**: Refresh usage instructions after UI/workflow changes.

## When rs-files-templates changes

- **[rs-repo-templates](https://github.com/LUMC-DCC/rs-repo-templates)**: Update included templates, invocation or generated-file expectations.
- **rs-tools**: Update integration when template inputs or output contracts change.
- **[rs-metadata](https://github.com/LUMC-DCC/rs-metadata)**: Update validation expectations when metadata-file structure/content changes.
- **[rs-guidelines](https://lumc-dcc.github.io/rs-guidelines/)**: Update documented examples when generated standards change.
- **[Research software training](https://lumc-dcc.github.io/research_software_training/)**: Update documented examples when generated standards change.

## When rs-repo-templates changes

- **rs-tools**: Update generator integration if Cookiecutter variables, template names or invocation change.
- **[rs-metadata](https://github.com/LUMC-DCC/rs-metadata)**: Review validation/CI assumptions if generated metadata or workflow files change.
- **[Research software training](https://lumc-dcc.github.io/research_software_training/)**: Update quick-start instructions and examples.
- **[rs-guidelines](https://lumc-dcc.github.io/rs-guidelines/)**: Update quick-start instructions and examples.
- **Repository**: Existing generated repositories do not update automatically; document or automate migrations when changes should propagate.

## When rs-metadata changes

- **[rs-files-templates](https://github.com/LUMC-DCC/rs-files-templates)**: Update generated examples/templates when validator requirements or supported profiles change.
- **[rs-repo-templates](https://github.com/LUMC-DCC/rs-repo-templates)**: Update CI/configuration when commands, configuration or supported metadata formats change.
- **Metadata bridge**: Review field mapping if repository metadata normalization changes affect bridge inputs.
- **[Research software training](https://lumc-dcc.github.io/research_software_training/)**: Update metadata instructions when validation rules or formats change.
- **[rs-guidelines](https://lumc-dcc.github.io/rs-guidelines/)**: Update metadata instructions when validation rules or formats change.

## When Repository changes

- **Metadata bridge**: Update extraction logic when repository metadata locations/formats change.
- **[rs-metadata](https://github.com/LUMC-DCC/rs-metadata)**: Update validation/normalization rules for new repository conventions.
- **[bio.tools registry](https://bio.tools/)**: Re-sync registry records after authoritative repository metadata changes.

## When Metadata bridge changes

- **[rs-metadata](https://github.com/LUMC-DCC/rs-metadata)**: Review extraction rules when repository metadata conventions change.

## When Metadata bridge › GitHub ↔ bio.tools bridge changes

- **[bio.tools registry](https://bio.tools/)**: Review registry records/API integration when mapping behavior changes.
- **[Diff Fuse](https://github.com/bio-tools/diff-fuse)**: Update integration only if bridge reconciliation depends on Diff Fuse API/payload conventions.

## When Metadata bridge › GitHub ↔ RSM bridge changes

- **[rsm-schema](https://github.com/LUMC-DCC/rsm-schema)**: Update mapping if the bridge changes its RSM representation or extracts new RSM fields.

## When bio.tools registry changes

- **[Metadata bridge › GitHub ↔ bio.tools bridge](https://github.com/bio-tools/biohackathon2025)**: Update API client, authentication, field mapping and sync logic after API/schema changes.
- **[Diff Fuse](https://github.com/bio-tools/diff-fuse)**: Update only if the registry JSON representation or reconciliation integration changes.

## When Diff Fuse changes

- **[Metadata bridge › GitHub ↔ bio.tools bridge](https://github.com/bio-tools/biohackathon2025)**: Update client integration if endpoints, payloads, conflict representation or merge semantics change.
- **[rsm-schema](https://github.com/LUMC-DCC/rsm-schema)**: Add adapters/tests only if schema-specific behavior is introduced.
<!-- generated:end -->
