# Replay receipt (release 0.1.0-candidate, 15 November 2026)

Release replay by the publisher from fresh copies of the five approved scripts (one copy of the package scripts per
mode, never the candidate directory), with bytecode writing disabled, on macOS 27.2.1 arm64, CPython 3.11.14,
standard library only.

| Script | Normal (`python3 -I -B`) | Optimised (`python3 -O -I -B`) |
|---|---|---|
| `verify.py --output verification.json` | exit 0, "All checks passed"; output identical to the shipped file except the recorded Python version and run time | the same |
| `verify_independent.py > verification_independent.jsonl` | exit 0; byte-identical | exit 0; byte-identical |
| `fingerprints.py` | exit 0; `fingerprints.json` byte-identical | exit 0; byte-identical |
| `verify_small_complete.py verification_small_complete.json` | exit 0; byte-identical | exit 0; byte-identical |
| `verify_extensions.py --output verification_extensions.json` | exit 0 (930,660 tail cases, minimum ratio 5/4); byte-identical | exit 0; byte-identical |

**Negative control.** In a copy of `verify.py` the support check `require(support >= target, ...)` was changed to
`require(support > target, ...)`, which is false at every extremal vector. Under `python -O` the script stopped with
`RuntimeError: ('support', (-2, 2), 1, 2, 2)` and exited with status 1, so its checks stay active under optimisation.

The lead's earlier replays of the same script bytes (14 November 2026) gave the same results.

## After the replay

The only later changes are text and metadata: the version and DOI added to the date line on the paper's title page;
the PDF rebuilt with three pdflatex passes (19 pages; a text comparison with the approved PDF shows only that line);
README.md (DOI, file list, citation and status added); and the release files (`AI_INDEX.md`, `REVIEW_SUMMARY.md`,
`RESEARCH_GATES.json`, `refs.bib`, `LICENSE.md`, `CITATION.cff`, `.zenodo.json`, `ENVIRONMENT.txt`, this receipt,
the CI workflow and the regenerated `SHA256SUMS`). The five scripts, their five outputs, `claim_ledger.md` and
`PRIOR_ART.md` are byte-identical to the approved candidate.

This receipt records execution only. The theorems rest on the written proofs; the scripts check finite ranges.
