# Phase 3 — Evidence Extraction and Binary Diff

This phase begins after the exact target build and NSO module map have been verified.

## Goals

- Build reproducible evidence indexes for `main` and other NSO0 modules.
- Narrow Pikachu/Eevee executable differences without embedding executable bytes in reports.
- Generate pointer candidates only inside verified mapped address ranges.
- Keep `main`, `rtld`, `sdk`, `subsdk*`, and any additional NSO modules distinct.

## Required inputs

- verified `nso_modules.json`
- locally extracted ExeFS NSO0 modules
- paired-version modules when performing Pikachu ↔ Eevee comparison

## Tools

- `tools/extract_binary_evidence.py` — indexes string candidates; default reports omit literal text.
- `tools/compare_binary_blocks.py` — fixed-size hash-only binary comparison.
- `tools/scan_pointer_candidates.py` — aligned little-endian integer scan inside researcher-supplied verified address ranges.

## Switch workflow

1. Run `map_nso_modules.py` on the extracted ExeFS.
2. Treat each NSO module independently.
3. Use verified module-relative `.text/.rodata/.data` ranges when selecting address intervals.
4. Generate evidence indexes for `main` first, then supporting modules as needed.
5. Compare Pikachu ↔ Eevee only between corresponding verified modules/builds.
6. Generate pointer candidates inside verified ranges.
7. Assign symbols only after direct evidence, cross-references, or reproducible paired-version correspondence.

## Evidence rules

- Do not treat runtime/SDK/subsdk code as game `main` code.
- Numeric values inside an address interval are only candidate pointers.
- String candidates do not establish function purpose on their own.
- Changed 4 KiB blocks are localization targets, not function boundaries.
- Do not copy labels from the 3DS Alola games.
- Unknowns remain unknown until verified.

## Repository policy

Do not commit cartridge images, encrypted title packages, keys, proprietary executable payloads, or literal extracted text dumps. Commit tooling, hashes, metadata, reconstructed source, analysis tables, and verification records according to project policy.
