# Non-ROM Artifact Preservation Policy

## Core rule

GitHub stores every storable work product except ROM binaries.

Original ROMs, modified ROMs, rebuilt ROMs, and equivalent complete game-image or installable-package binaries are excluded. Everything else produced or collected during the work is repository material.

## Commit all non-ROM results

This includes:

- analysis results, research material, reports, documents, and README files;
- scripts, source code, tools, configuration, and build descriptions;
- logs, manifests, inventories, hashes, checklists, and progress records;
- comparison tables and CSV, JSON, YAML, TOML, XML, TSV, and other structured data;
- graphics, sprites, images, palettes, fonts, icons, tiles, atlases, and converted data;
- patches, diffs, symbol maps, address maps, validation reports, and test results;
- intermediate non-ROM outputs that preserve provenance or reproducibility.

Generated, collected, intermediate, binary, or machine-readable does not mean disposable. Organize, document, and commit it.

## Graphics and sprite rule

Every concrete graphics, sprite, palette, font, icon, or tile task must include actual PNG output. Data and metadata alone are not sufficient.

Retain the conversion script and command, source-derived non-ROM data, palette and metadata files, manifest or hashes, PNG previews or sheets, and validation or comparison results.

## Placement

Use `research/` and `analysis/` for topic evidence, `tools/` for implementations, `artifacts/` for retained outputs, `manifests/` for indexes and hashes, `logs/` for execution records, and `patches/` for patch material.

Secrets, credentials, access tokens, and private keys are not work products and must not be committed.
