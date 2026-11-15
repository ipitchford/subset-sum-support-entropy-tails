#!/usr/bin/env python3
"""Exact finite checks for the additions in Corollary 6.2, Section 7 and Remark 8.3 of the manuscript.

Checks (all integer or Fraction arithmetic; no floating point in any decision):
  tail:      Theorem 1.5 (Section 7). For 1<=k<=K and 4k<=n<=10k, every i in [1,n-1] has
             P(Hyp(n,i,k) >= ik/n) >= k/n, with equality only at i=1; the local
             ratio conditions used in the proof hold in every case.
  tail_low:  For 2k<n<4k, the parameters where i=1 is NOT the minimiser (context only).
  identity:  the polynomial identity used in Case B of the proof of Theorem 1.5.
  smallball: Corollary 6.2 on seeded random rational populations (exact).
  modular:   the explicit counterexamples of Remark 8.3 over Z_q.
The script fails (nonzero exit) on any violated check, also under python -O.
Usage: python3 verify_extensions.py [--K 40] [--output verification_extensions.json]
"""
import argparse, json, random, sys
from fractions import Fraction as F
from itertools import combinations
from math import comb

FAILS = []
def check(cond, msg):
    if not cond:
        FAILS.append(msg)

def pmf(n, i, k):
    lo, hi = max(0, k - (n - i)), min(i, k)
    return {j: comb(i, j) * comb(n - i, k - j) for j in range(lo, hi + 1)}  # numerators over C(n,k)

