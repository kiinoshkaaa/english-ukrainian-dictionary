# B1 inventory reconciliation — working record

## Current repository state

- Current audited repository state after the R batch: `data/b1/words.csv` contains 642 records (54 `verified`, 588 `needs_review`); all 2,531 IDs are globally unique across the five level files. The historical batch notes below document the sequence of additions and corrections; older counts in those notes describe the repository at the time each batch was recorded.
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

The records are deliberately marked `needs_review`, not `verified`: the B1 classification is supported, but the individual Oxford entries could not all be retrieved during this pass to confirm each UK IPA and selected sense. Some pronunciation checks were independently surfaced through Cambridge results (including `belief`, `benefit`, `bomb`, `branch` and `brave`), while Oxford individual entries were available in search results for `bend` noun and `benefit` verb. This does not replace a complete item-by-item check. At the time of this batch, `bee` and `belt` were excluded based on earlier dictionary/topic level lookups (A1 and A2 respectively); a later inspection of the current B1-filtered online wordlist showed both as B1, so this earlier exclusion has been superseded and the conflict is documented in the later reconciliation entry. The `better` example was corrected to the plural noun sense `betters` (people of higher rank/status), but that record also remains pending review.

## Seventh B1 batch: breathe–central (candidate records pending dictionary verification)

Twenty further entries were added: `breathe`, `breathing`, `bride`, `bubble`, `bury`, the adverb use of `by`, `calm` (adjective, noun and verb), `campaign` (noun and verb), `campus`, `candidate`, `cap`, `captain`, `careless`, `category`, `ceiling`, `celebration` and `central`. Oxford's current online wordlist search results support these B1 assignments and POS distinctions. The current online list labels `breath` noun B2, whereas the older static Oxford 3000 PDFs show it as B1; following the project's current-online-first rule, `breath` has not been added to B1 and should be considered for B2 reconciliation. Oxford's current online list also confirms `by` adverb B1 while its preposition use is A1; the A1 preposition record remains separate.

All 20 new records are marked `needs_review` because the individual dictionary entries were not all retrievable for full UK IPA and sense verification during this pass. The Oxford list supports CEFR/POS classification, but this alone is not enough to mark a record fully verified. References: current Oxford list https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000 and official Oxford 3000 by-CEFR PDF https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf.

## Eighth B1 batch: centre–climb (candidate records pending dictionary verification)

Twenty-four further records were added: `centre` verb; `ceremony`; `chain` noun; `challenge` noun; `champion`; `channel`; `chapter`; `charge` noun and verb; `cheap` adverb; `cheat` noun and verb; `cheerful`; `chemical` adjective and noun; `chest`; `childhood`; `claim` noun and verb; `clear` verb; `click` noun and verb; `client`; and `climb` noun. The current Oxford online list assigns these forms to B1. Related A1/A2 forms are kept separate: `centre` noun A1, `cheap` adjective A1, `clear` adjective A2 and `climb` verb A1. Oxford distinguishes `chain` noun B1/verb B2 and `challenge` noun B1/verb B2.

All 24 records remain `needs_review` pending individual dictionary checks of UK IPA and selected senses. References: current Oxford list https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000 and official by-CEFR list https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf.

## Ninth B1 batch: clue–confirm (candidate records pending dictionary verification)

Twenty-two records were added alphabetically from `clue` through `confirm`: `clue`, `coach` verb, `coal`, `coin`, `collection`, `coloured`, `combine`, `comment` verb, `commercial` adjective and noun, `commit`, `communication`, `comparison`, `competitor`, `competitive`, `complaint`, `complex`, `concentrate`, `conclude`, `conclusion`, `confident` and `confirm`. Oxford's current online B1 wordlist and the official by-CEFR PDF support the B1 assignments. Existing A2 uses remain distinct: `coach` noun and `comment` noun are A2; the newly added records are the verb uses. All records remain `needs_review` until the individual dictionary entry, UK IPA, selected meaning and example pair are checked.

References: https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000 and https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf.

## Tenth B1 batch: confuse–cool (candidate records pending dictionary verification)

