#!/usr/bin/env python3
"""Complete finite certificate of Theorem 1.1 (values and all minimisers) for 2 <= n <= 7.

Why a finite box suffices. A minimiser x has a maximal set Z of zero k-sums. The solutions of
{L_S = 0 : S in Z} together with sum(x) = 0 form a subspace containing x; if it had dimension >= 2,
some further L_S (not identically zero on it, by injectivity of x -> L_x) would cut out a nonzero
subspace with strictly more zeros, contradicting minimality. So x spans a line, the kernel of an
(n-1) x n matrix of rank n-1 whose rows are 0/1 vectors (subset indicators and the all-ones vector).
The kernel is spanned by the vector of signed (n-1)x(n-1) minors, whose entries are bounded by the
maximal determinant of an (n-1)x(n-1) 0/1 matrix: 1, 1, 2, 3, 5, 9 for orders 1..6 (OEIS A003432).
Hence every minimiser is, up to scale, an integer vector with entries in [-H, H], H = H(n-1).
The script enumerates all sorted such vectors, so permutations and scalings are covered.
Exits nonzero on any mismatch, also under python -O.
"""
import json, sys
from functools import reduce
from itertools import combinations, combinations_with_replacement
from math import comb, gcd

HMAX = {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 9}

def formula(n, k):
    r = min(k, n - k)
    if r == 1:
        return 2
    if n == 2 * r:
        return 2 * comb(n - 2, r - 2)
    return {(6, 2): 6, (9, 3): 39, (10, 4): 110}.get((n, r), 2 * comb(n - 2, r - 1))

def nf(v):
    g = reduce(gcd, (abs(t) for t in v))
    p = tuple(sorted(t // g for t in v))
    q = tuple(sorted(-t // g for t in v))
    return min(p, q)

def listed(n, k):
    r = min(k, n - k)
    D = [1, -1] + [0] * (n - 2)
    if r == 1:
        c = [D]
    elif n == 2 * r:
        c = [[r - 1] * 2 + [-1] * (n - 2)]
    else:
        c = {(5, 2): [D, [1, 1, -1, -1, 0]], (6, 2): [[1] * 3 + [-1] * 3], (8, 2): [D, [1] * 4 + [-1] * 4],
             (9, 3): [[2] * 3 + [-1] * 6], (10, 4): [[1] * 5 + [-1] * 5]}.get((n, r), [D])
    return {nf(x) for x in c}

def main():
    out, fails = [], []
    for n in range(2, 8):
        B = HMAX[n - 1]
        subs = {k: list(combinations(range(n), k)) for k in range(1, n)}
        best = {k: None for k in range(1, n)}
        mins = {k: set() for k in range(1, n)}
        for v in combinations_with_replacement(range(-B, B + 1), n):
            if sum(v) != 0 or not any(v) or reduce(gcd, (abs(t) for t in v)) != 1:
                continue
            for k in range(1, n):
                s = sum(1 for S in subs[k] if sum(v[i] for i in S) != 0)
                if best[k] is None or s < best[k]:
                    best[k], mins[k] = s, {nf(v)}
                elif s == best[k]:
                    mins[k].add(nf(v))
        for k in range(1, n):
            ok = best[k] == formula(n, k) and mins[k] == listed(n, k)
            out.append(dict(n=n, k=k, box=B, minimum=best[k], formula=formula(n, k),
                            minimisers=sorted(mins[k]), ok=ok))
            if not ok:
                fails.append((n, k))
    res = dict(script="verify_small_complete.py", cases=out, failures=fails, passed=not fails)
    path = sys.argv[1] if len(sys.argv) > 1 else "verification_small_complete.json"
    with open(path, "w") as fh:
        json.dump(res, fh, indent=1)
    print("passed" if not fails else f"FAILED {fails}", len(out), "parameter pairs")
    if fails:
        sys.exit(1)

if __name__ == "__main__":
    main()
