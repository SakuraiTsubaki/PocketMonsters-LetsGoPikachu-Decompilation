# Verification Guide

This document defines how findings and reconstructed output should be verified before being treated as established project knowledge.

## Verification levels

- **Unverified** — a proposal, note, hypothesis, or imported claim that has not been independently checked.
- **Observed** — confirmed directly in a specific target build, executable, extracted file, or runtime observation.
- **Reproduced** — the observation can be recreated using documented steps, tooling, inputs, and target information.
- **Matched** — reconstructed output is verified against the intended target using hashes, byte comparison, deterministic output, or another clearly defined exact-match criterion.

## Minimum evidence

A verification record should include, when relevant:

- target game, region, language, revision, update, or build
- cryptographic hashes or stable identifiers
- file names, archive paths, offsets, symbols, addresses, or table identifiers
- tooling and commands used
- expected and actual output
- logs, diffs, manifests, screenshots, or test results
- known limitations and unresolved mismatches

## Recommended workflow

1. Define exactly what is being verified.
2. Identify the target version in `VERSIONS.md`.
3. Reproduce the finding from documented inputs and steps.
4. Compare output using the strongest practical method.
5. Record the result in documentation, a verification issue, or a manifest.
6. Update `PROJECT_STATUS.md` when the result changes project-level status.

## Matching claims

Do not describe a subsystem, asset, executable, or complete build as **matched** unless the matching criterion is explicit and reproducible. Behavioral similarity alone should be labeled separately from byte-exact or hash-exact matching.

ROM images, console keys, and other redistributable retail game binaries must not be committed as verification evidence.