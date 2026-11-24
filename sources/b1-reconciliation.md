# B1 inventory reconciliation — working record

## Current repository state

- `data/b1/words.csv` currently contains 20 records: `experiment` (verb), the first nine reconciled records, and a second batch of ten: `afford` (verb), `age` (verb), `aged` (adjective), `agent` (noun), `agreement` (noun), `ahead` (adverb), `aim` (noun and verb), `analyse` (verb) and `analysis` (noun). IDs are globally unique.
- A repository-wide ID audit found three collisions across A1/A2/B1. The A2 records `ski` adjective, `surprise` verb and `tie` noun were reassigned from `2031–2033` to `2035–2037`; the B1 `experiment` verb was reassigned from `2033` to `2038`. Existing A1 IDs `2031` (`be` auxiliary) and `2032` (`do` auxiliary) were retained. A2 `jump` verb keeps ID `2034`.
- The record is already documented as B1 according to the current Oxford 3000 online classification. Cambridge labels the cited verb sense B2; the existing note records this source discrepancy.
- The A1 and A2 files must be considered during B1 reconciliation because the same spelling can have a different CEFR level for another part of speech or sense.

## First verified B1 batch

The first nine additions were checked against the current Oxford 3000 online list for CEFR and part-of-speech assignment, then against the corresponding Oxford Advanced Learner’s Dictionary entry for UK IPA and meaning. The examples are original and have Ukrainian translations. The source entries are `access` noun (https://www.oxfordlearnersdictionaries.com/definition/english/access_1), `access` verb (https://www.oxfordlearnersdictionaries.com/definition/english/access_2), `achievement` (https://www.oxfordlearnersdictionaries.com/definition/english/achievement), `act` noun (https://www.oxfordlearnersdictionaries.com/definition/english/act_2), `addition` (https://www.oxfordlearnersdictionaries.com/definition/english/addition), `advanced` (https://www.oxfordlearnersdictionaries.com/definition/english/advanced), `admire` (https://www.oxfordlearnersdictionaries.com/definition/english/admire), `admit` (https://www.oxfordlearnersdictionaries.com/definition/english/admit) and `advise` (https://www.oxfordlearnersdictionaries.com/definition/english/advise). In particular, `act` noun is B1 while `act` verb is A2; `addition` is restricted to the mathematical sense identified as B1; and `access` noun and verb are separate B1 records. The B1 CSV now has 20 records in total. The second batch was checked against the current Oxford 3000 online list and individual Oxford entries. The `aged` record is specifically the sense meaning 'of the age of', pronounced /eɪdʒd/; the separate old-fashioned sense pronounced /ˈeɪdʒɪd/ is not included. `age` verb is B1 while `age` noun remains A1; both `aim` parts of speech are B1.

Second-batch Oxford dictionary entries: `afford` (https://www.oxfordlearnersdictionaries.com/definition/english/afford), `age` verb (https://www.oxfordlearnersdictionaries.com/definition/english/age_3), `aged` (https://www.oxfordlearnersdictionaries.com/definition/english/aged), `agent` (https://www.oxfordlearnersdictionaries.com/definition/english/agent), `agreement` (https://www.oxfordlearnersdictionaries.com/definition/english/agreement), `ahead` (https://www.oxfordlearnersdictionaries.com/definition/english/ahead), `aim` noun (https://www.oxfordlearnersdictionaries.com/definition/english/aim_2), `aim` verb (https://www.oxfordlearnersdictionaries.com/definition/english/aim_1), `analyse` (https://www.oxfordlearnersdictionaries.com/definition/english/analyse) and `analysis` (https://www.oxfordlearnersdictionaries.com/definition/english/analysis).

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

## Third verified B1 batch

The next alphabetical batch adds 11 records, continuing after `analysis`: `announce`, `announcement`, `annoy`, `annoyed`, `annoying`, `apart`, `apologise`, `application`, `appointment`, `appreciate` and `approximately`. Their B1 part-of-speech assignments were checked against the Oxford 3000 wordlist; the corresponding Oxford Advanced Learner’s Dictionary entries were checked for UK IPA and the selected meanings. Original example sentences and Ukrainian translations were written for this project.

Oxford's wordlist uses the spelling `apologize`; this dataset uses the standard British spelling `apologise`, supported by the Oxford entry's explicit British-English variant. The application entry is restricted to the B1 job/course application sense; the computing sense is B2 and is not included. The appointment entry illustrates the B1 arrangement-to-meet sense, not the separate B2 job/position sense.

## Fourth verified B1 batch

The following 11 records extend the alphabetical inventory from `arrest` through `authority`: `arrest` verb and noun, `arrival`, `assignment`, `assist`, `atmosphere`, `attach`, `attitude`, `attract`, `attraction` and `authority`. B1 part-of-speech assignments were checked against Oxford's wordlist; individual Oxford Advanced Learner’s Dictionary entries were checked for UK IPA and selected meanings. The examples and Ukrainian translations are original.

For words with several meanings, the records deliberately illustrate a specific learner-relevant sense: `arrest` as a police action and as the noun event; `atmosphere` as the mood of a place; `attach` in an email context; and `attraction` as a place worth visiting. The same spelling in separate parts of speech is represented by separate records where Oxford assigns both to B1.

## Fifth B1 batch: autumn–beauty

Thirteen records were added in alphabetical order: `autumn` (noun), `average` (verb), `award` (verb), `aware` (adjective), `backwards` (adverb), `bake` (verb), `balance` (noun and verb), `base` (noun, military-place sense), `basic` (adjective), `basis` (noun), `battery` (noun) and `beauty` (noun).

Individual Oxford Advanced Learner’s Dictionary entries were checked for UK IPA and selected meanings. The Oxford 3000 static list assigns the listed parts of speech to B1, except that the current online B1-filtered wordlist also surfaced `autumn` as B1 while the individual Oxford entry labels it Topics Time A1 and the static PDF lists it A1. Because the project gives priority to the current online wordlist but does not conceal the contradiction, `autumn` is included provisionally with `needs_review`; it must not be counted as verified until the discrepancy is resolved. The remaining 12 records have `verified` status based on their Oxford wordlist assignment and individual dictionary entry.

The `average` record is specifically the verb; its noun and adjective uses are A2. The `award` record is specifically the verb; its noun use is A2. The two `balance` records represent distinct parts of speech. The `base` noun record is restricted to the military-place sense, which Oxford marks B1; other senses may have different levels.

## Sixth B1 batch: belief–brave (candidate records pending dictionary verification)

Sixteen records were added in alphabetical order: `belief` (noun), `bell` (noun), `bend` (noun and verb), `benefit` (verb), `better` (noun), `bite` (noun and verb), `bomb` (noun and verb), `border` (noun), `bother` (verb), `branch` (noun), `brand` (noun and verb), and `brave` (adjective). The current Oxford online wordlist search results support the listed B1 part-of-speech assignments. In particular, Oxford lists `benefit` noun at A2 and verb at B1; `better` adjective at A1, adverb at A2 and noun at B1; `border` noun at B1 and verb at B2; and the listed noun/verb distinctions for `bend`, `bite`, `bomb` and `brand`. See the current Oxford list results and the official by-CEFR PDF: https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000 and https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf.

The records are deliberately marked `needs_review`, not `verified`: the B1 classification is supported, but the individual Oxford entries could not all be retrieved during this pass to confirm each UK IPA and selected sense. Some pronunciation checks were independently surfaced through Cambridge results (including `belief`, `benefit`, `bomb`, `branch` and `brave`), while Oxford individual entries were available in search results for `bend` noun and `benefit` verb. This does not replace a complete item-by-item check. `bee` was excluded because Oxford lists it at A1; `belt` was excluded because Oxford lists it at A2. The `better` example was corrected to the plural noun sense `betters` (people of higher rank/status), but that record also remains pending review.

## Seventh B1 batch: breathe–central (candidate records pending dictionary verification)

Twenty further entries were added: `breathe`, `breathing`, `bride`, `bubble`, `bury`, the adverb use of `by`, `calm` (adjective, noun and verb), `campaign` (noun and verb), `campus`, `candidate`, `cap`, `captain`, `careless`, `category`, `ceiling`, `celebration` and `central`. Oxford's current online wordlist search results support these B1 assignments and POS distinctions. The current online list labels `breath` noun B2, whereas the older static Oxford 3000 PDFs show it as B1; following the project's current-online-first rule, `breath` has not been added to B1 and should be considered for B2 reconciliation. Oxford's current online list also confirms `by` adverb B1 while its preposition use is A1; the A1 preposition record remains separate.

All 20 new records are marked `needs_review` because the individual dictionary entries were not all retrievable for full UK IPA and sense verification during this pass. The Oxford list supports CEFR/POS classification, but this alone is not enough to mark a record fully verified. References: current Oxford list https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000 and official Oxford 3000 by-CEFR PDF https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf.
