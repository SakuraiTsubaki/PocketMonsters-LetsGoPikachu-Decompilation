# Target Profile: Pocket Monsters Let's Go Pikachu

## Known repository scope

- Repository: `SakuraiTsubaki/PocketMonsters-LetsGoPikachu-Decompilation`
- Working target name: Pocket Monsters Let's Go Pikachu
- Platform family: Nintendo Switch
- Series generation: Generation VII
- Exact release, region, revision, and build: **not yet selected**

The repository name is a working label, not proof of a particular binary. No address, symbol, format, or behavior should be treated as target fact until the exact build is identified.

## Identity checklist

Record all available items before substantive reconstruction:

- official title and product identifier;
- platform and execution environment;
- region, language, revision, update, and distribution form;
- hashes for user-supplied images, executables, modules, or manifests;
- executable/container layout and relevant segment identifiers;
- analysis, extraction, compiler, linker, and SDK tool versions;
- legal provenance and distribution constraints for every input;
- differences from related versions that affect addresses, formats, or behavior.

Store machine-readable identifiers in `config/target.json`. Store restricted inputs outside Git.

## Initial research priorities

- Fingerprint the exact title, update, distribution, and executable build IDs before assigning addresses or symbols.
- Inventory executable modules, relocations, runtime/SDK interfaces, RomFS layout, and version-specific boundaries.
- Document target-specific serialization, archives, compression, graphics, text, audio, maps, and scripts.
- Keep keys, firmware, packages, decrypted modules, and extracted content outside Git; record only reproducible identifiers.
- Build deterministic extraction, symbol, format, and cross-version comparison tools for user-supplied inputs.

## First milestone

The foundation milestone is complete when the exact target build is recorded, the initial file/executable map is reproducible, at least one research record has been promoted to an analysis with stated confidence, and all commands needed to repeat that result are documented.
