# Fixed-size subset sums: sharp support, Rényi entropy and tail bounds

Author: Anonymous. Release 0.1.0-candidate, 15 November 2026. Unrefereed research candidate; text CC0-1.0, code MIT.

DOI: [10.5281/zenodo.24241302](https://doi.org/10.5281/zenodo.24241302) (this version; all versions:
[10.5281/zenodo.24241301](https://doi.org/10.5281/zenodo.24241301)). Plain-English page:
https://evidencepress.org/releases/subset-sum-support-entropy-tails/

## What this is about

Pick k of n given real numbers at random, without replacement, and add them up. How concentrated can that random sum be?
The paper answers this exactly in three senses.

1. **How often can the sum be exactly zero?** If the numbers add up to zero and are not all zero, at least
   2·C(n−2, k−1) of the k-subsets have a nonzero sum whenever k ≥ 5 and n ≥ 2k+1, and only the pattern
   (1, −1, 0, …, 0) achieves this. In the language of graph theory this is the smallest support of an eigenfunction
   in the first nontrivial eigenspace of the Johnson graph. It proves Conjecture 1 of Mogilnykh, Vorob'ev and
   Valyuzhenich (2018), which they had checked by computer for n ≤ 600. A formula for every n and k is given, with all
   extremal vectors, including one small case, (1, 1, −1, −1, 0) at n = 5, k = 2, that earlier classifications missed.
2. **How small can its entropy be?** For every Rényi order the minimum is found, answering a question left open by
   Ai, Kuželka and Pelekis (2026). A "one outlier" population is optimal, except when exactly half the numbers are
   drawn: there a "two outliers" population wins once the order exceeds an explicit threshold α_k (α_2 = 2, growing
   like 1.386k). So the natural Bernoulli lower bound holds for every population exactly for orders up to 2.
3. **How rarely can it be nonnegative?** For the two-valued populations to which Aydinian and Blinovsky conjecturally
   reduce the Manickam–Miklós–Singhi (MMS) problem, the chance of a nonnegative sum is smallest for a single outlier
   whenever n ≥ 4k. Ai and Pelekis (2026) had this for n ≥ 8k. So the Aydinian–Blinovsky conjecture would imply the
   MMS conjecture in its full range.

Exact analogues over Abelian groups (where the answer depends on whether the group has an element of order two),
and a small-ball inequality for sampling without replacement complete the picture; a known incidence-rank result is
re-derived in a few lines.

All results have complete written proofs; no step of any proof is computational. The scripts below check the
statements exactly on finite ranges.

## Contents

| File | Purpose |
|---|---|
| `manuscript.pdf`, `manuscript.tex` | The paper, with proofs and bibliography (pdfLaTeX). |
| `verify.py` → `verification.json` | Support formula and minimisers on all zero-sum vectors with entries in {−2,…,2}, n ≤ 10; hypergeometric atoms and equality cases, n ≤ 60; parity majorization for all population sizes 2k ≤ 200; entropy and equality statements on all populations with entries in {0,1,2,3}, n ≤ 10; the explicit examples and threshold values α_k. |
| `verify_independent.py` → `verification_independent.jsonl` | Lemma 2.2 for every k ≥ 5, n ≤ 300 (24,758 integer-mean cases); Lemma 8.1 on all unimodal sequences of length ≤ 8 over {0,1,2,3} plus 100,000 random ones; hypergeometric residue classes; Theorem 1.6 on six small Abelian groups. |
| `verify_small_complete.py` → `verification_small_complete.json` | Complete certificate of Theorem 1.1 (values and all minimisers) for n ≤ 7; the docstring explains why the finite search box is exhaustive. |
| `verify_extensions.py` → `verification_extensions.json` | Theorem 1.5 for all k ≤ 40, 4k ≤ n ≤ 10k (930,660 cases), the parameters below 4k where one outlier is not optimal, the identity used in the proof, the small-ball inequality, and the Z_q counterexamples of Remark 8.3. |
| `fingerprints.py` → `fingerprints.json` | Rational sequences, small matrices and hashes used for prior-art comparison. |
| `claim_ledger.md` | Each claim, its status and what is prior work. |
| `PRIOR_ART.md` | Sources compared and the novelty boundary. |
| `refs.bib` | The bibliography, built from Crossref, DataCite and arXiv records. |
| `AI_INDEX.md` | Machine-oriented map of claims, evidence and limits. |
| `REVIEW_SUMMARY.md` | What the internal review checked, the objections raised and how each was handled. |
| `RESEARCH_GATES.json` | Dated prior-art searches, sources read and limitations triage. |
| `REPLAY_RECEIPT.md`, `ENVIRONMENT.txt` | The release replay and the software used. |
| `LICENSE.md`, `CITATION.cff`, `.zenodo.json` | Licences and citation metadata. |
| `.github/workflows/replay.yml` | Continuous integration: every script, normal and `python -O`, plus a negative control. |
| `SHA256SUMS` | SHA-256 hashes of every other file in the package. |

## Reproduce

Python 3.10 or later, standard library only. Run from a copy of this folder:

```bash
python3 verify.py --output verification.json
python3 verify_independent.py > verification_independent.jsonl
python3 fingerprints.py
python3 verify_small_complete.py verification_small_complete.json
python3 verify_extensions.py --output verification_extensions.json
```

Each script finishes in seconds and exits nonzero on any failed check, also under `python3 -O`. All comparisons use
integers or exact fractions; the only floating-point output is the illustrative threshold table in `verification.json`.
`verification.json` also records the Python version and run time, which naturally differ between runs.

Build the PDF with `pdflatex manuscript.tex` (three passes, for the table of contents). Check the package with
`shasum -a 256 -c SHA256SUMS`.

## Limits

The finite checks cover finite ranges only; the unrestricted statements rest on the proofs. The paper does not settle
the MMS conjecture itself (it needs the Aydinian–Blinovsky reduction), the tail problem for n < 4k, higher Johnson
eigenspaces, the zero-sum problem over finite groups, or polynomial distance on slices for degree two or more.
The proofs have been checked by AI-assisted internal review and exact computation, not by external referees or a proof
assistant. The paper was prepared with substantial assistance from AI systems.

## Cite

Anonymous (2026). *Fixed-size subset sums: sharp support, Rényi entropy and tail bounds*. Version 0.1.0-candidate.
Zenodo. https://doi.org/10.5281/zenodo.24241302

## Status

Unrefereed research candidate, published by Evidence Press. Text, data and the paper are CC0-1.0; the Python scripts
and CI workflow are MIT (see `LICENSE.md`).
