# Claim ledger

Release 0.1.0-candidate, 14 November 2026. "Proved" means a complete written proof is in the manuscript; numbering follows the PDF.

| Claim | Status | Prior-work boundary |
|---|---|---|
| Thm 1.1: m(n,k) = 2C(n−2,k−1) for k ≥ 5, n ≥ 2k+1, unique minimiser D (MVV 2018, Conjecture 1) | Proved (Lemma 2.2 is the new step) | MVV reduced to two vector classes and compared the two expressions by computer for 6 ≤ n ≤ 600; VMV 2018 for n ≥ n₀(k), n₀ unspecified. |
| Thm 1.1: full formula and all minimisers for every n, k | Proved; complete computer certificate for n ≤ 7 | Balanced value and exceptions (6,2), (9,3), (10,4), tie (8,2) recorded in MVV §5. New: no further exceptions for k ≤ 4 beyond n = 600. |
| Extra minimiser (1,1,−1,−1,0) at (n,k) = (5,2) | Proved | Missing from MVV Thm 1 and SV Thm 5; the value m(5,2) = 6 is unchanged. |
| Lemma 2.1 (three distinct values) | Proved | MVV Thm 1 counting argument, stated here over any Abelian group with an affine constant. |
| Lemma 4.1 (chain reduction to hypergeometric laws) | Proved | Ai–Kuželka–Pelekis 2026, Lemma 3; stated at any strict gap, with the increment bound. |
| Thm 1.2 majorization frontier; Thm 4.3 parity chain for Hyp(2k,t,k) | Proved | Balanced maximal atom k/(2k−1) is in MVV §5; the full parity chain is new as far as the comparison in PRIOR_ART.md goes. |
| Thm 1.3: exact minimum Rényi entropy at every finite order, threshold α_k, all minimisers | Proved | Answers the optimisation AKP 2026 (§5) could not solve; their numerical suggestion holds except at n = 2k above α_k. |
| Cor 1.4: universal Bernoulli bound holds exactly for 0 < α ≤ 2 | Proved; counterexample (1,1,0,0), k = 2, α = 3 | — |
| Thm 1.5: min_i P(Hyp(n,i,k) ≥ ik/n) = k/n for n ≥ 4k, unique at i = 1 for n > 4k | Proved; checked for k ≤ 40, 4k ≤ n ≤ 10k | Ai–Pelekis 2026 proved n ≥ 8k. Proof uses AKKP 2026 Theorem 2 and Theorem 3(1). |
| Cor 7.2: Aydinian–Blinovsky conjecture ⇒ MMS conjecture for n ≥ 4k | Proved (conditional statement) | The reduction itself is a conjecture (Aydinian–Blinovsky 2012). |
| Remark 7.3: one outlier is not optimal for some 2k < n < 4k | Computed for k ≤ 40 (largest failing n/k = 10/3) | AKP note n = 3k+1. Exact threshold open. |
| Cor 6.1 largest atom; Cor 6.2 small-ball inequality | Proved | Balanced atom value from MVV. |
| Cor 6.3 largest families with incidence rank < n | Proved (short consequence of Cor 6.1) | Not new: Odlyzko determined this case and Ahlswede–Aydinian–Khachatrian solved every rank deficiency, as reported by GPS 2014 (Section 2). |
| Thm 1.6 exact degree-one distance over every nontrivial Abelian group | Proved | Binary case: Dumer–Kapralova 2013 (via BCIM 2018 Thm 1.2). Balanced value for n ≥ 8 implicit in the proof of ABSS 2025 Thm 6.1, whose stated bound is (r−1)/n (gain 1/n away from n = 2k). |
| Thm 1.6 entropy dichotomy by elements of order two | Proved | No classification of group-valued minimisers is claimed. |
| Remark 8.3: zero-sum theorem fails over Z_2, Z_3, Z_5 | Verified examples | Exact value over Z_q open. |
