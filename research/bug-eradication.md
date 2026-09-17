# Bug / Glitch Eradication Track — Pocket Monsters Let's Go Pikachu

## Objective

Remove every reproducible bug, glitch, crash, softlock, incorrect battle rule, text/data error, visual/audio defect, overflow/underflow, invalid state transition, save-risk condition, communication failure, and other unintended behavior that can be demonstrated in the selected Pocket Monsters Let's Go Pikachu target.

This is a living evidence-backed inventory, not a claim that public lists are exhaustive.

## Target state

- Repository target: Pocket Monsters Let's Go Pikachu
- Platform: Nintendo Switch
- Latest official update baseline: Ver. 1.0.2
- Exact game/update/region/revision/hash in this repository: **not selected yet** (`config/target.json`)
- Complete game-image/package binaries remain outside Git; hashes, extracted non-ROM data, patches, tests, logs, and reports belong in the repository.

## Required workflow

1. Fingerprint the exact base game and update layer.
2. Inventory executable modules, RomFS/data archives, scripts, tables, text, models, audio, save structures, and communication-related data.
3. Reproduce every known issue on the selected build when applicable.
4. Locate the exact code/data/resource cause.
5. Apply the smallest behavior-correct fix while preserving intended original content and version behavior.
6. Add deterministic regression coverage.
7. Re-test save migration, local/Internet communication paths where reproducible, GO Park interactions, encounters, partner systems, battles, and post-game state.
8. Preserve evidence for fixed, not-applicable, cannot-reproduce, and research-needed cases.

## Officially fixed issues that must remain fixed

### Ver. 1.0.1

- Mystery Gift Pokémon failing to register in the Pokédex if the game is closed without saving after receipt.
- Pokémon Markings and Judge function square/star ordering being reversed.
- Additional unspecified gameplay fixes.

### Ver. 1.0.2

- Link Trade becoming unusable after a disconnect during trade when play time is `999:59`.
- Mystery Gift serial-code/password input remaining locked after ten incorrect attempts even after the intended timeout.
- Previous 1.0.1 fixes retained.

## Known latest-version candidates to investigate and eliminate

### Partner / arithmetic

- Partner-power favored Golden Razz Berry counter overflow caused by adding before applying the intended cap.

### Encounter / overworld

- Double encounter hitbox case: touching two wild Pokémon at once starts one encounter while both wild Pokémon despawn.
- Overworld Trainer line-of-sight skip possible at high riding speed (notably Rapidash/Aerodactyl); determine intended detection rules before patching.

### Battle / text

- Opposing Trainer item use can display player-directed text such as "You used a (item)." instead of identifying the opponent/NPC action.

### Broad audit categories

- Integer overflow/underflow and cap-order errors in partner, catch-combo, candy, AV/stat, encounter, and reward counters.
- Save-state transitions around Mystery Gift, GO Park, transfers, party/box changes, evolution, and Pokédex registration.
- Communication reconnect/timeout state machines beyond the officially fixed `999:59` case.
- Version-exclusive partner behavior, field move/Secret Technique transitions, riding collision, camera, spawn/despawn, and scripted-event edge cases.
- Text speaker ownership, grammar, gender/language branching, icon/mark order, and UI state consistency.

## Evidence status rules

- `CONFIRMED-ROM`: reproduced against the selected game/update hash.
- `CONFIRMED-DATA`: directly proven by extracted code/data but not yet reproduced in gameplay.
- `OFFICIAL-FIX`: documented by Nintendo official update notes.
- `PUBLIC-REPORT`: reproducible public report not yet confirmed against our target.
- `RESEARCH-NEEDED`: trigger/cause/version scope remains uncertain.
- `FIXED`: patch applied and regression verification passed.

## Primary references

- Nintendo Korea — Let's Go Pikachu / Eevee Ver. 1.0.2 update notes: https://www.nintendo.com/kr/switch/pikachu_eevee/updateData.html
- Nintendo Support — Let's Go Pikachu / Eevee update history: https://en-americas-support.nintendo.com/app/answers/detail/a_id/43254/
- Bulbapedia — Generation VII glitch index: https://bulbapedia.bulbagarden.net/wiki/List_of_glitches_in_Generation_VII
- Bulbapedia — Generation VII battle glitches: https://bulbapedia.bulbagarden.net/wiki/List_of_battle_glitches_in_Generation_VII
- Bulbapedia — Generation VII overworld glitches: https://bulbapedia.bulbagarden.net/wiki/List_of_overworld_glitches_in_Generation_VII

## Immediate blocker

No exact Let's Go Pikachu game/update build is selected in `config/target.json`. Do not invent offsets, file names, symbols, functions, package layouts, or patch bytes. Fingerprint the actual input first, then convert each candidate above into a build-specific reproduction and regression test.