Fourteen records were added: `confuse` verb, `confused` adjective, `connection`, `consequence`, `consist`, `consumer`, `contact` noun and verb, `content` noun, `contrast` noun and verb, `convenient`, `convince` and `cool` verb. The current Oxford online wordlist supports these B1 assignments and part-of-speech distinctions. `confusing` is B2, `content` adjective is C1, and `cool` adjective is A1; those uses are not included here.

A correction was made to the previous batch: `comparison` noun was removed from B1 because the current Oxford online list classifies it as A1, despite the older static by-CEFR PDF placing it at B1. This is an example of why the current online list takes precedence. All 14 new records remain `needs_review` pending individual UK IPA and sense verification. Source: https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000.

## Eleventh B1 batch: costume–damage (candidate records pending dictionary verification)

Twenty-one records were added: `costume`, `cottage`, `cotton`, `count` noun, `countryside`, `court`, `cover` noun, `covered`, `cream` adjective, `criminal` adjective, `cruel`, `cultural`, `currency`, `current` adjective, `currently`, `curtain`, `custom`, `cut` noun, `daily` adverb, and `damage` noun and verb. Oxford's current online wordlist and official B1 list support these part-of-speech/level assignments. Related lower-level uses remain separate: `count` verb A2, `cover` verb A2, `cream` noun A1, `criminal` noun A2, `cut` verb A1 and `daily` adjective A2. All new records remain `needs_review` pending individual dictionary verification.

References: https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000 and https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf.

## Twelfth B1 batch: deal–dislike (candidate records pending dictionary verification)

Twenty-six records were added: `deal` noun, `decade`, `deep` adverb, `define`, `definite`, `definition`, `deliver`, `departure`, `despite`, `destination`, `determine`, `determined`, `development`, `diagram`, `diamond`, `difficulty`, `direct` verb and adverb, `directly`, `dirt`, `disadvantage`, `disappointed`, `disappointing`, `discount` noun, and `dislike` noun and verb. Oxford's official by-CEFR list supports these entries. Distinct lower-level forms remain separate: `deal` verb A2, `deep` adjective A2 and `direct` adjective A2. `discount` verb is B2 and is not included.

All 26 records remain `needs_review` pending individual UK IPA and selected-sense verification. References: https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000 and https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf.

## Thirteenth B1 batch: divide–duty (candidate records pending dictionary verification)

Thirteen records were added: `divide` verb, `documentary`, `donate`, `double` adverb, `doubt` noun and verb, `dressed`, `drop` noun, `drum`, `drunk`, `due`, `dust` and `duty`. The current Oxford online wordlist supports the B1 assignments and distinctions: `divide` verb B1 (noun B2), `double` adverb B1 (other listed grammatical uses A2), and `drop` noun B1 (verb A2). `district` was not added because the current online list classifies it as B2, despite older American-list evidence that differs. All 13 records remain `needs_review` pending individual dictionary checks.

References: https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000 and https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf.

## Fourteenth B1 batch: eastern–expedition (candidate records pending dictionary verification)

Forty-six records were added from the current Oxford B1-filtered list: `eastern` adjective, `earthquake` noun, `ease` noun, `economic` adjective, `economy` noun, `edge` noun, `editor` noun, `educate` verb, `educated` adjective, `educational` adjective, `effective` adjective, `effectively` adverb, `effort` noun, `election` noun, `element` noun, `embarrassed` adjective, `embarrassing` adjective, `emergency` noun, `emotion` noun, `employment` noun, `encourage` verb, `enemy` noun, `engaged` adjective, `engineering` noun, `entertain` verb, `entertainment` noun, `entrance` noun, `entry` noun, `environmental` adjective, `episode` noun, `equal` adjective and verb, `equally` adverb, `escape` noun and verb, `essential` adjective, `eventually` adverb, `examine` verb, `except` conjunction, `exchange` noun and verb, `excitement` noun, `exhibition` noun, `expand` verb, `expected` adjective, and `expedition` noun.

