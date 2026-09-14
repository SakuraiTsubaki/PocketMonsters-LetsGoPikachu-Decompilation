# Pocket Monsters: Let's Go, Pikachu! — Decompilation

![Status](https://img.shields.io/badge/status-initial_setup-lightgrey)
![Project](https://img.shields.io/badge/project-decompilation-blue)
![ROMs](https://img.shields.io/badge/ROM_binaries-not_included-success)

Decompilation and source-reconstruction project for **Pokémon: Let's Go, Pikachu!**.

## 🎯 Goals

- Reconstruct game code and data into readable, editable source form.
- Document executable structures, data formats, scripts, assets, and version differences.
- Keep analysis, tooling, metadata, and documentation reproducible.
- Build a clean foundation for long-term reverse-engineering work.

## 🚧 Status

This repository is in its **initial setup** stage. Source reconstruction and documentation will be added progressively.

## 🗂️ Planned scope

- Code and executable analysis
- Game data structures
- Scripts and event data
- Graphics and asset metadata
- Audio and resource formats
- Maps and world data
- Tools, notes, manifests, and verification data

## 📌 Repository policy

ROM images and redistributed ROM binaries are **not included**. The repository is intended for reconstructed source, extracted/recreated project data, tooling, analysis, and documentation.

## 🧭 Roadmap

- [ ] Establish baseline version/revision inventory
- [ ] Map executable and data structures
- [ ] Begin source reconstruction
- [ ] Document assets, scripts, and formats
- [ ] Add verification and reproducibility workflow

## 📚 Documentation

| Document | Purpose |
| --- | --- |
| [Project status](docs/PROJECT_STATUS.md) | Current stage, coverage, validation level, and next milestones |
| [Roadmap](docs/ROADMAP.md) | Recommended decompilation phases and long-term progression |
| [Version coverage](docs/VERSIONS.md) | Regions, languages, revisions, updates, builds, and hashes |
| [Research guide](docs/RESEARCH_GUIDE.md) | Evidence, confidence, and research-recording workflow |
| [Verification guide](docs/VERIFICATION.md) | Standards for Observed, Reproduced, and Matched results |
| [Repository structure](docs/REPOSITORY_STRUCTURE.md) | Intended long-term source, data, asset, tooling, and manifest layout |
| [Documentation hub](docs/README.md) | Entry point for format, executable, script, asset, version, and verification notes |

## 🧱 Repository structure

As real project material is reconstructed, the repository may grow into areas such as `src/`, `include/`, `data/`, `assets/`, `tools/`, `tests/`, and `manifests/`. Empty directory trees are not created only for appearance, and platform-specific structure should follow verified target architecture rather than another generation's layout.

See [Repository Structure](docs/REPOSITORY_STRUCTURE.md) for the full organization policy.

## 🔬 Research and verification

Research findings should identify the relevant target version or revision and clearly separate hypotheses from observed, reproduced, or matched results. Use the repository's Research and Verification issue templates when tracking substantial findings.

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules, evidence expectations, commit guidance, and pull-request requirements.
