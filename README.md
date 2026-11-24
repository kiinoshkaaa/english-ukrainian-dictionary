# English–Ukrainian Dictionary (British English, Pre-A1–B2)

A carefully curated learner's dictionary for Ukrainian-speaking learners of British English.

## Editorial principles
- Target variety: contemporary Standard Southern British English (SSBE).
- Pronunciation: UK IPA; records are marked verified only after checking an individual authoritative dictionary entry.
- Translations and example translations: Ukrainian.
- CEFR levels are assigned from published vocabulary references, not from arbitrary word-count targets.
- Never label a record verified unless its pronunciation and meaning have been checked against a cited source.

## Vocabulary scope and reference counts
The main core list is the Oxford 3000, whose words are assigned to A1, A2, B1 and B2. Oxford University Press describes the revised list's approximate level profile as:
- A1: about 900 words
- A2: about 800 words
- B1: about 700 words
- B2: about 600 words

These are the published approximate counts for the Oxford 3000, not universal CEFR quotas and not a promise that every dictionary must contain exactly these numbers. The CEFR itself does not prescribe a fixed vocabulary count for each level.

- **Pre-A1 (formerly called A0 in this project):** an optional foundation supplement. It is not an official CEFR level and must not be presented as one.
- **A1–B2:** preserve Oxford's level labels for each headword/part of speech or sense where the source distinguishes them.
- **B2 extensions:** additional B2 entries from Oxford 5000 may be added only when the source labels them B2. C1 entries are excluded.
- Use English Vocabulary Profile as a secondary reference where a word has different meanings or uses at different levels.
- A headword may appear at more than one level only when the source supports a different level for a distinct meaning, part of speech or use.
- Do not pad or truncate a level to reach a desired number. Completeness and accurate classification take priority.

## Primary references
- Oxford 3000 and 5000 (current online wordlist; primary CEFR reference): https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000
- Oxford 3000 and 5000 overview: https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000
- Oxford 3000 full list (PDF): https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000.pdf
- Oxford 3000 by CEFR level (PDF): https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf
- Oxford's explanation of the CEFR: https://www.oxfordlearnersdictionaries.co.uk/about/wordlists/cefr
- English Vocabulary Profile: https://englishprofile.org/

## Data format
CSV fields: id, headword, ipa_uk, ukrainian_translation, part_of_speech, example_en, example_uk, level, category, source, verification_status, notes.

See data/schema.json and sources/references.md.

## Status
The A1 inventory contains 893 records. A2 currently contains 993 records representing 867 unique normalized headwords; multiple records may represent different parts of speech or senses. The A2 headword inventory and its part-of-speech coverage have been reconciled against the Oxford 3000 A2 reference, with British spelling and multiword-expression normalization and current-online/static-PDF conflicts documented in `sources/a2-reconciliation.md`. This is an inventory and part-of-speech reconciliation, not a claim that every translation and original example pair in all 993 records has been independently re-audited. The current Oxford 3000 online wordlist is the primary source for CEFR assignments by part of speech. The two official Oxford 3000 PDFs are retained as historical reference snapshots and do not agree on every assignment. Both the by-CEFR PDF and the current online list place `top` noun/adjective and `experiment` noun at A2, with `experiment` verb at B1; the separate full Oxford 3000 PDF differs by placing `top` noun/adjective and `experiment` noun/verb at B1. Repository-wide ID uniqueness was audited while beginning B1; three cross-level collisions were corrected by assigning globally unique IDs to the A2 `ski` adjective, `surprise` verb, `tie` noun and B1 `experiment` verb. Further static-PDF/current-online differences for `free`, `ride` and `tidy` are documented in the relevant A2 records; the current online per-part-of-speech classification takes precedence. The by-CEFR PDF lists all uses of `either` at A2, and the inventory keeps these uses in separate A2 records. Cambridge labels the physical-position adjective sense of `top` B1; this is an additional source difference recorded in the entry notes. The Oxford A2 PDF also includes `all right`, `any more`, and `per cent`; these are represented in the inventory. The adverb `all` is recorded at A2 separately from its A1 determiner/pronoun use. Distinct parts of speech and distinct senses may have separate records. The A0 foundation supplement contains 3 records; B1 currently contains 320 records, including `experiment` verb and 319 additional entries; its candidate inventory, reconciled batches and outstanding individual dictionary checks are documented in `sources/b1-reconciliation.md`. The latest 265 B1 candidates from `belief` through `guilty` remain `needs_review` until their individual UK IPA and selected senses are fully checked. B2 currently contains 0 records. Across all level files there are 2,209 records: 1,943 marked `verified` and 266 marked `needs_review` (the `autumn` noun level discrepancy and 265 newly added B1 records awaiting individual dictionary verification). A `verified` status is a data label, not proof by itself: each record still requires an individual check of UK pronunciation, meaning, Ukrainian gloss and original example pair. Structural validation does not establish editorial accuracy. CEFR placement follows the relevant published vocabulary list; conflicting classifications must be documented rather than silently resolved. These counts describe the current repository contents, not completion of the full A0–B2 vocabulary scope.

## Workflow
1. Build level-specific candidate inventories from the Oxford lists.
2. Preserve the source's CEFR assignment and part-of-speech/sense distinctions.
3. Verify UK IPA and core meanings against cited dictionary sources.
4. Write original, natural British-English examples and accurate Ukrainian translations.
5. Run scripts/validate.py and manually review flagged records.
6. Generate the PDF only after the vocabulary data and Unicode font rendering have been checked.

Structural validation does not replace editorial verification of IPA, translations, CEFR assignments or examples.
