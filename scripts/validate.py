#!/usr/bin/env python3
"""Structural checks only; source accuracy still requires editorial review."""
import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("a0", "a1", "a2", "b1", "b2")
FIELDS = ["id", "headword", "ipa_uk", "ukrainian_translation", "part_of_speech",
          "example_en", "example_uk", "level", "category", "source",
          "verification_status", "notes"]
STATUSES = {"verified", "needs_review", "draft"}


def normalize_headword(value):
    return re.sub(r"\s+", " ", (value or "").strip().casefold())


def main():
    errors = []
    ids = {}
    unique_headwords = set()
    entries = {}
    totals = Counter()
    statuses = Counter()

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
                level = folder.upper()
                totals[level] += 1
                where = f"{path.relative_to(ROOT)}:{line}"
                for field in FIELDS:
                    if not (row.get(field) or "").strip():
                        errors.append(f"{where}: empty required field {field}")

                entry_id = (row.get("id") or "").strip()
                headword = (row.get("headword") or "").strip()
                if entry_id:
                    if entry_id in ids:
                        errors.append(f"{where}: duplicate id {entry_id} (first: {ids[entry_id]})")
                    else:
                        ids[entry_id] = where

                key = normalize_headword(headword)
                if key:
                    unique_headwords.add(key)

                # A headword may legitimately have multiple POS/sense records.
                # Flag only a repeated entry with the same level, headword,
                # POS, Ukrainian gloss and example sentence.
                entry_key = (
                    level,
                    key,
                    re.sub(r"\s+", " ", (row.get("part_of_speech") or "").strip().casefold()),
                    re.sub(r"\s+", " ", (row.get("ukrainian_translation") or "").strip().casefold()),
                    re.sub(r"\s+", " ", (row.get("example_en") or "").strip().casefold()),
                )
                if key:
                    if entry_key in entries:
                        errors.append(f"{where}: duplicate entry for {headword!r} (first: {entries[entry_key]})")
                    else:
                        entries[entry_key] = where

                if (row.get("level") or "").strip().upper() != level:
                    errors.append(f"{where}: level does not match folder {level}")

                status = (row.get("verification_status") or "").strip()
                if status not in STATUSES:
                    errors.append(f"{where}: invalid verification_status {status!r}")
                else:
                    statuses[status] += 1
                    source = (row.get("source") or "").strip()
                    if status == "verified" and "The_Oxford_3000_by_CEFR_level.pdf" in source:
                        errors.append(f"{where}: Oxford CEFR list alone cannot verify pronunciation or translation")

                ipa = (row.get("ipa_uk") or "").strip()
                if ipa and not (ipa.startswith("/") and ipa.endswith("/") and len(ipa) > 2):
                    errors.append(f"{where}: IPA must be enclosed in /slashes/")

    print("Records by level: " + ", ".join(f"{level}={totals[level]}" for level in LEVELS))
    print("Verification status: " + ", ".join(f"{status}={statuses[status]}" for status in sorted(STATUSES)))
    print(f"Total unique headwords: {len(unique_headwords)}")
    if errors:
        print("Validation issues:")
        for item in errors:
            print(f"- {item}")
        return 1
    print("Structural checks passed. This does not verify IPA, translations, CEFR assignments or example quality.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
