# Research Guide

This guide defines how reverse-engineering findings should be recorded so that later contributors can reproduce and verify them.

## Evidence first
Record target version/revision, file or executable name, offsets or addresses when meaningful, hashes or identifiers, tools or commands used, and comparison notes.

## Confidence levels
- **Hypothesis** — plausible but not confirmed.
- **Observed** — directly seen in a target build or extracted data.
- **Reproduced** — recreated with documented steps.
- **Matched** — reconstructed output verified against the intended target.

Do not silently promote hypotheses into facts.

## Research workflow
1. Define the exact question.
2. Identify the target version and evidence source.
3. Record observations before interpretation.
4. Build the smallest reproducible test or extraction method possible.
5. Compare across versions when relevant.
6. Document the result in `docs/`, code comments, manifests, or a verification issue.
7. Update project status, versions, or roadmap documents when scope or progress changes.

## Repository boundaries
Do not commit retail ROM/game images, decrypted distribution images, console keys, or other redistributable game binaries. Reconstructed source, tooling, documentation, manifests, metadata, and project-created assets should remain reproducible and reviewable.