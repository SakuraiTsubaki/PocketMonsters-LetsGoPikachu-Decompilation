# Contributing

Work in this repository must be tied to an exact Pocket Monsters Let's Go Pikachu build and preserve its complete non-ROM evidence trail.

Before making target claims, complete `PROJECT.md` and `config/target.json`. Keep the ROM binary outside Git, but commit every storable non-ROM item created, collected, extracted, converted, normalized, or organized during the work.

Required retained material includes analysis, research, reports, documentation, scripts, source, tools, configuration, logs, manifests, checklists, comparison tables, structured data, graphics, sprites, images, palettes, fonts, icons, tiles, converted data, patches, and verification results.

Graphics-related work is incomplete unless actual PNG previews, sheets, renders, or comparisons are committed alongside the underlying data and metadata.

Reusable target-independent components belong in the shared [Decompilation repository](https://github.com/SakuraiTsubaki/Decompilation).

Before review, run:

```text
python scripts/check_repository.py .
python -m unittest discover -s tests -v
```

A pull request must describe target identity, scope, provenance, retained artifacts, verification, confidence, and follow-up.
