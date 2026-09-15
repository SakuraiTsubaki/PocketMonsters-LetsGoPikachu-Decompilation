# Phase 01 — Executable Mapping

## Goal

Establish a reproducible executable baseline for the exact local Pokémon: Let's Go, Pikachu! target before function naming or source reconstruction begins.

## Inputs

Use only a locally owned/extracted target. Do not commit cartridge images, encrypted title packages, keys, or extracted proprietary executable binaries.

Expected local inputs include:

- extracted application tree
- ExeFS modules such as `main`, `rtld`, `sdk`, and `subsdk*`
- RomFS tree

## Step 1 — Inventory

```bash
python tools/inventory_extracted_tree.py /path/to/extracted-game \
  --project "Pokemon: Let's Go, Pikachu!" --platform "Nintendo Switch" \
  -o manifests/local/inventory.json
```

## Step 2 — Map each NSO0 module

Run the inspector separately for every NSO0 present in ExeFS:

```bash
python tools/inspect_nso.py /path/to/ExeFS/main -o manifests/local/nso-main.json
python tools/inspect_nso.py /path/to/ExeFS/rtld -o manifests/local/nso-rtld.json
python tools/inspect_nso.py /path/to/ExeFS/sdk -o manifests/local/nso-sdk.json
```

Repeat for all `subsdk*` modules that actually exist in the target.

Record:

- Module ID / build ID
- `.text`, `.rodata`, and `.data` file ranges
- module-relative memory ranges
- stored and mapped sizes
- compression flags
- hash-check flags
- BSS size
- dynamic string/symbol table metadata

## Step 3 — Establish executable images

Compressed NSO segments must be decompressed locally before instruction-level matching. Never commit proprietary NSO binaries or decompressed sections.

Treat `main`, `rtld`, `sdk`, and each `subsdk*` as separate modules. Do not collapse their address spaces into one guessed flat image.

## Step 4 — First reconstruction outputs

Repository-safe outputs include function/symbol maps, per-module section maps, call-graph metadata, reconstructed source, data-structure notes, scripts, tests, hashes, and verification manifests.

## Evidence status

Until a real local target has been inventoried, all game/revision-specific values remain **Unverified**.
