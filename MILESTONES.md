# Milestones: Pocket Monsters Let's Go Pikachu

This roadmap governs research, tooling, analysis, reconstruction, and preservation for `SakuraiTsubaki/PocketMonsters-LetsGoPikachu-Decompilation`.

## Ground rules

- Milestones are evidence gates, not date promises or percentages.
- Complete them in dependency order unless an independent experiment is clearly labeled.
- Original, modified, and rebuilt ROM or complete game-package binaries remain local and are never committed.
- Commit every other storable work product: notes, references, source, scripts, tools, settings, logs, manifests, tables, CSV/JSON/YAML, patches, validation evidence, and generated outputs.
- Graphics and sprite work must include actual viewable PNG results alongside encoded data and metadata.
- Normal diagnostics and validation belong in the repository; this roadmap does not create a separate bug-eradication program.
- A milestone becomes complete only when its exit criteria are backed by committed evidence.

## Target snapshot

| Field | Current value |
| --- | --- |
| Target | Pocket Monsters Let's Go Pikachu |
| Platform family | Nintendo Switch |
| Generation | Generation VII |
| Identity status | `unselected` |

The target identity is currently unselected. Release, region, revision, edition, update level, and hashes must remain empty until verified from authorized local inputs.

## Dependency chain

`T0 → T1 → T2 → T3 → T4 → T5 → T6`

Parallel work is allowed inside a milestone, but later results must cite the exact earlier manifests and tool versions they depend on.

## T0 — Scope and exact target identity

**Goal:** establish the precise legal research target and a reproducible input contract.

**Required outputs**

- Complete `config/target.json` with release, region/language, revision or version, edition/update context, and cryptographic hashes.
- Provenance notes that identify how local inputs were obtained without committing protected game images or secrets.
- A deterministic identity verifier and fixture-based tests.
- A target-selection decision record listing rejected or still-unknown candidates.
- A machine-readable matrix when more than one variant is intentionally in scope.

**Exit criteria**

- A fresh authorized local input can be accepted or rejected deterministically.
- Every scope claim is either supported by evidence or explicitly marked unknown.
- CI validates the target schema without requiring ROM bytes.

## T1 — Reproducible structural inventory

**Goal:** produce a deterministic, reviewable map of the target before interpretation.

**Required outputs**

- Edition/version manifest; package-derived non-ROM metadata; ExeFS, RomFS, NSO/module, symbol, relocation, compression, update, and downloadable-content inventories.
- Stable CSV/JSON manifests containing offsets, sizes, hashes, hierarchy, and tool versions where applicable.
- Extraction commands, environment notes, logs, and repeat-run comparison results.
- Sanitized synthetic fixtures covering parser boundaries and malformed-input handling.

**Exit criteria**

- Two clean runs on the same identified input produce identical manifests.
- Every extracted or indexed item has traceable source coordinates.
- Tools fail safely and explain unsupported structures without silently guessing.

## T2 — Executable and symbol map

**Goal:** turn executable regions into a navigable evidence-backed code map.

**Required outputs**

- AArch64 executable/module maps; functions, call edges, relocations, symbols, data references, compiler/toolchain fingerprints, and confidence records.
- Machine-readable function, section, relocation, symbol, and reference tables.
- Naming conventions that distinguish confirmed, probable, and hypothetical symbols.
- Reproducible disassembly/decompilation commands and representative annotated slices.
- Comparison tables for every intentionally supported variant.

**Exit criteria**

- Entry points and major execution regions are accounted for.
- Every promoted symbol cites address/range evidence and confidence.
- Generated maps are deterministic and consumable by later reconstruction tools.

## T3 — Resource formats and asset pipelines

**Goal:** document and reproduce the target's non-code data formats.

**Required outputs**

- RomFS formats, tables, scripts, models, textures, shaders, UI, fonts, audio, localization, and converters with manifests and PNG previews.
- Round-trip or semantic-equivalence tests for each supported converter.
- Source-coordinate and hash manifests for converted results.
- PNG sheets, previews, or comparisons for graphics, sprites, icons, fonts, palettes, tiles, textures, and other visual work.
- Format specifications separating verified fields from unresolved bytes.

**Exit criteria**

- Each claimed format has at least one reproducible fixture and documented command.
- Converted outputs retain provenance and can be regenerated deterministically.
- Visual pipelines include reviewable PNG output, not only metadata.

## T4 — Reviewed reconstruction slices

**Goal:** reconstruct bounded components with clear evidence and interfaces.

**Required outputs**

- Small, reviewable source or data slices linked to original coordinates and manifests.
- Buildable or testable boundaries, interface notes, assumptions, and confidence records.
- Equivalence checks appropriate to the component: bytes, layout, decoded data, control flow, state transitions, or observable behavior.
- Generated files, maps, logs, and comparison reports needed to audit each slice.

**Exit criteria**

- Every slice can be regenerated and validated without committing a ROM.
- Reviewers can trace each conclusion from input identity through tooling to output.
- Unknown behavior remains explicitly marked instead of being filled by invention.

## T5 — Integrated reproducible workflow

**Goal:** connect identity, extraction, analysis, conversion, reconstruction, and validation into one documented workflow.

**Required outputs**

- A clean-environment bootstrap and ordered command manifest.
- Version-pinned tool configuration and deterministic output locations.
- Cross-component integration tests and representative end-to-end fixtures.
- Coverage/gap reports for code regions, resource families, variants, and unsupported cases.
- Build or reassembly instructions that consume a user-supplied local input when required and never publish a complete game image.

**Exit criteria**

- A new contributor can reproduce documented non-ROM outputs from the declared inputs and commands.
- CI verifies all repository-owned tooling and fixtures.
- Generated differences are explained by a checked-in report or treated as a failed validation.

## T6 — Evidence-backed research release

**Goal:** publish a coherent, reusable research release without overstating completeness.

**Required outputs**

- Versioned documentation, schemas, tools, source, data, manifests, and generated non-ROM artifacts.
- A release manifest listing exact commits, tool versions, supported identities, coverage, and known unknowns.
- Archived logs and validation summaries sufficient to audit the release.
- Migration notes for schema/tool changes and a backlog for the next evidence cycle.

**Exit criteria**

- All included claims have confidence labels and inspectable evidence.
- The release contains no ROM or equivalent complete game-package binary, credentials, keys, or machine-local cache.
- Every graphics/sprite deliverable has its required PNG review artifact.
- The release statement describes measured coverage rather than claiming unsupported completion.

## Family coordination

Coordinate Nintendo Switch findings with Let's Go Eevee and keep paired-version deltas machine-readable.

Shared parsers, schemas, validation libraries, and cross-target methods should be promoted to [`SakuraiTsubaki/Decompilation`](https://github.com/SakuraiTsubaki/Decompilation) only after they are demonstrated on committed fixtures. This target repository retains its own input identities, target-specific manifests, interpretations, and outputs.

## Status recording

Use one of `planned`, `in-progress`, `blocked`, or `evidence-complete` in future progress records. Record the supporting commit, commands, artifacts, and remaining limitations whenever a status changes. This file intentionally assigns no completion status without that evidence.
