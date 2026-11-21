# English–Ukrainian Dictionary (British English, A0–B2)

A carefully curated learner's dictionary for Ukrainian-speaking learners of British English.

## Editorial principles
- Target variety: contemporary Standard Southern British English (SSBE).
- Pronunciation: UK IPA, checked against authoritative learner's dictionaries.
- Translations and example translations: Ukrainian.
- Learning bands: A0 (project-defined foundation), A1, A2, B1 and B2.
- Never label a record verified unless its pronunciation and meaning have been checked against a cited source.

## Data format
CSV fields: id, headword, ipa_uk, ukrainian_translation, part_of_speech, example_en, example_uk, level, category, source, verification_status, notes.

See data/schema.json and sources/references.md.

## Status
This is the initial project scaffold. It does not yet contain 5,000 vocabulary entries. Vocabulary will be added in reviewed batches; empty CSV files are templates, not completed word lists.

## Levels
- A0: useful foundation vocabulary; an editorial band, not an official CEFR level.
- A1–B2: assign levels using CEFR-aligned vocabulary references, prioritising Oxford 3000 where applicable.

## Workflow
1. Collect candidate headwords and assign a provisional level/category.
2. Verify UK IPA and core meanings against cited dictionary sources.
3. Write original, natural British-English examples and accurate Ukrainian translations.
4. Run python scripts/validate.py.
5. Manually review flagged records.
6. Generate the PDF after reviewed vocabulary batches are populated.

Structural validation does not replace editorial verification of IPA, meanings, CEFR levels or example quality.
