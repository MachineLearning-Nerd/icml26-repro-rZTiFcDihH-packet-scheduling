"""Verify that an additive Space candidate preserves the judged file tree."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


MODIFIED_ADDITIVELY = {"logbook.json", "pages/index.md"}


def _files(root: Path) -> dict[str, Path]:
    return {
        path.relative_to(root).as_posix(): path
        for path in root.rglob("*")
        if path.is_file() and ".cache" not in path.relative_to(root).parts
    }


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--judged", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    old = _files(args.judged)
    new = _files(args.candidate)
    missing = sorted(set(old) - set(new))
    unchanged = sorted(set(old) - MODIFIED_ADDITIVELY)
    changed_unexpectedly = [
        relative for relative in unchanged if _sha(old[relative]) != _sha(new[relative])
    ]
    old_index = old["pages/index.md"].read_text(encoding="utf-8")
    new_index = new["pages/index.md"].read_text(encoding="utf-8")
    index_preserved_as_prefix = new_index.startswith(old_index)

    old_logbook = json.loads(old["logbook.json"].read_text(encoding="utf-8"))
    new_logbook = json.loads(new["logbook.json"].read_text(encoding="utf-8"))
    old_children = {
        child["slug"]: child for child in old_logbook["root"]["children"]
    }
    new_children = {
        child["slug"]: child for child in new_logbook["root"]["children"]
    }
    old_navigation_preserved = all(
        new_children.get(slug) == child for slug, child in old_children.items()
    )
    new_paths = sorted(set(new) - set(old))
    passed = (
        not missing
        and not changed_unexpectedly
        and index_preserved_as_prefix
        and old_navigation_preserved
        and new_logbook["space_id"] == "DineshAI/rZTiFcDihH"
    )
    result = {
        "judged_revision": "8f84eab5754de43ee08dfc1bb9a792cde93cc6ab",
        "space_id": new_logbook["space_id"],
        "old_file_count": len(old),
        "candidate_file_count": len(new),
        "old_file_names_subset_of_candidate": not missing,
        "missing_old_files": missing,
        "unchanged_old_files_hash_match": not changed_unexpectedly,
        "changed_unexpectedly": changed_unexpectedly,
        "modified_additively": sorted(MODIFIED_ADDITIVELY),
        "old_index_preserved_as_prefix": index_preserved_as_prefix,
        "old_navigation_preserved": old_navigation_preserved,
        "new_paths": new_paths,
        "pass": passed,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
