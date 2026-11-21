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


## Fifth review batch — 2026-11-21

Recorded Cambridge Dictionary pronunciation-entry targets for eight further records: `be`, `beautiful`, `because`, `become`, `bed`, `bedroom`, `before`, and `behind`. This is a source-routing step, not a pronunciation verification: these records remain `needs_review` until the individual UK pronunciation entries are directly checked.

Cambridge Grammar confirms the adjective use of `beautiful`. A Cambridge English–German result confirms `become` is a verb and gives the core sense 'to come or grow to be', but its displayed /biˈkam/ is not a UK IPA form and was explicitly not used to validate the CSV transcription. For `behind`, the example demonstrates the preposition, while the record also lists an adverb; sense coverage needs review.


## Sixth editorial correction batch — 2026-11-21

- `beautiful`: corrected UK IPA from `/ˈbjuːtɪfl/` to `/ˈbjuːtɪfəl/`. Cambridge displays UK `/ˈbjuː.tɪ.fəl/`; the previous transcription omitted the unstressed vowel. The record remains `needs_review` because translation and example pair have not been fully audited.
- `before`: expanded POS to preposition, adverb, conjunction, consistent with the Cambridge English Preliminary vocabulary listing. Current example covers only the preposition.
- `behind`: retained preposition and adverb, supported by the Cambridge English Preliminary list; current example covers only the preposition.
- `begin` and `become`: verb POS and basic example sense cross-checked against the Cambridge English Preliminary vocabulary listing; other fields remain pending.

The Cambridge Preliminary list is used here only as corroboration for POS/sense coverage, not as proof of Oxford A1 level or as a pronunciation source. All five records remain `needs_review`.


## Seventh editorial correction batch — 2026-11-21

- `bicycle`: corrected broad UK IPA from `/ˈbaɪsɪkl/` to `/ˈbaɪsɪkəl/`, matching the Cambridge University Press pronunciation index entry. The source is an index, not a direct learner-dictionary entry; record remains `needs_review`.
- `blonde`: narrowed Ukrainian gloss from `білявий; білявка` to `білявий; світловолосий`, because Oxford's A1 listing gives the adjective entry and the CSV POS was adjective only. The example translation was improved to `У неї світле волосся.` This is an editorial translation correction, not an Oxford-sourced translation.

The Oxford 3000 inventory distinguishes A1 senses from higher-level POS: `best` is adjective A1 (adverb/noun A2), `better` adjective A1 (adverb A2), `between` preposition A1 (adverb A2), and `bill` noun A1 (verb B2). Their current POS entries were retained because they represent the A1 category only. The Cambridge Preliminary list corroborates several of these headwords' basic POS categories but is not the project's CEFR authority.


## Eighth pronunciation and POS batch — 2026-11-21

- `believe`: Cambridge UK IPA /bɪˈliːv/ confirmed and linked. Cambridge currently labels the main displayed sense A2, while Oxford 3000 includes the headword at A1. The Oxford level is retained; the discrepancy is flagged for sense-level review.
- `better`: Cambridge UK pronunciation corresponds to broad non-rhotic /ˈbetə/. Oxford's A1 POS is adjective; adverb is A2 and noun B1, so the CSV correctly keeps adjective only.
- `both`: Cambridge UK IPA /bəʊθ/ confirmed. Oxford lists determiner and pronoun at A1; the CSV includes both, and its example illustrates determiner use.

These are source-backed pronunciation/POS checks only. All three entries remain `needs_review` until Ukrainian translations and example pairs are fully checked.

## Ninth dictionary-level review batch — 2026-11-21

Three records were fully checked and promoted to `verified`:

- `box` — Cambridge confirms UK /bɒks/, the A1 container noun sense, and the current example illustrates that sense.
- `bread` — Cambridge confirms UK /bred/, the A1 uncountable food noun sense, and the current example illustrates that sense.
- `breakfast` — Cambridge confirms UK /ˈbrek.fəst/, the A1 noun sense, and the current example illustrates that sense.

For all three, the Ukrainian gloss and original example translation were editorially checked.

One additional correction was made without promoting the record: `bottle` UK IPA corrected from /ˈbɒtl/ to /ˈbɒtəl/, consistent with Cambridge UK /ˈbɒt.əl/. Cambridge labels the ordinary container sense A2, while Oxford is the project's A1 level authority; this difference is flagged and the record remains `needs_review`.

