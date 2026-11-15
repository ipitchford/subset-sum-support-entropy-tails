# Review summary (public, rating-free)

Internal AI-assisted review of the first version and of its revision (14 November 2026), and a source check at
publication (15 November 2026). This is not human peer review, independent reproduction or formal verification.

**Who reviewed.** First round: five reviewer roles run as separate AI agents (editor, methodology, domain specialist,
cross-disciplinary perspective, devil's advocate), one adversarial review by a second AI model, and a clean replay of
the shipped scripts. Second round, on the revision: a re-review of everything that changed, a proof audit of the new
and rewritten proofs, an audit of the new proofs by the second model, and a final replay in normal and `python -O`
mode. At publication the scripts were replayed again from fresh copies and two attributions were checked against the
cited sources (below).

## Outcome

No reviewer in either round found an error in a main result or a counterexample. The requested changes concerned
readability, positioning against earlier work, notation, a handful of one-sentence proof gaps, references and the
verification scripts. One revision round addressed them and added two results (the tail theorem from n = 4k and the
small-ball inequality). The second round found two wrong sentences whose conclusions were unaffected, one attribution
gap, one over-stated sentence in the introduction and one misreported source; all were corrected. No numbered result
changed in the second round.

## Objections and how each was handled

| Objection | Disposition |
|---|---|
| The first version gave little context and was hard to read; notation was overloaded (Hyp and Ber undefined; several letters reused) | New introduction (the question in plain terms, what was known by strand, notation, main results stated first, what is new and what is not, roadmap); every section opens by saying what it does; half-sample size is k throughout |
| MVV's own evidence and the earlier asymptotic result were not stated | The introduction and the table in Theorem 1.1 state that MVV compared the two candidate values by computer for 6 <= n <= 600 and that Vorob'ev-Mogilnykh-Valyuzhenich treat n >= n0(k) with n0 unspecified; the status column says which values are MVV's |
| The numerical suggestion of Ai-Kuzelka-Pelekis was quoted too strongly | Quoted as "numerical experiments suggest the minimum is at i = 1" |
| Six steps were justified in one sentence (Lemma 2.2 inequalities, Lemma 4.2, Theorem 4.3 parity lattice and averaging, the central atom in Corollary 6.1, Lemma 8.1 termination, the asymptotics of alpha_k) | Each written out; Corollary 1.4 given its own proof; equality cases of Theorem 1.3 split into labelled cases |
| The zero-sum theorem is not characteristic-free, and the paper did not say so | Remark 8.3: explicit counterexamples over Z_2, Z_3 and Z_5 (224 < 252, 414 < 420, 210 < 252), recomputed by two reviewers; the finite-group problem is listed as open |
| Context for the Manickam-Miklos-Singhi (MMS) problem and adjacent work was missing | Manickam-Singhi 1988, Pokrovskiy 2015, Aydinian-Blinovsky 2012, Ai-Pelekis 2026 and Ai-Kuzelka-Pelekis 2025 cited; the survey of Sotnikova-Valyuzhenich cited in its published form |
| Extension requested: is the single-outlier tail bound true beyond n >= 8k? | Theorem 1.5 proves it for n >= 4k, using a 2026 lemma of Ai, Karagiannis, Kuzelka and Pelekis (credited); Corollary 7.2 states plainly that it gives MMS only conditionally on the Aydinian-Blinovsky conjecture; Remark 7.3 records that below 4k a single outlier is not always worst |
| One verification script used `assert` | Replaced by explicit checks; all five scripts exit nonzero on failure under `python -O`; a complete certificate for n <= 7 (verify_small_complete.py) and a script for the extensions were added |
| Second round: a sign relation in Section 5 was reversed, and the error rate in Remark 5.1 was wrong | Both sentences corrected; the downstream reasoning was already right |
| Second round: Case B of the tail proof follows an argument already in Ai-Karagiannis-Kuzelka-Pelekis | Credited to their Theorem 3(1); the "what is new" list rewritten accordingly |
| Second round: the introduction claimed that every question reduces to two-valued populations | Corrected: proved for the zero atom and the whole law; for the sign it is the Aydinian-Blinovsky conjecture |
| Second round: the incidence-rank corollary was presented as new and misread its source | Corollary 6.3 is now stated as known (Odlyzko; Ahlswede-Aydinian-Khachatrian, as reported by Grosu-Person-Szabo, Section 2) and removed from the abstract |

Smaller items (global ranges n >= 2, 1 <= k <= n-1; the (2,1) equality note; exact wording of the gain over
Amireddy-Behera-Srinivasan-Sudan; endpoint conventions) were fixed in the same round.

## Source check at publication (15 November 2026)

- **Dumer and Kapralova (2013), Lemma 8.2.** The journal article was read in full. Its Corollary 10 states that for all
  b in [1, m-1] and w in [1, m-1] the Krawtchouk polynomial K_b^m(w) has maximum absolute value at w = 1, except for
  m = 2b, where the maximum is at w = 2. Its definition of K_b^m(w) (equation 4) is the manuscript's K_k^(n)(i) with
  (m, b, w) = (n, k, i). The attribution in Lemma 8.2 and the remark after it is correct as written; nothing changed.
- **Levin (2024), the sentence after Theorem 4.3.** The arXiv preprint 2311.17884v1 (Theorem 1) and the author's
  Columbia Biostatistics Technical Report B-255 (which restates the 2024 result as its Theorem 2) both describe
  symmetric intervals centred at half the population category sizes, a centre that does not depend on the sample
  size, with the probability monotone in the sample size on each side of half the population. This matches the
  manuscript's description, "peakedness about a fixed centre as the sample size varies"; neither contains a
  moving-centre or majorization result. The sentence is attribution only and is used in no proof; nothing changed.

## What the review did not do

No human specialist read the paper; nothing was formalised in a proof assistant; the prior-art search was bounded
(see RESEARCH_GATES.json).
