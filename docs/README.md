# Documentation Hub

This directory is the central documentation portal for the decompilation project. Use it to move from target identification and research through reconstruction, asset handling, manifests, and verification without losing version context or evidence.

## Quick links

| Document | Purpose |
| --- | --- |
| [Project Status](PROJECT_STATUS.md) | Current stage, target coverage, validation level, and next milestones |
| [Roadmap](ROADMAP.md) | Recommended project phases from target definition through reproducible reconstruction |
| [Version Coverage](VERSIONS.md) | Regions, languages, revisions, updates, builds, hashes, and support status |
| [Research Guide](RESEARCH_GUIDE.md) | Evidence, confidence, offsets, naming, and research-recording practices |
| [Verification Guide](VERIFICATION.md) | Standards for Unverified, Observed, Reproduced, and Matched results |
| [Repository Structure](REPOSITORY_STRUCTURE.md) | Intended long-term layout for source, data, assets, tools, tests, and manifests |
| [Project Standards](PROJECT_STANDARDS.md) | Naming, provenance, generated-data, manifest, and repository-boundary rules |
| [Asset Workflow](ASSET_WORKFLOW.md) | Extraction, reviewable assets, deduplication, manifest registration, and batch workflow |
| [Manifest Guide](../manifests/README.md) | Machine-readable inventories, hashes, target coverage, provenance, and shared assets |
| [Contributing](../CONTRIBUTING.md) | Contribution rules, evidence expectations, commits, and pull-request guidance |

## Research areas

As verified work becomes concrete, documentation may grow into areas such as `architecture/`, `formats/`, `research/`, `versions/`, and `verification/`. Create these directories when they contain real research material rather than as empty placeholders.

## Recommended documentation flow

1. Identify the target in `VERSIONS.md`.
2. Record investigation methods and evidence according to `RESEARCH_GUIDE.md`.
3. Reconstruct source, data, or assets following `PROJECT_STANDARDS.md` and `REPOSITORY_STRUCTURE.md`.
4. For asset work, follow `ASSET_WORKFLOW.md` and register material in `../manifests/`.
5. Apply the validation levels defined in `VERIFICATION.md`.
6. Update `PROJECT_STATUS.md` and `ROADMAP.md` when meaningful milestones are reached.

## Documentation rules

- Distinguish confirmed findings from hypotheses.
- Identify the exact target version or revision for version-specific claims.
- Record offsets, paths, symbols, hashes, commands, and other stable evidence when practical.
- Use `TBD`, `unknown`, or `null` instead of inventing missing information.
- Preserve enough provenance for another researcher to reproduce or verify the finding.
- Keep retail ROM images, decrypted game images, console keys, and other redistributable game binaries out of the repository.
