# A1 editorial quality audit

Date: 2026-11-21

## Scope and reference

- Target: contemporary mainstream British English pronunciation, represented with broad UK IPA.
- CEFR/headword reference: Oxford University Press, *The Oxford 3000 by CEFR level*, A1 section.
- The Oxford reference supports headword inclusion, level and listed parts of speech. It does not verify UK IPA, Ukrainian translations, or the project's original examples.
- Pronunciation references: individual Cambridge Dictionary pronunciation entries where a direct entry URL is present. Oxford pronunciation guidance describes its British model as mainstream/unmarked RP and explains broad phonemic transcription conventions.

## Inventory checks

- A1 records: 892
- Headwords: 892 unique
- IDs: 892 unique
- Headword inventory: reconciled to the 892 headwords in the Oxford A1 section
- Missing/extra headwords in the reconciliation: 0 / 0
- Folder/level mismatches: 0
- Blank required fields: none found in the structural pass

## Corrections made in this pass

- Corrected part-of-speech labels where the Oxford A1 list clearly did not support the previous extra labels: `above`, `after`, `game`, `garden`, `good`, `high`, `his`, `hope`, `no`, `please`, `point`, `rule`, `start`, `swim`, `talk`, `type`, `will`, and `wrong`.
- Restored listed noun/adjective uses for `goodbye`, `hello`, `one`, `opposite`, and `welcome`.
- Corrected the provisional UK IPA for `hello` from `/heˈləʊ/` to `/həˈləʊ/`; it remains pending re-verification.
- Removed optional syllable-divider dots from 18 Cambridge-style IPA strings to make the broad transcription format consistent with the project's Oxford-style notation.
- Downgraded 10 entries that cited a Cambridge-published index PDF rather than an individually inspected dictionary pronunciation entry.
- Rewrote Oxford-PDF notes so they no longer imply that the CEFR list proves pronunciation, translation or example quality.

## Verification status after this pass

- `verified`: 20
- `needs_review`: 872
- `draft`: 0

A record marked `needs_review` is not certified as error-free. The remaining 872 entries still need individual dictionary-level review of pronunciation, meanings, parts of speech, and example/translation pairs. A structural pass and a correct headword inventory are not a substitute for that work.

## Known limitation

This pass does not claim that all 892 IPA transcriptions, Ukrainian translations, examples, or part-of-speech labels have been individually checked against dictionary entries. Do not publish the A1 section as fully proofread until the 872 pending records have been reviewed and their statuses updated with direct evidence.


## Follow-up dictionary-level review — 2026-11-21

First verified batch: **2 entries**.

- `about` — UK pronunciation, core A1 senses and part-of-speech use checked against Cambridge Dictionary; example and Ukrainian translation editorially checked.
- `above` — UK IPA checked against Cambridge Dictionary pronunciation; core meanings and part-of-speech use checked against learner-dictionary evidence; example and Ukrainian translation editorially checked.

Both records are now marked `verified` in `data/a1/words.csv`. The remaining entries have not been promoted based on this batch and remain subject to individual review. This is a continuing audit, not a claim that the A1 list is fully verified.


## Pronunciation-source batch — 2026-11-21

Cambridge Dictionary UK pronunciation pages were located and recorded for eight further entries: `action`, `actor`, `actress`, `add`, `address`, `adult`, `advice`, and `afraid`. Their IPA values were retained because the available Cambridge results were consistent with the existing broad UK transcriptions. Their records remain `needs_review`: this batch did not independently verify every meaning, Ukrainian translation, part-of-speech label, and example.

**CEFR note:** Cambridge's entry for `advice` labels its displayed sense A2, while the project follows the Oxford 3000 by CEFR list, which includes `advice` at A1. This is recorded as a source-label difference to investigate, not silently changed. The Oxford list remains the project's level authority unless the project scope is deliberately revised.

The batch does not constitute full proofreading of these entries.


## Second pronunciation-source batch — 2026-11-21

Cambridge UK pronunciation entries were checked and linked for seven further headwords: `across`, `activity`, `after`, `afternoon`, `age`, `air`, and `always`. The broad IPA already in the CSV was retained where consistent with Cambridge's UK rendering. For `across`, Cambridge grammar also confirms preposition and adverb uses. For `always`, Cambridge confirms the core A1 adverb sense. All seven records remain `needs_review` because full verification of Ukrainian translations and example pairs, plus any remaining lexical details, has not been completed.


## Third pronunciation and usage-source batch — 2026-11-21

Cambridge Dictionary sources were recorded for 15 entries across two additional batches:

- `animal`, `answer`, `another`, `anyone`, `apartment`, `area`, `around`;
- `anything`, `April`, `arm`, `ask`, `at`, `aunt`, `autumn`, `away`.

The UK IPA was checked where a Cambridge pronunciation result was available. The record for `at` was expanded to show both strong /æt/ and weak /ət/ forms. These records remain `needs_review` because the whole record (especially the Ukrainian translation and example pair) has not been fully verified.

### CEFR and usage flags

Cambridge's displayed senses for `another`, `anyone`, `apartment`, `around`, `ask`, and `aunt` include levels A2 or B1, whereas the project's Oxford 3000 source places the headwords in A1. The project continues to use Oxford as the level authority; these cross-dictionary differences are flagged for sense-specific review. Cambridge also notes that `apartment` is mainly US for the ordinary residential meaning and that UK usage usually prefers `flat` (though `apartment` also occurs in UK business usage). This may require improving the Ukrainian gloss/example to make the intended British usage clear.


## Fourth pronunciation-source batch — 2026-11-21

Cambridge UK pronunciation references were added for eight further A1 records: `baby`, `back`, `bad`, `bag`, `ball`, `banana`, `bank`, and `bath`. Existing broad IPA forms were consistent with the retrieved Cambridge UK forms. These records remain `needs_review`; this batch did not certify all senses, POS labels, Ukrainian translations, and examples.

Specific editorial flags: `back` currently combines a noun/adverb POS list while its example and gloss demonstrate only the noun; `bad` has a noun label that needs validation for the intended A1 sense; `bank` currently narrows the translation to a financial institution and may need an explicit sense scope; `bath` uses the British collocation `have a bath` in its example.
