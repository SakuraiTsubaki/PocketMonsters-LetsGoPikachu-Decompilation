# Project Standards

This document defines shared repository conventions for source reconstruction, research data, manifests, and project assets. Platform-specific rules may extend these standards once the target architecture is verified.

## Naming conventions

- Prefer stable, descriptive, ASCII-safe file and directory names unless the original format requires otherwise.
- Use lowercase names for new generic directories and tooling paths unless a verified upstream convention requires different casing.
- Avoid spaces in machine-consumed paths when a clear hyphen or underscore is sufficient.
- Preserve verified original identifiers when they carry technical meaning; document aliases instead of silently renaming them.
- Include version, language, revision, or region identifiers in paths or metadata when material differs between targets.

## Source and generated data

- Prefer editable source, metadata, and reproducible conversion steps over opaque generated output.
- Generated files should identify their source inputs and generation method when practical.
- Do not treat generated output as authoritative when an editable source representation exists.
- Keep tools and scripts required to reproduce committed derived data in the repository whenever practical.

## Asset policy

- Human-viewable assets such as PNG previews may be committed when they help inspection, review, or verification.
- Preserve the corresponding reconstructed source data or documented extraction/conversion path where practical.
- Byte-identical assets shared by versions, revisions, or languages should normally be stored once and referenced through metadata, manifests, or version maps instead of duplicated.
- Do not deduplicate files merely because they look visually or audibly identical; confirm identity using hashes or byte comparison when practical.
- Record meaningful differences between regional, language, revision, and update variants.

## Manifest policy

Manifests should use a structured, reviewable format such as JSON, YAML, CSV, or Markdown tables as appropriate. Entries should record enough information to identify and reproduce the material they describe.

Recommended fields include:

- logical identifier or asset name
- repository path
- target version / region / language / revision
- source container, archive, section, table, or executable identifier
- source offset, index, symbol, or record identifier when known
- file size where useful
- cryptographic hash for identity-sensitive material
- extraction or generation tool / command
- verification level
- notes and known differences

Do not invent unknown metadata. Use an explicit `unknown`, `TBD`, or equivalent state when information has not been verified.

## Evidence and provenance

- Separate confirmed observations from hypotheses.
- Record the target build or version associated with technical claims.
- Prefer hashes and stable identifiers over filenames alone for identity checks.
- Keep enough provenance to trace reconstructed data back to its verified source location or derivation process.
- Update `VERSIONS.md`, `PROJECT_STATUS.md`, and verification records when newly confirmed information changes project scope.

## Repository boundaries

- Do not commit retail ROM images, decrypted game images, console keys, or other redistributable game binaries.
- Reconstructed source, project data, analysis, manifests, tooling, documentation, and reviewable extracted/recreated assets may belong in the repository when they serve the decompilation project.
- Temporary dumps, local caches, and disposable build output should remain outside version control unless they are intentionally promoted into documented project material.

## Platform-specific extensions

Do not force conventions from another generation or platform onto this project. Once executable, archive, resource, and build layouts are verified, add platform-specific naming, directory, manifest, and verification rules that reflect the actual target architecture.