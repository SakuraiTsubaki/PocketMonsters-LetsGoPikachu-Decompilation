# Roadmap

This roadmap defines the recommended order for turning this repository from an initial research scaffold into a reproducible decompilation project.

## Phase 0 — Target definition
- [ ] Identify authoritative game versions, regions, languages, revisions, and updates.
- [ ] Record hashes and provenance for each supported target.
- [ ] Define the primary matching target.

## Phase 1 — Binary and container mapping
- [ ] Document executable layout, sections, overlays, archives, and resource containers.
- [ ] Build file manifests and extraction notes.
- [ ] Record known compression, packing, and serialization formats.

## Phase 2 — Symbol and subsystem mapping
- [ ] Name functions, symbols, tables, and major data structures.
- [ ] Identify engine subsystems and dependencies.
- [ ] Track confidence and evidence for each finding.

## Phase 3 — Source reconstruction
- [ ] Reconstruct code into readable, maintainable source.
- [ ] Reconstruct scripts, data tables, and asset metadata.
- [ ] Add extraction/repacking tools where needed.

## Phase 4 — Verification
- [ ] Add repeatable tests and comparison workflows.
- [ ] Track matching or behavioral-equivalence status by subsystem.
- [ ] Document remaining mismatches and unknowns.

## Phase 5 — Reproducible project workflow
- [ ] Provide documented setup and build/repack steps.
- [ ] Add CI or automated verification where practical.
- [ ] Keep generated outputs reproducible from repository sources and tooling.