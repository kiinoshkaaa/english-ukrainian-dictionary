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
- Oxford 3000 and 5000: https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000
- Oxford 3000 by CEFR level (PDF): https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf
- Oxford's explanation of the CEFR: https://www.oxfordlearnersdictionaries.co.uk/about/wordlists/cefr
- English Vocabulary Profile: https://englishprofile.org/

## Data format
CSV fields: id, headword, ipa_uk, ukrainian_translation, part_of_speech, example_en, example_uk, level, category, source, verification_status, notes.

See data/schema.json and sources/references.md.

## Status
The A1 headword inventory contains 892 entries and has been reconciled against the A1 section of the Oxford 3000 by CEFR level PDF. This is a complete headword inventory for that reference list, not a fully verified learner's dictionary. After the latest editorial QA pass, 524 records are marked `verified`; 368 records remain `needs_review`. A `verified` label means the UK pronunciation and core meaning have been checked against an individual dictionary entry, with the Ukrainian gloss and original example pair editorially reviewed. CEFR placement follows the Oxford level list; where another dictionary assigns a different level, the difference is recorded in the entry notes. These pending records require dictionary-level checks of UK IPA, Ukrainian meanings, parts of speech, and example/translation quality. The A0 supplement has 3 entries. A2, B1 and B2 remain empty templates.

## Workflow
1. Build level-specific candidate inventories from the Oxford lists.
2. Preserve the source's CEFR assignment and part-of-speech/sense distinctions.
3. Verify UK IPA and core meanings against cited dictionary sources.
4. Write original, natural British-English examples and accurate Ukrainian translations.
5. Run scripts/validate.py and manually review flagged records.
6. Generate the PDF only after the vocabulary data and Unicode font rendering have been checked.

Structural validation does not replace editorial verification of IPA, translations, CEFR assignments or examples.
