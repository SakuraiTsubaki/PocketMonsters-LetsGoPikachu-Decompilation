# Tests

Tests cover repository policy, target-specific tools, reconstructed logic, data formats, regressions, comparisons, and reproducible build properties.

Prefer small independently distributable fixtures. When a test requires a user-supplied restricted input, identify it by hash, skip safely when absent, and document setup without redistributing it.
