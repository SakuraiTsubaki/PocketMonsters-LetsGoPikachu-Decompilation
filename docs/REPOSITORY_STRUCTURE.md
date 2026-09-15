# Repository Structure

This document defines the intended long-term layout of the decompilation project. Directories should be added when they contain real project material; avoid creating empty placeholder trees only for appearance.

## Top-level layout

- `src/` — reconstructed source code and implementation files
- `include/` — shared declarations, headers, constants, and interfaces
- `data/` — structured game data reconstructed into editable source form
- `assets/` — extracted, reconstructed, or recreated project assets that belong in the repository
- `tools/` — extraction, conversion, analysis, repacking, and verification utilities
- `tests/` — automated checks and regression tests
- `manifests/` — hashes, inventories, version maps, and reproducibility metadata
- `docs/` — research notes, format documentation, roadmaps, status, and verification records
- `.github/` — issue templates, pull request templates, and GitHub project configuration

## Organization principles

1. Prefer source and reproducible project data over opaque generated output.
2. Keep version-specific material clearly separated when releases differ.
3. Deduplicate byte-identical assets when practical and record shared usage in metadata or manifests.
4. Keep human-viewable assets such as PNG previews when they are useful for review and verification.
5. Do not commit retail ROM images, console keys, or other redistributable game binaries.
6. Generated outputs should be reproducible from committed source material and tooling whenever practical.

## Growth policy

The exact source tree may differ by platform, executable format, engine, and toolchain. Do not force a directory structure copied from another generation when the target architecture requires something different. Add platform-specific directories only after the relevant executable, container, or resource layout has been verified.