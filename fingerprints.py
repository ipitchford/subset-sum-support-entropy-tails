#!/usr/bin/env python3
"""Reproduce exact fingerprints used in the novelty comparison; Python standard library."""
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib
import json


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def digest(matrix):
    value = json.dumps(matrix, separators=(",", ":")).encode()
    return hashlib.sha256(value).hexdigest()


def matrix_record(n, k):
    sets = list(combinations(range(n), k))
    matrix = [[int(j in subset) for j in range(n)] for subset in sets]
    transpose = list(map(list, zip(*matrix)))
    reverse = [row[::-1] for row in matrix[::-1]]
    gram = [[sum(row[i] * row[j] for row in matrix) for j in range(n)] for i in range(n)]
    small = c(n - 2, k - 1)
    large = k * c(n - 1, k - 1)
    return dict(n=n, k=k, dimensions=[len(matrix), n], matrix=matrix,
                rank=n, gram=gram, gram_trace=sum(gram[j][j] for j in range(n)),
                gram_determinant=large * small ** (n - 1),
                gram_characteristic_polynomial=f"(lambda-{large})*(lambda-{small})^{n-1}",
                row_sums=[k] * len(matrix), column_sums=[c(n - 1, k - 1)] * n,
                hashes=dict(matrix=digest(matrix), transpose=digest(transpose),
                            reversed_rows_and_columns=digest(reverse),
                            sorted_rows=digest(sorted(matrix)),
                            reversed_columns_sorted_rows=digest(sorted(row[::-1] for row in matrix))))


result = dict(
    conventions="Exact probabilities; n population size, k sample size, i marked population count.",
    hypergeometric_instances=[dict(n=n, k=k, i=i,
        numerator=[c(i,j)*c(n-i,k-j) for j in range(k+1)],
        denominator=c(n,k),
        probabilities=[str(Fraction(c(i,j)*c(n-i,k-j),c(n,k))) for j in range(k+1)])
        for n,k in [(4,2),(6,3),(8,4),(15,5)] for i in range(1,min(n,5))],
    krawtchouk_n8_k4=[sum((-1)**j*c(i,j)*c(8-i,4-j) for j in range(5)) for i in range(9)],
    support_k5=[dict(n=n, value=2*c(n-2,4)) for n in range(11,31)],
    balanced_maximum_atoms=[str(Fraction(m,2*m-1)) for m in range(2,22)],
    balanced_outer_atoms=[str(Fraction(m-1,2*(2*m-1))) for m in range(2,22)],
    incidence_matrices=[matrix_record(n,k) for n,k in [(3,1),(4,2),(5,2)]],
    prior_art_collision="The binomial, Krawtchouk and incidence objects are classical. The proposed contribution is the stated optimisation/proof, not those objects."
)
Path("fingerprints.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print("Exact fingerprints written to fingerprints.json")