The source list also confirms distinctions that should not be collapsed: `economics` noun is B2; `education` noun is A2; `efficient` adjective is B2; `engage` verb is B2 while `engaged` adjective is B1; `environment` noun is A2 while `environmental` adjective is B1; and `experience` noun is not included here because it requires a separate check of its exact Oxford level and POS listing. `eager` adjective is C1 and is excluded. All 46 new records remain `needs_review`: the current Oxford list supports the B1/POS assignments, but each dictionary entry's UK IPA, selected sense and example still need individual editorial checking.

Primary reference: current Oxford 3000 B1-filtered list https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000. Oxford explains that its 3000 core entries are aligned to CEFR and that the wordlist can be filtered by level and part of speech: https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000.

## Fifteenth B1 batch: experience–extra (candidate records pending dictionary verification)

Nine additional records complete the E section visible in the current Oxford B1-filtered wordlist: `experience` verb, `experienced` adjective, `explode` verb, `explore` verb, `explosion` noun, `export` noun and verb, and `extra` adverb and noun. `experiment` verb was already present in the earlier B1 inventory; `experiment` noun is A2. Other nearby forms excluded by the current list include `expose` verb (B2), `express` verb (A2), `expression` noun (A2), `extend` verb (B2), `extent` noun (B2), and `external` adjective (B2). All nine new records remain `needs_review` pending individual UK IPA, meaning and example verification.

Primary reference: current Oxford B1-filtered list https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000. Oxford's list shows the CEFR level and part of speech separately for each entry.

## Sixteenth B1 batch: fairly–forthcoming (candidate records pending dictionary verification)

Thirty-one records were added from the current Oxford B1-filtered list: `fairly` adverb, `familiar` adjective, `fancy` adjective and verb, `far` adjective, `fascinating` adjective, `fashionable` adjective, `fasten` verb, `favour` noun, `fear` verb, `feature` verb, `fence` noun, `fighting` noun, `file` noun, `financial` adjective, `fire` verb, `fitness` noun, `fixed` adjective, `flag` noun, `flood` noun and verb, `flow` noun and verb, `fold` verb, `folk` adjective and noun, `following` noun, `force` noun and verb, `forever` adverb, and `forthcoming` adjective. Oxford's current list distinguishes these B1 grammatical uses from lower-level uses such as `fair` adjective A2, `far` adverb A1, `fear` noun A2, `feature` noun A2, `fire` noun A1, and `following` adjective A2.

All 31 new records remain `needs_review`: the CEFR/POS assignments are supported by the current Oxford B1-filtered wordlist, but individual UK IPA, selected meanings, natural examples and translations still require editorial review. Primary source: https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000.

## Seventeenth B1 batch: garage–guilty (candidate records pending dictionary verification)

Twenty-four records were added from the current Oxford B1-filtered list: `garage` noun, `gather` verb, `generally` adverb, `generation` noun, `generous` adjective, `gentle` adjective, `gentleman` noun, `ghost` noun, `giant` adjective and noun, `glad` adjective, `global` adjective, `glove` noun, `go` noun, `goods` noun, `grade` noun, `graduate` noun and verb, `grain` noun, `grateful` adjective, `growth` noun, `guard` noun and verb, and `guilty` adjective. The `go` noun record is separate from `go` verb A1; other B1 grammatical uses are recorded separately where Oxford lists them. All 24 records remain `needs_review` pending individual dictionary verification.

Primary source: current Oxford B1-filtered wordlist https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000. The list assigns a CEFR level to each part-of-speech entry, so the B1 classification must be checked at the POS level rather than by headword alone.

## Eighteenth B1 batch: hand–hurry (candidate records pending dictionary verification)

Twenty-two records were added from the current Oxford B1-filtered list: `hand` verb, `hang` verb, `happiness` noun, `hardly` adverb, `head` verb, `headline` noun, `heating` noun, `heavily` adverb, `helicopter` noun, `highlight` noun and verb, `highly` adverb, `hire` verb, `historic` adjective, `historical` adjective, `honest` adjective, `horrible` adjective, `horror` noun, `host` noun, `hunt` verb, and `hurry` noun and verb. Lower-level headword uses remain distinct (for example, `hand` and `head` nouns are A1). All new records remain `needs_review` pending individual UK IPA, meaning and example verification.