This batch adds three verified records. Other entries remain pending full review.

## Tenth dictionary-level review batch — 2026-11-21

Two further entries were fully checked and promoted to `verified`:

- `boy` — Cambridge confirms UK /bɔɪ/, the A1 countable noun meaning, and the record's example illustrates the core meaning.
- `brother` — Cambridge confirms UK pronunciation; the project's broad non-rhotic form /ˈbrʌðə/ represents the displayed UK /ˈbrʌð.ə(r)/. Cambridge confirms the A1 countable noun meaning, and the example illustrates it.

The Ukrainian glosses and original example translations were editorially checked. The records for `build` and `building` were not promoted: Cambridge labels the ordinary displayed senses A2, so their Oxford A1 placement needs sense-level review.

## Eleventh dictionary-level review batch — 2026-11-21

Five entries were checked and promoted to `verified`:

- `brown` — Cambridge confirms UK /braʊn/ and A1 noun/adjective colour senses. The example demonstrates the adjective.
- `busy` — Cambridge confirms UK /ˈbɪz.i/ and an A1 adjective sense for a place full of activity/people. The example was revised from a person being occupied (A2) to `This is a busy street.`, with Ukrainian `Це жвава вулиця.`
- `butter` — Cambridge confirms UK pronunciation (represented in broad non-rhotic form as /ˈbʌtə/) and the A1 uncountable noun sense.
- `buy` — Cambridge confirms UK /baɪ/ and the A1 verb sense of obtaining something by paying money.
- `can` — Cambridge confirms strong /kæn/ and weak /kən/ UK forms and A1 modal uses for ability, permission and requests. The IPA field now records both strong and weak forms.

For each entry, the example was checked against the selected sense and the Ukrainian gloss/example translation were editorially checked. The word `boyfriend` was not promoted: Cambridge labels its ordinary romantic-relationship noun sense A2, so the Oxford A1 placement needs sense-level reconciliation.

## Twelfth pronunciation review batch — 2026-11-21

Cambridge UK pronunciation pages were directly retrieved for four additional words and their broad UK transcriptions were checked:

- `car`: Cambridge /kɑː r/, represented in this project's broad non-rhotic style as /kɑː/.
- `centre`: Cambridge /ˈsen.tə r/, represented as /ˈsentə/.
- `carrot`: Cambridge /ˈkær.ət/, represented as /ˈkærət/.
- `chair`: Cambridge /tʃeə r/, represented as /tʃeə/.

These are pronunciation-only checks. Cambridge dictionary definition pages returned HTTP 403 in this review, so meanings, parts of speech, Ukrainian translations, and example pairs were not independently verified. None of these four records was promoted to `verified`. Do not count this batch as completed full-entry verification.

## Thirteenth dictionary-level review batch — 2026-11-21

- `cheese` was fully checked and promoted to `verified`: Cambridge confirms UK /tʃiːz/, the A1 noun meaning, and a food-related example. The CSV example `Would you like some cheese?` matches that sense; the Ukrainian gloss and translation were editorially checked.
- `cat` was checked against Cambridge: UK /kæt/, A1 countable noun pet sense. Its existing CSV status was already `verified`, so no status change was needed.
- `card` was not promoted. The current example `Can I pay by card?` illustrates a Cambridge B1 payment-card sense, not a clearly supported A1 sense. The Oxford headword-level A1 listing does not by itself validate that specific sense.
- `chicken` was not promoted: Cambridge labels the ordinary bird/meat noun sense A2, whereas the project uses Oxford for headword-level CEFR placement. Flag for sense-level reconciliation.

## Fourteenth dictionary-level review batch — 2026-11-21

Three entries were fully checked and promoted to `verified`:

- `cake` — Cambridge confirms UK /keɪk/ and the A1 food noun sense (countable and uncountable). The existing example demonstrates the food sense.
- `camera` — Cambridge confirms UK /ˈkæm.rə/ and the A1 countable noun meaning. The project's broad transcription /ˈkæmərə/ is retained as a broad representation.
- `cheap` — Cambridge confirms UK /tʃiːp/ and the A1 adjective sense of costing little money. The existing example demonstrates the low-price meaning.

For all three, the Ukrainian gloss and example translation were editorially checked. `call` was not promoted: Cambridge marks the phone-call noun A2 and the naming verb B1; the current example uses the phone-call verb sense, so the Oxford A1 headword placement requires sense-specific reconciliation.
