# A2 inventory reconciliation

## Reference and priority

The current Oxford 3000 online wordlist is the primary reference for CEFR assignment by headword and part of speech:

- https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000

The downloadable Oxford 3000 by CEFR level PDF is retained as a static reference snapshot. It is useful for cross-checking the inventory, but it is not allowed to override a conflicting current online assignment. The separate full Oxford 3000 PDF also differs from the by-CEFR PDF for some entries.

## Headword normalization

The current A2 CSV contains 993 records and 867 unique normalized headwords.

The headword comparison must preserve full multiword expressions and British English spelling. A simplified extracted list used during the initial comparison contained 864 items and required these corrections:

- Restore the complete expressions `according to` and `used to`; do not treat `according` or `used` as standalone headwords for these entries.
- Include the listed expressions `all right`, `any more` and `per cent`.
- Retain the British forms `organisation`, `organise`, `realise` and `recognise` in the learner-facing dictionary rather than replacing them with US spellings.

These normalization differences explain why a naïve exact-string comparison against a flattened list gives false missing/extra results.

## Part-of-speech corrections in this pass

Four missing A2 part-of-speech records were added after checking the Oxford entries and A2 labels:

| Headword | Added part of speech | Oxford entry |
|---|---|---|
| jump | verb | https://www.oxfordlearnersdictionaries.com/definition/english/jump_1 |
| ski | adjective | https://www.oxfordlearnersdictionaries.com/definition/english/ski_2 |
| surprise | verb | https://www.oxfordlearnersdictionaries.com/definition/english/surprise_2 |
| tie | noun | https://www.oxfordlearnersdictionaries.com/definition/english/tie_2 |

The A2 verb record for `lecture` was already present. A duplicate addition was removed after checking the existing records.

## Current online list versus static PDF

The following static-PDF differences are documented in the relevant CSV notes. The current online Oxford assignment takes precedence:

- `free`: current online list assigns the adverb to A2 and the adjective to A1; the static by-CEFR PDF places the adjective under A2.
- `ride`: current online list assigns the noun to A2 and the verb to A1; the static by-CEFR PDF places the verb under A2.
- `tidy`: current online list assigns the verb to A2; the adjective is listed at a higher level. The static by-CEFR PDF groups the adjective and verb under A2.

Other already documented Oxford PDF differences include `top` and `experiment`; see the notes in their CSV records and the repository README.

## Repeated headword and part-of-speech pairs

These repeated pairs are intentional separate senses, not duplicate rows:

- `lead | verb`: guiding/being in charge and being in front in a competition or ranking.
- `rest | noun`: the remaining part and a period of relaxation or sleep.
- `rock | noun`: stone and the music genre.

The validator's exact-entry duplicate rule and the editorial comparison distinguish these senses.

## Technical checks after the edits

The latest A2 file contains:

- 993 records
- 867 unique normalized headwords
- 0 duplicate IDs
- 0 malformed CSV rows
- 0 blank required fields
- 0 records with a level other than A2
- 0 invalid verification-status values
- 0 malformed IPA slash wrappers
- 0 non-HTTPS source fields
- 0 exact duplicate entries
- 0 repeated English example sentences
- 0 repeated Ukrainian example translations

These are structural and inventory checks. They do not independently prove that every translation, example pair, CEFR nuance or dictionary source on all 993 records has been re-opened and re-audited. The repository validator explicitly does not perform those editorial checks.