Primary source: current Oxford B1-filtered wordlist https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000.

## Nineteenth B1 batch: identity–IT (candidate records pending dictionary verification)

Thirty-four records were added from the current Oxford B1-filtered list: `identity` noun, `ignore` verb, `immediate` adjective, `immigrant` noun, `impact` noun and verb, `import` noun and verb, `importance` noun, `impression` noun, `impressive` adjective, `improvement` noun, `incredibly` adverb, `indeed` adverb, `indicate` verb, `indirect` adjective, `indoor` adjective, `indoors` adverb, `influence` noun and verb, `ingredient` noun, `injure` verb, `injured` adjective, `innocent` adjective, `intelligence` noun, `intend` verb, `intention` noun, `invest` verb, `investigate` verb, `involved` adjective, `iron` noun and verb, `issue` noun, and `IT` noun. The `IT` noun is separate from the A1 pronoun `it`.

The existing A2 record for `ill` adjective was not duplicated into B1: the current search snippets produced conflicting level signals for this entry, so it requires a dedicated Oxford-entry reconciliation before any level change. All 34 new records remain `needs_review` pending individual UK IPA, meaning and example verification.

Primary source: current Oxford B1-filtered wordlist https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000.

## Twentieth B1 batch: judge–kiss (candidate records pending dictionary verification)

Eleven records were added from the current Oxford B1-filtered list: `judge` noun and verb, `keen` adjective, `key` verb, `keyboard` noun, `kick` noun and verb, `killing` noun, `kind` adjective, and `kiss` noun and verb. The noun `key` and noun `kind` remain A1 in the existing A1 inventory; these new records represent separate B1 grammatical uses. All eleven records remain `needs_review` pending individual dictionary verification.

Primary source: current Oxford B1-filtered wordlist https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000.


## Level-conflict correction: bee and belt

A later check of the current Oxford B1-filtered online list (https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000) shows `bee` noun and `belt` noun as B1. This conflicts with the earlier dictionary/topic-level classification used in the sixth-batch note (bee A1 and belt A2). The B1 records have now been added provisionally as `needs_review` rather than silently choosing one source. The existing A2 `belt` record is retained pending a direct comparison of the current Oxford wordlist item and the individual Oxford dictionary entry. No claim is made that the conflict has been resolved.

## Twenty-first B1 batch: latest–luxury (candidate records pending individual dictionary verification)

Thirty-five records were added for the L section: `latest` adjective, `lay` verb, `layer` noun, `lead` noun, `leading` adjective, `leaf` noun, `leather` noun, `label` verb, `laboratory` noun, `lack` verb, `legal` adjective, `leisure` noun, `length` noun, `level` adjective, `lie` noun and verb, `like` noun, `limit` noun and verb, `lip` noun, `liquid` adjective and noun, `literature` noun, `live` adjective and adverb, `living` adjective and noun, `local` noun, `locate` verb, `located` adjective, `location` noun, `lonely` adjective, `loss` noun, and `luxury` adjective and noun.

The current Oxford online wordlist is the CEFR/POS basis for these candidates. Lower-level or other-level forms are kept separate: `label` noun A2; `lack` noun B2; `level` noun A2 and verb B2; `lie` verb A1 for the horizontal-position sense versus B1 for the untruth sense; `like` verb/preposition A1; `local` adjective A1; and `live` verb A1. `labour` noun is B2 and is not included. The list also distinguishes `latest` adjective B1 from `latest` noun B2, and `luxury` adjective/noun B1.

All 35 entries remain `needs_review`. The Oxford wordlist supports the provisional CEFR/POS assignment, but the UK IPA, exact dictionary sense, Ukrainian gloss and example pair have not yet been individually audited. The initial `liquid` adjective and `live` adjective examples were revised after editorial review; all entries remain subject to individual verification.

Primary reference: current Oxford 3000 B1-filtered wordlist, https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000. Searchable list result: Oxford's L entries and grammatical classifications, including the distinctions above. General Oxford 3000 reference: https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000.

