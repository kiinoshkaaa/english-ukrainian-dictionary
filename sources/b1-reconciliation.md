# B1 inventory reconciliation — working record

## Current repository state

- `data/b1/words.csv` currently contains 10 records: `experiment` (verb) plus nine newly reconciled B1 records: `access` (noun and verb), `achievement` (noun), `act` (noun), `addition` (mathematical noun sense), `advanced` (adjective), `admire` (verb), `admit` (verb) and `advise` (verb). IDs are globally unique.
- A repository-wide ID audit found three collisions across A1/A2/B1. The A2 records `ski` adjective, `surprise` verb and `tie` noun were reassigned from `2031–2033` to `2035–2037`; the B1 `experiment` verb was reassigned from `2033` to `2038`. Existing A1 IDs `2031` (`be` auxiliary) and `2032` (`do` auxiliary) were retained. A2 `jump` verb keeps ID `2034`.
- The record is already documented as B1 according to the current Oxford 3000 online classification. Cambridge labels the cited verb sense B2; the existing note records this source discrepancy.
- The A1 and A2 files must be considered during B1 reconciliation because the same spelling can have a different CEFR level for another part of speech or sense.

## First verified B1 batch

The first nine additions were checked against the current Oxford 3000 online list for CEFR and part-of-speech assignment, then against the corresponding Oxford Advanced Learner’s Dictionary entry for UK IPA and meaning. The examples are original and have Ukrainian translations. The source entries are `access` noun (https://www.oxfordlearnersdictionaries.com/definition/english/access_1), `access` verb (https://www.oxfordlearnersdictionaries.com/definition/english/access_2), `achievement` (https://www.oxfordlearnersdictionaries.com/definition/english/achievement), `act` noun (https://www.oxfordlearnersdictionaries.com/definition/english/act_2), `addition` (https://www.oxfordlearnersdictionaries.com/definition/english/addition), `advanced` (https://www.oxfordlearnersdictionaries.com/definition/english/advanced), `admire` (https://www.oxfordlearnersdictionaries.com/definition/english/admire), `admit` (https://www.oxfordlearnersdictionaries.com/definition/english/admit) and `advise` (https://www.oxfordlearnersdictionaries.com/definition/english/advise). In particular, `act` noun is B1 while `act` verb is A2; `addition` is restricted to the mathematical sense identified as B1; and `access` noun and verb are separate B1 records. The B1 CSV now has 10 records in total, including the pre-existing `experiment` verb.

## Provisional candidate inventory

A community-maintained GitHub extraction of Oxford 3000 CEFR data was inspected as a discovery aid:

https://github.com/Kolia951/The_Oxford_3000_CEFR/blob/main/package.txt

Its B1 section contains 806 distinct headword strings. This is **not accepted as the authoritative B1 count or final inventory**. It is a candidate list only; it must be checked against the current Oxford Learner's Dictionaries B1-filtered Oxford 3000 list and the official Oxford 3000 PDF before records are added or moved.

Preliminary exact-headword overlaps between that candidate list and the current repository:

- 52 candidate headwords also occur in the A1 file.
- 67 candidate headwords also occur in the A2 file.

These overlaps are not automatically errors. Oxford assigns levels by part of speech and sometimes by individual sense. Each overlap must be resolved at the headword + part-of-speech + sense level. Do not copy a whole headword into B1 solely because it appears in the candidate list.

## Authoritative references

1. Current Oxford 3000/5000 online wordlist, with B1 filter and part-of-speech labels:
   https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000
2. Oxford 3000 full PDF:
   https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000.pdf
3. Oxford 3000 by CEFR level PDF:
   https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf

Oxford explains that the Oxford 3000 covers A1–B2 and that its online wordlist shows CEFR level, part of speech and British pronunciation. The online wordlist is the primary source for current level assignment; downloadable PDFs are retained as static comparison snapshots.

## Editorial workflow

1. Extract the official B1 entries with their part-of-speech and sense distinctions.
2. Normalize British spelling and multiword expressions without collapsing distinct expressions.
3. Compare B1 candidates with A1 and A2 at part-of-speech/sense level.
4. Check each accepted entry's UK IPA and core meaning in an individual authoritative dictionary entry.
5. Write an original, natural British-English example and an accurate Ukrainian translation.
6. Record source disagreements explicitly. Do not mark a record verified merely because a headword appears in a CEFR list.
7. Run structural validation and inspect all warnings before considering B1 complete.

## Scope warning

The 806 candidate headwords are a discovery count from a third-party extraction, not a verified Oxford B1 total. No claim of B1 completeness should be made until the current official list has been reconciled by headword, part of speech and sense.
