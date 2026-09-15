# Manifests

This directory stores machine-readable and reviewable inventories for reconstructed source, extracted/recreated assets, version coverage, hashes, and reproducibility metadata.

## Purpose

A manifest should make it possible to answer:

- What is this file or asset?
- Which verified target version, region, language, revision, or build does it belong to?
- Where did it come from inside the target data?
- How was it extracted, reconstructed, or generated?
- How can its identity be verified?
- Is it shared with another version or stored once to avoid duplication?

## Recommended formats

Use JSON, YAML, CSV, or Markdown tables when appropriate. Prefer formats that are easy to review in Git and straightforward to consume from tooling.

## Recommended fields

- `id` — stable logical identifier
- `path` — repository path
- `kind` — source, data, graphic, audio, script, map, table, metadata, etc.
- `target` — version, region, language, revision, update, build
- `source` — archive, container, executable, section, table, symbol, index, or offset
- `size` — byte size when useful
- `hashes` — cryptographic identity hashes
- `generated_by` — tool or command used to produce the committed material
- `verification` — Unverified, Observed, Reproduced, or Matched
- `shared_with` — other targets that use the same byte-identical material
- `notes` — meaningful differences, limitations, or unresolved questions

## Rules

1. Do not invent unknown metadata; use `null`, `unknown`, or `TBD` explicitly.
2. Prefer cryptographic hashes for identity-sensitive files.
3. Do not deduplicate assets only because they look or sound identical; verify byte identity or hashes when practical.
4. Keep provenance sufficient to trace committed material back to a verified source location or reproducible derivation process.
5. Do not place retail ROM images, console keys, or redistributable game binaries in this directory.

See `example.asset-manifest.json` for a reusable starting point and `../docs/PROJECT_STANDARDS.md` for the broader repository rules.