## Twenty-second B1 batch: mad–mystery (candidate records pending individual dictionary verification)

Twenty-nine records were added for the M section: `mad` adjective, `magic` noun, `magical` adjective, `mall` noun, `mainstream` adjective, `management` noun, `market` verb, `marketing` noun, `marriage` noun, `meanwhile` adverb, `measure` noun and verb, `medium` adjective, `mental` adjective, `mention` noun, `mess` noun, `mild` adjective, `mine` noun, `mix` noun and verb, `mixture` noun, `mood` noun, `move` noun, `mud` noun, `murder` noun and verb, `muscle` noun, `musical` noun, and `mystery` noun.

The current Oxford 3000 online list assigns these B1 levels by part of speech. Important exclusions and distinctions: `magic` adjective is A1 while the noun is B1; `manager` noun is A2 while `management` noun is B1; `market` noun is A1 while the verb is B1; `marketplace` is C1 and is excluded; `mention` verb is A2 while the noun is B1; `medium` adjective is B1 while the noun is B2; `mine` pronoun is A2 while the noun is B1; `move` verb is A1 while the noun is B1; `musical` adjective is A2 while the noun is B1. The Oxford list also places `mainstream` noun at C1 and only the adjective at B1.

All 29 records remain `needs_review`. The online Oxford list supports the provisional CEFR/POS classifications; individual dictionary checks of UK IPA, exact senses and examples are still required. In particular, pronunciation and sense distinctions for `mad`, `medium`, `mine`, and `musical` must be retained during final review.

Primary reference: current Oxford 3000 B1-filtered wordlist, https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000. The same source lists adjacent A1/A2/B2/C1 entries, allowing POS-level distinctions to be checked.

## Twenty-third B1 batch: nail–nuclear (candidate records pending current-list reconciliation and individual dictionary verification)

Twenty records were added provisionally for the N section: `nail` noun, `narrative` noun and adjective, `nation` noun, `native` adjective and noun, `naturally` adverb, `necessarily` adverb, `need` modal verb, `needle` noun, `neighbourhood` noun, `neither` adverb, `net` noun, `next` noun, `nor` conjunction/adverb, `normal` noun, `northern` adjective, `note` verb, `now` conjunction, and `nuclear` adjective.

The primary evidence used for this provisional batch is the published Oxford 3000 PDF snapshot, which explicitly lists the headwords and grammatical categories at B1. The project normally prioritizes the current online Oxford list; this PDF snapshot is not treated as proof that every assignment remains unchanged online. Accordingly, all 20 records remain `needs_review` until current online level/POS status and each individual dictionary entry have been checked.

The list distinguishes several lower-level uses already present in the repository: `need` lexical verb A1 and noun A2 versus modal verb B1; `neither` determiner/pronoun A2 versus adverb B1; `next` adjective/adverb A1 versus noun B1; `normal` adjective A2 versus noun B1; and `note` noun A1 versus verb B1. `negative` adjective is A1 and noun B2; `network` noun is A2; `nervous` adjective is A2; `notice` noun/verb is A2; `novel` noun is A2; `numerous` adjective is B2; these are not added to B1. The static Oxford list also shows `native` adjective/noun B1, `naturally` adverb B1, `necessarily` adverb B1, `neighbourhood` noun B1, `nuclear` adjective B1, and `narrative` noun/adjective B1.

The B1-filtered current online Oxford page could not be independently opened during this pass; the PDF snapshot and the individual nuclear entry are the available supporting references. Do not interpret this batch as a completed level reconciliation. All IPA, Ukrainian glosses and original examples are provisional pending individual dictionary review.

References: Oxford 3000 PDF snapshot https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000.pdf (N entries); Oxford's current Oxford 3000/5000 overview https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000; Oxford nuclear entry https://www.oxfordlearnersdictionaries.com/us/definition/english/nuclear.

## Twenty-fourth B1 batch: obvious–outdoors (candidate records pending individual dictionary verification)

