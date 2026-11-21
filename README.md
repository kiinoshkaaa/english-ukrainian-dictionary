# English–Ukrainian Dictionary (British English, Pre-A1–B2)

A carefully curated learner's dictionary for Ukrainian-speaking learners of British English.

## Editorial principles
- Target variety: contemporary Standard Southern British English (SSBE).
- Pronunciation: UK IPA, checked against authoritative learner's dictionaries.
- Translations and example translations: Ukrainian.
- CEFR levels are assigned from published vocabulary references, not from arbitrary word-count targets.
- Never label a record verified unless its pronunciation and meaning have been checked against a cited source.

## Vocabulary scope and level assignment
- **Pre-A1 (formerly called A0 in this project):** a clearly labelled foundation supplement. Pre-A1 is not one of the six formal CEFR levels, and this supplement must not be presented as an official CEFR vocabulary list.
- **A1–B2:** use the Oxford 3000 by CEFR level as the main core-word reference. Preserve the level assigned by Oxford; do not force equal-sized groups.
- **B2 extensions:** include additional B2 entries from the Oxford 5000 only when they are explicitly labelled B2. Do not import C1 entries into this dictionary.
- Use the English Vocabulary Profile as a secondary reference, especially where a word has different meanings or uses at different levels. Assign levels to the relevant sense/use, not blindly to the spelling alone.
- Count distinct headwords and lexical senses separately in project reports. A headword may occur at more than one level only when the source supports a different level for a distinct meaning or part of speech.
- Do not promise a fixed total such as 5,000 if the selected references do not support that total. Completeness and correct level assignment take priority over reaching a target.

## Primary references
- Oxford Learner's Dictionaries, Oxford 3000 and Oxford 5000: https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000
- Oxford 3000 by CEFR level: https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf
- English Vocabulary Profile: https://englishprofile.org/

## Data format
CSV fields: id, headword, ipa_uk, ukrainian_translation, part_of_speech, example_en, example_uk, level, category, source, verification_status, notes.

See data/schema.json and sources/references.md.

## Status
The repository is an in-progress project, not yet a complete dictionary. The current Pre-A1 file contains 100 entries; the A1, A2, B1 and B2 files are still empty templates. These counts describe the repository's current contents, not the number of words that exist at each level.

## Workflow
1. Build the candidate list from the level-specific reference lists.
2. Record the source level and distinguish headwords, senses, and parts of speech.
3. Verify UK IPA and core meanings against cited dictionary sources.
4. Write original, natural British-English examples and accurate Ukrainian translations.
5. Run python scripts/validate.py and manually review flagged records.
6. Generate the PDF only after the data and Unicode font rendering have been checked.

Structural validation does not replace editorial verification of IPA, meanings, CEFR levels or example quality.
