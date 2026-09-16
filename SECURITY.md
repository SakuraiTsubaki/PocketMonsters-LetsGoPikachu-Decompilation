# Security Policy

Security reports are relevant when repository tools, parsers, build helpers, workflows, or supplied examples could execute untrusted input or affect contributor systems.

Do not publish practical exploit details in a public issue. Use GitHub's private vulnerability reporting feature when available. Treat all external binaries, archives, symbols, metadata, and user-supplied paths as untrusted.

Tools should prevent path traversal, unsafe archive extraction, shell interpolation, uncontrolled overwrite, implicit credential use, and destructive defaults.
