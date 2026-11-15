# Prior art and novelty boundary

Release 0.1.0-candidate, 14 November 2026. Searches of arXiv, Semantic Scholar (including the citation graph of
Mogilnykh–Vorob'ev–Valyuzhenich 2018), Crossref and the web were made on 12 and 14 November 2026 for each main
statement, its formulas (for example the sequence 252, 420, 660, 990, … of minimum supports at k = 5) and its aliases
(minimum support / Johnson eigenfunction / MMS-type; entropic MMS / Rényi; hypergeometric tail / Aydinian–Blinovsky;
Boolean-slice distance / spherically punctured codes). No earlier proof of MVV Conjecture 1, no solution of the Rényi
optimisation of Ai–Kuželka–Pelekis, and no proof of the hypergeometric tail statement for 4k ≤ n < 8k was found.
This is evidence of novelty, not a guarantee of historical priority.

| Source | What it contains | Relation to this paper |
|---|---|---|
| Mogilnykh, Vorob'ev, Valyuzhenich 2018 (doi 10.33048/semi.2018.15.137; arXiv 1810.04075) | Thm 1: minimisers are coordinate differences or two-valued; §5: computer comparison for 6 ≤ n ≤ 600, balanced value, exceptions; Conjecture 1. | Thm 1.1 proves Conjecture 1 for all n and adds the (5,2) minimiser missing from Thm 1. |
| Vorob'ev, Mogilnykh, Valyuzhenich 2018 (doi 10.1016/j.disc.2018.04.018) | Minimum supports of every Johnson eigenspace for n ≥ n₀(k), n₀ unspecified. | Thm 1.1 makes the first eigenspace explicit for all n. |
| Sotnikova, Valyuzhenich 2021 survey (doi 10.26493/2590-9770.1404.61e) | Restates MVV Thm 1 as Thm 5. | Same (5,2) omission. |
| Ai, Kuželka, Pelekis 2026 (arXiv 2606.30486v1) | Shannon bound; Lemma 3 chain majorization; Cor 5 reduces Rényi to hypergeometric laws; §5: optimisation unsolved, numerics suggest i = 1. | Thm 1.3 solves it; the suggestion fails at n = 2k above α_k. |
| Ai, Kuželka, Pelekis 2025 (arXiv 2503.20473) | Majorization of populations for tail bounds in sampling without replacement. | Adjacent; does not contain the results here. |
| Ai, Pelekis 2026 (doi 10.1016/j.spl.2026.110798; arXiv 2601.09485) | Tail P(H ≥ EH) ≥ k/n for n ≥ 8k; authors state they could not reach n ≥ 4k. | Thm 1.5 reaches n ≥ 4k. |
| Ai, Karagiannis, Kuželka, Pelekis 2026 (arXiv 2610.24726v1) | Thm 2: IFR lemma; Thm 3: P(H > EH) ≥ 1/4 for non-integer mean (and ≥ 1/6 for integer mean) under mild conditions. | Used in the proof of Thm 1.5 (credited); the paper does not mention the MMS or 4k consequence. |
| Aydinian, Blinovsky 2012 (doi 10.1134/S0032946012040059); Manickam, Singhi 1988; Pokrovskiy 2015 | The two-valued reduction conjecture; MMS conjecture; MMS for n ≥ 10^46 k. | Context for Thm 1.5 and Cor 7.2. |
| Mattner, Schulz 2018 (doi 10.1090/tran/6986); Levin 2024 (doi 10.1080/07474946.2024.2379901; preprint arXiv 2311.17884) | Normal approximation of symmetric hypergeometric laws; peakedness about a fixed centre (half the category sizes) as the sample size varies. | Thm 4.3 compares balanced laws centred at their moving means; different ordering. |
| Madiman, Wang, Woo 2019 (doi 10.1016/j.disc.2019.03.002) | Majorization, Sperner theory and Rényi entropy. | General framework; no subset-sum optimisation. |
| Dumer, Kapralova 2013 (doi 10.1109/TIT.2013.2250579); Brouwer, Cioabă, Ihringer, McGinnis 2018, Thm 1.2 (doi 10.1016/j.jctb.2018.04.005) | Binary Krawtchouk extremum (BCIM attribute it to DK Cor. 10 and reprove it). | Input to Thm 1.6; binary distance is prior work. |
| Amireddy, Behera, Srinivasan, Sudan 2025 (doi 10.4230/LIPIcs.ICALP.2025.11; ECCC TR25-056) | Degree-one distance ≥ (r−1)/n for n ≥ 8; its proof yields the balanced value. | Thm 1.6 gives the exact value (r/n off half-sampling) for all n and all groups. |
| Grosu, Person, Szabó 2014 (doi 10.1112/jlms/jdu029) | Rank-extremal families; report that the case behind Cor 6.3 was determined by Odlyzko and, for every rank deficiency, by Ahlswede–Aydinian–Khachatrian. | Cor 6.3 is a known value, re-derived from Cor 6.1. |