Seventeen records were added for the O section: `obvious` adjective, `obviously` adverb, `occasion` noun, `occur` verb, `odd` adjective, `official` adjective, `old-fashioned` adjective, `once` conjunction, `operation` noun, `organized` adjective, `organizer` noun, `original` noun, `originally` adverb, `ought` modal verb, `ours` pronoun, `outdoor` adjective, and `outdoors` adverb.

The current Oxford B1-filtered list directly supports `obvious`, `obviously`, `occasion`, `occur`, `odd`, and `official` adjective as B1. The Oxford list results also distinguish `once` conjunction B1 from adverb A1; `official` noun is B2; `ours` pronoun B1 from `ourselves` pronoun A2; and `outdoor` adjective plus `outdoors` adverb B1. The published Oxford 3000 list snapshot supports `old-fashioned` adjective, `operation` noun, `organized` adjective, `organizer` noun, `original` noun, `originally` adverb and `ought` modal verb at B1. These snapshot-based entries remain provisional until checked against the current online filter.

Nearby exclusions are deliberately not added: `offer` noun/verb A2, `officer` noun A2, `oil` noun A2, `opportunity` noun A2, `option` noun A2, `ordinary` adjective A2, `organisation` noun A2, `organise` verb A2, `outside` adjective/noun/preposition A2 and adverb A1, `oven` noun A2, `ourselves` pronoun A2, `operator` noun B2, and `offshore` adjective C1.

All 17 new records remain `needs_review`. The individual UK IPA, precise sense, Ukrainian translation and original example pair have not yet completed independent dictionary review. The headwords `organized` and `organizer` follow the spelling used in the Oxford list; British variants `organised` and `organiser` should be considered during the final editorial normalization.

Primary references: current Oxford B1-filtered list https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000; Oxford's official Oxford 3000 wordlist PDF snapshot https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000.pdf; Oxford's overview of CEFR and POS filtering https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000.

## Twenty-fifth B1 batch: pack–push (candidate records pending individual dictionary verification)

Eighty-five records were added for the P section, covering the Oxford 3000 B1 grammatical entries from `pack` through `push`: `pack`, `package`, `painful`, `pale`, `pan`, `participate`, `particularly`, `pass` (noun), `passion`, `path`, `payment`, `peaceful`, `percentage`, `perfectly`, `performance`, `personally`, `persuade`, `photographer`, `photography`, `pin` (noun and verb), `pipe`, `place` (verb), `planning`, `pleasant`, `pleasure`, `plenty`, `plot` (noun), `plus` (preposition), `podcast` (noun), `poem`, `poet`, `poetry`, `point` (verb), `poison` (noun and verb), `poisonous`, `policy`, `political`, `politician`, `politics`, `port`, `portrait`, `possibly`, `pot`, `pour`, `poverty`, `powder`, `powerful`, `practical`, `pray`, `prayer`, `prediction`, `prepared`, `presentation`, `press` (noun and verb), `pressure`, `pretend`, `previous`, `previously`, `priest`, `primary`, `prince`, `princess`, `printing`, `prisoner`, `private`, `producer`, `production`, `profession`, `profit`, `program` (verb), `promote`, `proper`, `properly`, `property`, `protest` (noun and verb), `proud`, `prove`, `pull` (noun), `punish`, `punishment`, and `push` (noun).

The current Oxford B1-filtered online list supports the part-of-speech assignments surfaced in the search results, while the official Oxford 3000 PDF provides a static cross-check for the wider P sequence. Distinct lower-level forms are retained separately rather than duplicated indiscriminately: `pass` verb A2 vs noun B1; `place` noun A1 vs verb B1; `point` noun A1 vs verb B1; `program` noun A2 vs verb B1; and `pull`/`push` verbs A2 vs nouns B1. The UK form `programme` noun is A1 and is not conflated with the B1 verb `program`. Other nearby forms not included at B1 include `participant` noun B2, `patient` adjective B2, `particular` adjective A2, `passenger` noun A2, `permission` noun A2, `permit` verb/noun B2, `phase` noun B2, `physics` noun A2, `principal` noun C1 and adjective B2, `pole` noun C1, `proceeds` noun C1, and `professional` noun B2.

