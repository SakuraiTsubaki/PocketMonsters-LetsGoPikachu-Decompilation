# Project Status

**Current stage:** Phase 0 — target identity / reproducibility baseline

Initial setup is complete. Metadata-only target inventory tooling and CI are active.

## Progress
- [x] Establish repository baseline and ROM/key exclusion rules
- [x] Add deterministic target inventory tooling
- [x] Add machine-readable version inventory and CI
- [ ] Inventory the first verified Let's Go Pikachu target
- [ ] Record revision/update/hash metadata
- [ ] Document NCA/ExeFS/RomFS and NSO/module layout
- [ ] Map symbols, functions, and major subsystems
- [ ] Document game-data formats and resource containers
- [ ] Begin bounded source reconstruction
- [ ] Add reconstruction matching verification

Machine-readable inventory: `manifests/version-inventory.json`

## Immediate next milestone
Run `tools/inventory_target.py` on the first local Let's Go Pikachu target or extracted tree, register exact identity, then begin ExeFS/RomFS/module mapping. Retail bytes and keys remain local.
