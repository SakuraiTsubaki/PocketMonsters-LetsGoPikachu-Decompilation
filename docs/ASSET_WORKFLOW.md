# Asset Workflow

This document defines the recommended workflow for extracting, reconstructing, reviewing, deduplicating, documenting, and committing project assets.

## 1. Identify the target

Before processing an asset, record the verified target version, region, language, revision, update, or build when known. If any field is not verified, leave it explicitly as `TBD`, `unknown`, or `null` rather than guessing.

## 2. Record the source location

Track enough provenance to locate the asset again. Depending on the platform, this may include:

- archive or container
- executable or section
- file path
- table, symbol, or record identifier
- index or offset
- extraction tool and command

Do not commit retail ROM images, decrypted game images, console keys, or other redistributable game binaries as source material.

## 3. Preserve reproducible project material

Prefer reconstructed source data, editable metadata, and reproducible extraction/conversion tooling over opaque generated output.

When graphics or sprites are part of the work, include a human-viewable representation such as PNG alongside the reconstructed/source asset data when practical so changes can be reviewed without specialized tooling.

For other asset classes, keep an appropriate reviewable representation when it materially helps inspection and verification.

## 4. Name and organize the asset

Use stable, descriptive repository paths. Keep version-, region-, language-, or revision-specific material separate when it actually differs.

Do not create duplicate copies merely to mirror every target if the bytes are identical.

## 5. Verify identity before deduplication

Assets that look or sound identical are not automatically identical.

Before deduplicating across versions, revisions, or languages, compare bytes or cryptographic hashes when practical. If the material is byte-identical:

1. keep one representative copy where practical;
2. record all verified users of that copy in metadata or a manifest;
3. keep version-specific provenance even when the stored asset is shared.

If the data differs, preserve the distinct variants and document the difference.

## 6. Register the asset in a manifest

Use `manifests/` to record identity, provenance, target coverage, source location, hashes, generation method, verification level, and shared usage.

`manifests/example.asset-manifest.json` is the reusable starting point.

Recommended verification values are:

- `Unverified`
- `Observed`
- `Reproduced`
- `Matched`

## 7. Verify the reconstruction

Where practical, verify that the committed asset can be recreated from documented source material and tooling. Record hashes, comparisons, logs, or other evidence when identity matters.

Do not label an asset `Matched` unless the exact-match criterion is defined and satisfied.

## 8. Commit in reviewable batches

Prefer small, coherent asset batches over very large uploads. A batch should be easy to inspect, compare, and revert independently.

For sprite or graphics work, keep the source/reconstructed graphics data, the human-viewable PNG, and the relevant metadata/manifest entry together when practical.

## Review checklist

Before committing an asset batch, check:

- [ ] target identity is recorded or explicitly unknown
- [ ] source provenance is documented
- [ ] reconstructed/editable source material is retained when practical
- [ ] human-viewable PNGs are included for sprite/graphics work when practical
- [ ] hashes or byte comparison were used before deduplicating
- [ ] distinct regional/language/revision variants are preserved when they differ
- [ ] manifest entries are updated
- [ ] verification level is accurate
- [ ] no retail game images, console keys, or redistributable game binaries are included
- [ ] the batch is small enough to review comfortably

See also `PROJECT_STANDARDS.md`, `VERIFICATION.md`, `REPOSITORY_STRUCTURE.md`, and `../manifests/README.md`.