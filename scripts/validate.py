#!/usr/bin/env python3
"""Structural checks only; human source review is still required."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("a0", "a1", "a2", "b1", "b2")
FIELDS = ["id", "headword", "ipa_uk", "ukrainian_translation", "part_of_speech",
          "example_en", "example_uk", "level", "category", "source",
          "verification_status", "notes"]
STATUSES = {"verified", "needs_review", "draft"}


def main():
    errors = []
    ids = set()
    words = {}
    total = verified = 0
    for folder in LEVELS:
        path = ROOT / "data" / folder / "words.csv"
        if not path.exists():
            errors.append(f"Missing file: {path.relative_to(ROOT)}")
            continue
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != FIELDS:
                errors.append(f"{path.relative_to(ROOT)}: unexpected CSV header")
                continue
            for line, row in enumerate(reader, 2):
                total += 1
                where = f"{path.relative_to(ROOT)}:{line}"
                for field in FIELDS:
                    if not (row.get(field) or "").strip():
                        errors.append(f"{where}: empty required field {field}")
                entry_id = (row.get("id") or "").strip()
                headword = (row.get("headword") or "").strip()
                if entry_id and entry_id in ids:
                    errors.append(f"{where}: duplicate id {entry_id}")
                ids.add(entry_id)
                key = re.sub(r"\\s+", " ", headword.casefold())
                if key and key in words:
                    errors.append(f"{where}: duplicate headword {headword} (first: {words[key]})")
                elif key:
                    words[key] = where
                if (row.get("level") or "").strip().lower() != folder:
                    errors.append(f"{where}: level does not match folder {folder.upper()}")
                status = (row.get("verification_status") or "").strip()
                if status and status not in STATUSES:
                    errors.append(f"{where}: invalid verification_status {status}")
                if status == "verified":
                    verified += 1
    print(f"Records: {total}; marked verified: {verified}")
    if errors:
        print("Validation issues:")
        print("\\n".join(f"- {item}" for item in errors))
        return 1
    print("Structural checks passed. IPA, translations, CEFR levels and examples still require editorial review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
