# AI index: Fixed-size subset sums (v0.1.0-candidate)

Machine-oriented map of claims, evidence and limits. Human readers should start with [README.md](README.md) and the
paper [manuscript.pdf](manuscript.pdf) (source [manuscript.tex](manuscript.tex); Section 1 is a plain introduction:
the question, what was known, notation, main results, what is new and what is not, and a roadmap).
DOI 10.5281/zenodo.24241302 (concept 10.5281/zenodo.24241301). Status: unrefereed candidate; internal AI-assisted
review only. Per-claim prior-work boundaries: [claim_ledger.md](claim_ledger.md); sources compared:
[PRIOR_ART.md](PRIOR_ART.md); bibliography: [refs.bib](refs.bib).

## Normalisation

Population x = (x_1, ..., x_n) of reals, n >= 2, 1 <= k <= n-1, r = min(k, n-k). S uniform among the k-subsets of
[n]; X = sum_{i in S} x_i. Hyp(n,i,k) = number of marked items in a uniform k-sample from n items of which i are
marked. Ber(p) = (1-p, p). At half-sampling n = 2k: U = (1/2, 1/2) and Q_k = ((1-q_k)/2, q_k, (1-q_k)/2) with
q_k = k/(2k-1), the laws of one and two outliers. p <= q is majorization of sorted mass vectors (padded by zeros).
H_alpha is Renyi entropy in bits. m(n,k) = minimum number of k-subsets with nonzero sum over nonzero x with zero
total, i.e. the minimum support of an eigenfunction in the first nontrivial eigenspace of the Johnson graph J(n,k).
D = (1, -1, 0, ..., 0).

## Claims and where they are proved

| ID | Claim | Location | Status / credit |
|---|---|---|---|
| T1.1 | m(n,k) = 2 if r = 1; 2C(n-2,r-2) if n = 2r, r >= 2; 6, 39, 110 at (n,r) = (6,2), (9,3), (10,4); 2C(n-2,r-1) otherwise; all minimising vectors listed | Theorem 1.1, Sections 2-3 | written proof. Reduction to two vector classes: MVV 2018 Thm 1; balanced value and exceptions: MVV Section 5. New: uniform proof of the comparison (Lemma 2.2), hence MVV Conjecture 1 |
| T1.1a | m(n,k) = 2C(n-2,k-1) for k >= 5, n >= 2k+1, attained only by D up to scaling and permutation | Theorem 1.1 | proves MVV 2018 Conjecture 1 (they compared the two expressions by computer for 6 <= n <= 600) |
| T1.1b | (n,k) = (5,2): (1,1,-1,-1,0) is a second minimiser (value 6 unchanged) | Theorem 1.1, Remark 3.1 | new; absent from MVV Thm 1 and the survey SV 2021 Thm 5 |
| L2.2 | Integer-mean atom estimate for two-valued vectors | Lemma 2.2 | written proof; checked for every k >= 5, n <= 300 (24,758 integer-mean cases) |
| T1.2 | Majorization frontier: p <= Ber(k/n) if n != 2k or n = 2; p <= U or p <= Q_k if n = 2k >= 4; U and Q_k incomparable; all attained | Theorem 1.2, Section 4 | written proof; chain reduction is AKP 2026 Lemma 3 (Lemma 4.1) |
| T4.3 | Parity majorization chain for balanced hypergeometric laws Hyp(2k,t,k) | Theorem 4.3 | written proof; checked for all 2k <= 200 |
| T1.3 | Exact minimum of H_alpha(X) over nonconstant x for every 0 < alpha < infinity; threshold alpha_k defined by (1/2)(2k/(2k-1))^a + ((k-1)/(2k-1))^a = 1; alpha_2 = 2, alpha_k increasing, alpha_k = (2k - 1/2) ln 2 - ln2/(24k) + O(k^-2); every minimiser two-valued with multiplicities {1,n-1} or {2,n-2} | Theorem 1.3, Section 5 | written proof; answers the optimisation left open by AKP 2026 (Section 5) |
| C1.4 | H_alpha(X) >= H_alpha(Ber(k/n)) for all nonconstant real x and all n, k iff 0 < alpha <= 2 | Corollary 1.4 | written proof; counterexample (1,1,0,0), k = 2, alpha = 3: power sum 11/36 > 1/4 |
| T1.5 | For n >= 4k and 1 <= i <= n-1: P(Hyp(n,i,k) >= ik/n) >= k/n, equality at i = 1, only at i = 1 when n > 4k | Theorem 1.5, Section 7 | written proof using AKKP 2026 Theorem 2 (IFR lemma) and Theorem 3(1); Ai-Pelekis 2026 had n >= 8k; checked for k <= 40, 4k <= n <= 10k (930,660 cases, minimum ratio 5/4 for i >= 2) |
| C7.2 | The Aydinian-Blinovsky conjecture implies the Manickam-Miklos-Singhi conjecture for all n >= 4k | Corollary 7.2 | conditional statement; does NOT prove MMS |
| R7.3 | Below n = 4k a single outlier is not always extremal (k <= 40: failures up to n/k = 10/3) | Remark 7.3 | computed |
| T1.6 | Over a nontrivial Abelian group G: degree-one functions on the slice have support proportion >= r/n (n != 2k), (k-1)/(2k-1) (n = 2k >= 4), 1/2 ((n,k) = (2,1)), attained; entropy minimum at n = 2k depends on whether G has an element of order two | Theorem 1.6, Section 8 | written proof; binary distance is Dumer-Kapralova 2013 (Cor. 10; see BCIM 2018 Thm 1.2); balanced value for n >= 8 implicit in ABSS 2025 Thm 6.1 (stated bound (r-1)/n) |
| L8.2 | Binary Krawtchouk extremum: |K_k(i)| <= |K_k(1)| (k != n/2), <= |K_k(2)| (k = n/2), 1 <= i <= n-1 | Lemma 8.2 | prior work: Dumer-Kapralova 2013 Corollary 10 (checked against the journal text); reproved in BCIM 2018 Thm 1.2 |
| C6.1, C6.2 | Largest atom of X; small-ball inequality for intervals of length at most the largest population gap | Corollaries 6.1, 6.2 | written proofs; balanced atom value from MVV |
| C6.3 | Largest families with incidence rank < n | Corollary 6.3 | known (Odlyzko; Ahlswede-Aydinian-Khachatrian, as reported in GPS 2014 Section 2); re-derived |
| R8.3 | The zero-sum theorem fails over Z_2, Z_3, Z_5 (224 < 252, 414 < 420, 210 < 252) | Remark 8.3 | verified examples |