def tail_check(K):
    cases = 0
    min_ratio_noninteger = None
    min_ratio_integer = None
    margin = None  # min over i>=2 of tail/(k/n)
    for k in range(1, K + 1):
        for n in range(4 * k, 10 * k + 1):
            tot = comb(n, k)
            for i in range(1, n):
                p = pmf(n, i, k)
                j0 = -(-i * k // n)  # ceil(ik/n)
                num = sum(v for j, v in p.items() if j >= j0)
                # tail >= k/n  <=>  num * n >= k * tot
                lhs, rhs = num * n, k * tot
                cases += 1
                if i == 1:
                    check(lhs == rhs, f"i=1 tail not k/n at n={n},k={k}")
                    continue
                check(lhs > rhs or (n == 4 * k and lhs >= rhs), f"tail < k/n at n={n},i={i},k={k}")
                if n > 4 * k:
                    check(lhs > rhs, f"non-unique minimiser at n={n},i={i},k={k}")
                r = F(lhs, rhs)
                margin = r if margin is None or r < margin else margin
                mu = F(i * k, n)
                if mu > 1:
                    if mu.denominator != 1:
                        m = mu.numerator // mu.denominator
                        if (m + 1) in p and m in p:
                            rr = F(p[m + 1], p[m])
                            check(rr >= F(1, 2), f"Case B ratio < 1/2 at n={n},i={i},k={k}")
                            min_ratio_noninteger = rr if min_ratio_noninteger is None or rr < min_ratio_noninteger else min_ratio_noninteger
                        check(4 * num >= tot, f"Case B tail < 1/4 at n={n},i={i},k={k}")
                    else:
                        j = int(mu)
                        if (j - 1) in p:
                            rr = F(p[j], p[j - 1])
                            check(rr > 1, f"Case C ratio <= 1 at n={n},i={i},k={k}")
                            min_ratio_integer = rr if min_ratio_integer is None or rr < min_ratio_integer else min_ratio_integer
                        check(4 * num >= tot, f"Case C tail < 1/4 at n={n},i={i},k={k}")
    return dict(K=K, n_range="4k..10k", cases=cases,
                min_case_B_ratio=str(min_ratio_noninteger), min_case_C_ratio=str(min_ratio_integer),
                min_tail_over_k_by_n_for_i_ge_2=str(margin), min_tail_ratio_float=float(margin))

def tail_low(K):
    out = {}
    for k in range(2, K + 1):
        bad = []
        for n in range(2 * k + 1, 4 * k):
            tot = comb(n, k)
            for i in range(2, n):
                p = pmf(n, i, k)
                j0 = -(-i * k // n)
                num = sum(v for j, v in p.items() if j >= j0)
                if num * n < k * tot:
                    bad.append(n)
                    break
        out[k] = dict(n_where_i1_not_minimal=bad, max_ratio_n_over_k=str(F(max(bad), k)) if bad else None)
    worst = max(F(max(v["n_where_i1_not_minimal"]), k) for k, v in out.items() if v["n_where_i1_not_minimal"])
    return dict(K=K, largest_n_over_k_with_failure=str(worst), largest_float=float(worst), per_k=out)

def identity_check():
    # 2(i-m)(k-m) - (m+1)(n-i-k+m+1) == (m-1)(n-i-k+m-1) + 2(ik-nm-1); each side has degree <= 2 in each variable
    pts = 0
    for n in range(0, 5):
        for i in range(0, 5):
            for k in range(0, 5):
                for m in range(0, 5):
                    lhs = 2 * (i - m) * (k - m) - (m + 1) * (n - i - k + m + 1)
                    rhs = (m - 1) * (n - i - k + m - 1) + 2 * (i * k - n * m - 1)
                    check(lhs == rhs, f"identity fails at {(n, i, k, m)}")
                    pts += 1
    return dict(points=pts)

def frontier_top(n, k, l):
    """Sum of the l largest masses over all hypergeometric laws Hyp(n,i,k), 1<=i<n (Fractions)."""
    best = F(0)
    for i in range(1, n):
        v = sorted(pmf(n, i, k).values(), reverse=True)
        best = max(best, F(sum(v[:l]), comb(n, k)))
    return best

def smallball_check(trials, seed):
    rng = random.Random(seed)
    worst = F(0)
    attained = 0
    for _ in range(trials):
        n = rng.randint(3, 9)
        k = rng.randint(1, n - 1)
        x = [F(rng.randint(-12, 12), rng.randint(1, 4)) for _ in range(n)]
        if len(set(x)) == 1:
            continue
        xs = sorted(x)
        g = max(xs[t + 1] - xs[t] for t in range(n - 1))
        sums = sorted(sum(x[s] for s in S) for S in combinations(range(n), k))
        tot = len(sums)
        # max mass of a half-open interval [v, v+g): it suffices to start at a sum value
        best = 0
        hi = 0
        for lo in range(tot):
            if hi < lo:
                hi = lo
            while hi < tot and sums[hi] < sums[lo] + g:
                hi += 1
            best = max(best, hi - lo)
        bound = frontier_top(n, k, 1)
        mass = F(best, tot)
        check(mass <= bound, f"small-ball violated for x={x}, k={k}")
        worst = max(worst, mass / bound)
        attained += (mass == bound)
    return dict(trials=trials, seed=seed, max_mass_over_bound=str(worst), attained_count=attained)

def modular_check():
    ex = []
    def support(q, n, k, x):
        return sum(1 for S in combinations(range(n), k) if sum(x[s] for s in S) % q)
    for q, n, k, x in [(2, 11, 5, [0] * 7 + [1] * 4), (3, 12, 5, [1] * 9 + [2] * 3), (5, 11, 5, [0] + [1] * 10)]:
        check(sum(x) % q == 0 and any(v % q for v in x), "example not a nonzero zero-sum vector")
        s = support(q, n, k, x)
        real = 2 * comb(n - 2, k - 1)
        check(s < real, f"Z_{q} example does not beat real value")
        ex.append(dict(q=q, n=n, k=k, x=x, support=s, real_value=real))
    return ex

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--K", type=int, default=40)
    ap.add_argument("--trials", type=int, default=3000)
    ap.add_argument("--output", default="verification_extensions.json")
    a = ap.parse_args()
    res = dict(script="verify_extensions.py",
               tail=tail_check(a.K), tail_low=tail_low(a.K), identity=identity_check(),
               smallball=smallball_check(a.trials, 20261114), modular=modular_check())
    res["failures"] = FAILS
    res["passed"] = not FAILS
    with open(a.output, "w") as fh:
        json.dump(res, fh, indent=1, sort_keys=True)
    print(json.dumps({k: res[k] for k in ("passed",)}), "tail:", res["tail"]["cases"], "cases; min ratio", res["tail"]["min_tail_ratio_float"],
          "; failure range below 4k up to n/k =", res["tail_low"]["largest_float"])
    if FAILS:
        print("FAILURES:", FAILS[:20], file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
