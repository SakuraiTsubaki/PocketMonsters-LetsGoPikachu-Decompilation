# PocketMonsters-LetsGoPikachu-Decompilation

A complete, target-specific foundation for reproducible research, analysis, tooling, and source reconstruction related to **Pocket Monsters Let's Go Pikachu**.

| Field | Value |
| --- | --- |
| Working target | Pocket Monsters Let's Go Pikachu |
| Platform family | Nintendo Switch |
| Series generation | Generation VII |
| Exact build identity | Not selected; complete `PROJECT.md` and `config/target.json` before target claims |
| Foundation status | Ready for evidence-backed work |

This repository begins without migrated code, assets, conclusions, or progress claims. Its first research milestone is to identify an exact, reproducible target build.

## Repository areas

| Area | Responsibility |
| --- | --- |
| [`research/`](research/) | Target-specific references, experiments, questions, and methodology. |
| [`analysis/`](analysis/) | Symbols, structures, formats, comparisons, and verified findings. |
| [`tools/`](tools/) | Target adapters and extraction, inspection, conversion, build, and verification utilities. |
| [`src/`](src/) | Reviewed source reconstruction and source-linked data. |
| [`config/`](config/) | Target identity, symbols, mappings, and reproducible tool/build configuration. |
| [`tests/`](tests/) | Unit, regression, comparison, and build-verification checks. |
| [`progress/`](progress/) | Evidence-based milestones and unresolved blockers. |
| [`docs/`](docs/) | Target workflow and architecture documentation. |

Target-independent methods and tools belong in [`SakuraiTsubaki/Decompilation`](https://github.com/SakuraiTsubaki/Decompilation).

## Start here

1. Complete the identity checklist in [`PROJECT.md`](PROJECT.md).
2. Replace the unselected fields in [`config/target.json`](config/target.json) with verified identifiers.
3. Open a focused research record from [`research/template.md`](research/template.md).
4. Promote reproducible conclusions through [`analysis/template.md`](analysis/template.md).
5. Add target-specific tooling with tests and documented inputs/outputs.
6. Run `python scripts/check_repository.py .` and the unit tests before review.

## Non-negotiable rules

- Record provenance, hashes, versions, commands, environment, and confidence.
- Distinguish Confirmed, Probable, and Hypothesis conclusions.
- Never commit copyrighted game images, firmware, keys, credentials, or locally extracted proprietary content.
- Keep generated output separate from reviewed source and analysis.
- Add concrete work, not invented completion percentages or placeholder source trees.
