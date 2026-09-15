# Phase 02 — Source Reconstruction Bootstrap

## Objective

Establish the first verified source-reconstruction map for **Pokémon: Let's Go, Pikachu!** from a locally extracted Nintendo Switch application tree while keeping cartridge images, encrypted packages, keys, and proprietary executable payloads out of Git.

## Required local inputs

- extracted ExeFS directory
- extracted RomFS directory

## Generated metadata

1. `inventory_extracted_tree.py` — full path/size/SHA-256 inventory
2. `inspect_nso.py` — one NSO0 module header/segment map
3. `map_nso_modules.py` — complete ExeFS NSO module map (`main`, `rtld`, `sdk`, `subsdk*`, others)
4. `classify_romfs.py` — structural RomFS clustering by path, extension, magic, size, and hash

Recommended outputs:

- `analysis/executable/nso_modules.json`
- `analysis/romfs/classification.json`

## Module rule

Keep `main` separate from runtime-loader, SDK, and subsdk modules. Function names and ownership must not be assigned solely from module position; labels require executable or data-flow evidence.

## Reconstruction queues

After module/segment verification, classify code and data into startup/runtime, filesystem/resource loading, event/script, field/map, battle, Pokémon data, UI/text, save, communication/GO integration, partner systems, graphics/audio, and other verified subsystems.

## Pikachu ↔ Eevee comparison

Use `Sakurai/tools/compare_gen7_inventories.py` after both complete inventories exist. Separate identical files, same-path modifications, version-only resources, and identical content moved to different paths.

Do not import Alola executable addresses, structures, or assumptions into Let's Go without independent verification; the platform and executable format differ.

## Exit criteria

- exact target/update recorded
- all NSO0 modules inventoried
- `main` segment layout verified
- full RomFS inventory reproducible
- first executable/resource families evidence-backed
- Pikachu/Eevee machine-generated difference baseline produced
