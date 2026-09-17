#!/usr/bin/env python3
"""Validate a target decompilation repository without third-party packages."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

REQUIRED_PATHS = (
    ".editorconfig", ".gitattributes", ".gitignore", "README.md",
    "CONTRIBUTING.md", "SECURITY.md", "LICENSE", "PROJECT.md",
    "ARTIFACT_POLICY.md", "analysis/README.md", "analysis/template.md",
    "artifacts/README.md", "artifacts/graphics/README.md",
    "config/README.md", "config/target.json", "docs/workflow.md",
    "logs/README.md", "manifests/README.md", "patches/README.md",
    "progress/README.md", "research/README.md", "research/template.md",
    "src/README.md", "tests/README.md", "tools/README.md",
)
TARGET_FIELDS = (
    "repository", "target", "platform_family", "generation",
    "identity_status", "release", "region", "revision", "hashes",
)
ROM_BINARY_SUFFIXES = {
    ".3ds", ".cci", ".cia", ".gb", ".gba", ".gbc", ".iso",
    ".nds", ".nsp", ".rom", ".xci",
}
TEXT_SUFFIXES = {
    "", ".c", ".cc", ".cfg", ".cpp", ".csv", ".h", ".hpp", ".inc",
    ".ini", ".json", ".log", ".md", ".py", ".s", ".sh", ".toml",
    ".tsv", ".txt", ".xml", ".yaml", ".yml",
}
GRAPHICS_DIRECTORY_NAMES = {
    "graphics", "sprites", "images", "palettes", "fonts", "icons", "tiles",
}
SKIP_PARTS = {".git", ".venv", "node_modules"}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file() and not any(part in SKIP_PARTS for part in path.parts):
            yield path


def validate_graphics_previews(root: Path) -> list[str]:
    errors: list[str] = []
    for directory in root.rglob("*"):
        if not directory.is_dir() or directory.name.lower() not in GRAPHICS_DIRECTORY_NAMES:
            continue
        files = [path for path in directory.rglob("*") if path.is_file()]
        payloads = [path for path in files if path.name.lower() != "readme.md"]
        if payloads and not any(path.suffix.lower() == ".png" for path in files):
            relative = directory.relative_to(root)
            errors.append(f"graphics work has no PNG preview: {relative}")
    return errors


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_PATHS:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    target_path = root / "config/target.json"
    if target_path.is_file():
        try:
            target = json.loads(target_path.read_text(encoding="utf-8"))
            for field in TARGET_FIELDS:
                if field not in target:
                    errors.append(f"missing target field: {field}")
            if target.get("identity_status") not in {"unselected", "identified", "verified"}:
                errors.append("invalid identity_status")
            if not isinstance(target.get("hashes"), list):
                errors.append("target hashes must be a list")
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            errors.append(f"invalid config/target.json: {error}")

    for path in iter_files(root):
        relative = path.relative_to(root)
        if path.suffix.lower() in ROM_BINARY_SUFFIXES:
            errors.append(f"blocked ROM binary: {relative}")
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            data = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"text file is not UTF-8: {relative}")
            continue
        for number, line in enumerate(data.splitlines(), 1):
            if line.endswith((" ", "\t")):
                errors.append(f"trailing whitespace: {relative}:{number}")
        if data and not data.endswith("\n"):
            errors.append(f"missing final newline: {relative}")

    errors.extend(validate_graphics_previews(root))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"error: {error}")
        return 1
    print(f"repository validation passed: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