No step of any proof is computational. The scripts check statements exactly on finite ranges and corroborate, but do
not replace, the proofs.

## Evidence files

| File | What it checks | Output |
|---|---|---|
| [verify.py](verify.py) | T1.1 on all zero-sum vectors with entries in {-2..2}, n <= 10; hypergeometric atoms and equality cases, n <= 60; T4.3 for 2k <= 200; T1.3 equality statements on populations with entries in {0..3}, n <= 10, orders 2, 3, 5; examples and alpha_k decimals | [verification.json](verification.json) (python and elapsed_seconds fields vary by run) |
| [verify_independent.py](verify_independent.py) | L2.2 to n = 300; Lemma 8.1 on unimodal sequences; hypergeometric residue classes; T1.6 on Z2, Z3, Z4, Z5, Z6, Z2xZ2 | [verification_independent.jsonl](verification_independent.jsonl) |
| [verify_small_complete.py](verify_small_complete.py) | Complete certificate of T1.1 (values and all minimisers) for n <= 7 | [verification_small_complete.json](verification_small_complete.json) |
| [verify_extensions.py](verify_extensions.py) | T1.5 for k <= 40, 4k <= n <= 10k; R7.3; the identity used in Section 7; C6.2; R8.3 | [verification_extensions.json](verification_extensions.json) |
| [fingerprints.py](fingerprints.py) | Rational sequences and small matrices used for prior-art comparison | [fingerprints.json](fingerprints.json) |

Every script uses the Python standard library, integers and fractions.Fraction (the alpha_k decimals are labelled
approximations), and exits nonzero on any failed check, also under `python -O`. Release replay:
[REPLAY_RECEIPT.md](REPLAY_RECEIPT.md); software: [ENVIRONMENT.txt](ENVIRONMENT.txt); CI:
[.github/workflows/replay.yml](.github/workflows/replay.yml).

## Review and gates

[REVIEW_SUMMARY.md](REVIEW_SUMMARY.md) lists the objections of the internal review and their dispositions (rating-free).
[RESEARCH_GATES.json](RESEARCH_GATES.json) records the dated prior-art searches, the sources read in full and the
triage of limitations.

## Limits

- Real numbers for the zero-sum theorem; over Z_2, Z_3 and Z_5 it fails (R8.3). Exact value over finite groups open.
- First Johnson eigenspace only; higher eigenspaces and the Grassmann analogue open.
- The tail problem for 2k < n < 4k is open; MMS itself is not proved (C7.2 is conditional).
- Polynomial distance on slices for degree two or more is not addressed.
- Internal AI-assisted review only: no human peer review, independent reproduction or formal verification.

## Licence

Text, paper and data CC0-1.0; code (Python scripts, CI workflow) MIT. See [LICENSE.md](LICENSE.md). Creator: Anonymous.
