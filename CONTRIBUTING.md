# Contributing

Work in this repository must be specific to Pocket Monsters Let's Go Pikachu and tied to an exact target build.

Before making target claims, complete `PROJECT.md` and `config/target.json` with evidence-backed release, region, revision, and hash data. Use the research and analysis templates, preserve provenance, and keep observations separate from interpretations.

Tools must document supported builds, inputs, outputs, dependencies, error behavior, safety constraints, and verification. Reusable target-independent components should be proposed to the shared [Decompilation repository](https://github.com/SakuraiTsubaki/Decompilation).

Do not commit restricted game images, firmware, extracted proprietary content, secrets, or credentials.

Before review, run:

```text
python scripts/check_repository.py .
python -m unittest discover -s tests -v
```

A pull request must describe scope, evidence, changes, verification results, confidence, and unresolved follow-up.