All 85 records remain `needs_review`. Their UK IPA, precise dictionary sense, Ukrainian equivalent and original example pair have not yet completed individual dictionary-entry verification. The spelling `program` is retained for the verb entry as listed by Oxford; British usage context and any preferred spelling normalization should be checked before final approval. No record in this batch is marked verified.

Primary references: current Oxford 3000/5000 wordlist (including B1 filter and part-of-speech labels), https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000; Oxford 3000 full PDF, https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000.pdf; Oxford 3000 by CEFR PDF, https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf.
## Twenty-sixth B1 batch: qualified–quotation (candidate records pending individual dictionary verification)

Seven records were added for the Q section: `qualified` (adjective), `qualify` (verb), `queue` (verb), `quit` (verb), `quotation` (noun), and `quote` (noun and verb). The current Oxford B1-filtered online list supports these part-of-speech assignments. The current online classification differs from the older static PDF for two nearby forms: `qualification` noun is B2 and `queue` noun is B2, so neither is added to B1; only `queue` verb is included. The static PDF lists `qualification` noun and `queue` noun at B1, but the current online list is the project's primary CEFR reference.

All seven records remain `needs_review`. Their IPA, exact dictionary sense, Ukrainian equivalent and original examples have not yet completed individual dictionary-entry verification. The `qualified` adjective is used in the sense of having the training or experience needed for a job; `qualify` is illustrated in the sense of gaining a professional qualification; `queue` is the verb meaning to wait in a line; `quit` means to leave a job; `quotation` is a passage quoted from a source; and `quote` is represented separately as noun and verb.

Primary references: current Oxford B1-filtered list https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000?dataset=english&level=b1&list=ox3000; current Oxford wordlist results for the Q entries https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000; static Oxford 3000 PDF snapshot https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000.pdf; Oxford individual entry for `qualify` https://www.oxfordlearnersdictionaries.com/definition/english/qualify and `quotation` https://www.oxfordlearnersdictionaries.com/definition/english/quotation.

## R batch — 60 candidate records (IDs 2621–2680)

Added 60 B1 records from the R section of the Oxford 3000 by CEFR level list. The batch includes the following headwords and POS distinctions: `race` (people/ethnic group, noun; not the A2 competition sense), `racing` noun, `range` noun, `rare` adjective, `rarely` adverb, `reaction` noun, `reality` noun, `receipt` noun, `recommendation` noun, `reference` noun, `reflect` verb, `regularly` adverb, `reject` verb, `relate` verb, `related` adjective, `relation` noun, `relative` noun and adjective, `relaxed` adjective, `relaxing` adjective, `release` verb and noun, `reliable` adjective, `religion` noun, `religious` adjective, `remain` verb, `remind` verb, `remote` adjective, `rent` verb and noun, `repair` noun, `repeat` noun, `repeated` adjective, `represent` verb, `request` verb, `require` verb, `reservation` noun, `resource` noun, `respect` noun and verb, `responsibility` noun, `responsible` adjective, `result` verb, `retire` verb, `retired` adjective, `revise` verb, `ring` noun (the B1 sound/call sense, distinct from the A2 jewellery sense), `rise` noun, `risk` noun and verb, `robot` noun, `roll` verb and noun, `romantic` adjective, `rope` noun, `rough` adjective, `row` noun, `royal` adjective, `rugby` noun and `rule` verb.

The CEFR/POS candidate inventory was checked against the Oxford 3000 by CEFR level PDF and cross-checked against the Oxford 3000 full-list PDF snapshot. These are list-level checks, not individual dictionary-entry verification. The 60 records therefore remain `needs_review`; UK IPA, sense selection, Ukrainian glosses and original example pairs still require individual review. The current online Oxford wordlist is the project's primary reference where it can be checked directly; static PDFs are retained as dated corroborating snapshots.

References: Oxford 3000 by CEFR level PDF (https://englishpages.net/wp-content/uploads/2024/08/The_Oxford_3000_by_CEFR_level.pdf); Oxford 3000 full list PDF (https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000.pdf); Oxford wordlists overview (https://www.oxfordlearnersdictionaries.com/wordlist/).
