#!/usr/bin/env python3
"""Independent finite checks for sharp fixed-size subset sums.

Python 3.10+; standard library only. All comparisons except the labelled
threshold approximations use integers or exact rational arithmetic.
These finite checks corroborate, and do not replace, the manuscript proofs.
Run: python verify.py --output verification.json
"""

from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import comb, gcd
from functools import reduce
from pathlib import Path
import argparse
import json
import platform
import time


def require(condition, detail):
    if not condition:
        raise RuntimeError(detail)


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def masses(n, i, k):
    return [choose(i, j) * choose(n - i, k - j) for j in range(k + 1)]


def majorized(left, right):
    length = max(len(left), len(right))
    a = sorted(left, reverse=True) + [0] * (length - len(left))
    b = sorted(right, reverse=True) + [0] * (length - len(right))
    sa = sb = 0
    for x, y in zip(a, b):
        sa += x
        sb += y
        if sa > sb:
            return False
    return sa == sb


def support_formula(n, k):
    r = min(k, n - k)
    if r == 1:
        return 2
    if n == 2 * r:
        return 2 * comb(n - 2, r - 2)
    exceptions = {(6, 2): 6, (9, 3): 39, (10, 4): 110}
    return exceptions.get((n, r), 2 * comb(n - 2, r - 1))


def normal_form(values):
    divisor = reduce(gcd, (abs(x) for x in values))
    require(divisor > 0, "Zero vector has no projective normal form")
    p = tuple(sorted(x // divisor for x in values))
    q = tuple(sorted(-x // divisor for x in values))
    return min(p, q)


def extremisers(n, k):
    r = min(k, n - k)
    difference = [1, -1] + [0] * (n - 2)
    if r == 1:
        candidates = [difference]
    elif n == 2 * r:
        candidates = [[r - 1] * 2 + [-1] * (n - 2)]
    elif (n, r) == (5, 2):
        candidates = [difference, [1, 1, -1, -1, 0]]
    elif (n, r) == (6, 2):
        candidates = [[1] * 3 + [-1] * 3]
    elif (n, r) == (8, 2):
        candidates = [difference, [1] * 4 + [-1] * 4]
    elif (n, r) == (9, 3):
        candidates = [[2] * 3 + [-1] * 6]
    elif (n, r) == (10, 4):
        candidates = [[1] * 5 + [-1] * 5]
    else:
        candidates = [difference]
    return {normal_form(x) for x in candidates}


def subset_sum_counts(values, k):
    return Counter(sum(values[i] for i in indices)
                   for indices in combinations(range(len(values)), k))


def check_support_grid():
    populations = laws = equality_cases = 0
    for n in range(2, 11):
        for values in combinations_with_replacement(range(-2, 3), n):
            if sum(values) != 0 or all(x == 0 for x in values):
                continue
            populations += 1
            for k in range(1, n):
                counts = subset_sum_counts(values, k)
                support = comb(n, k) - counts.get(0, 0)
                target = support_formula(n, k)
                require(support >= target, ("support", values, k, support, target))
                if support == target:
                    require(normal_form(values) in extremisers(n, k),
                            ("unlisted equality", values, k))
                    equality_cases += 1
                laws += 1
        # Check attainment independently, including patterns outside the grid.
        for k in range(1, n):
            for values in extremisers(n, k):
                counts = subset_sum_counts(values, k)
                require(comb(n, k) - counts.get(0, 0) == support_formula(n, k),
                        ("construction", n, k, values))
    return dict(n_range=[2, 10], integer_alphabet=list(range(-2, 3)),
                zero_sum_populations=populations, slice_laws=laws,
                equality_cases=equality_cases,
                scope="All nondecreasing vectors on this finite grid; all k. Permutations preserve the counts.")


def check_hypergeometric_atoms():
    laws = atoms = equalities = 0
    for n in range(3, 61):
        for k in range(1, (n - 1) // 2 + 1):
            target = comb(n - 1, k)
            for i in range(1, n):
                weights = masses(n, i, k)
                require(sum(weights) == comb(n, k), ("Vandermonde", n, i, k))
                for j, weight in enumerate(weights):
                    expected = (i, j) in {(1, 0), (n - 1, k)}
                    if n == 2 * k + 1:
                        expected |= (i, j) in {(2, 1), (n - 2, k - 1)}
                    require(weight <= target, ("atom", n, i, k, j))
                    require((weight == target) == expected,
                            ("atom equality", n, i, k, j, weight, target))
                    equalities += weight == target
                    atoms += 1
                laws += 1
    return dict(n_max=60, hypergeometric_laws=laws, atom_comparisons=atoms,
                classified_equalities=equalities)


def check_parity_majorization():
    comparisons = proper = reflections = 0
    for m in range(2, 101):
        for t in range(1, m):
            before, after = masses(2 * m, t, m), masses(2 * m, t + 2, m)
            require(majorized(after, before), ("parity", m, t))
            equal = sorted(before) == sorted(after)
            require(equal == (t == m - 1), ("parity strictness", m, t))
            proper += not equal
            reflections += equal
            comparisons += 1
    return dict(m_max=100, comparisons=comparisons,
                proper_comparisons=proper, reflection_equalities=reflections)


def check_entropy_grid():
    laws = powers = equalities = chain_comparisons = 0
    orders = (2, 3, 5)
    for n in range(2, 11):
        for values in combinations_with_replacement(range(4), n):
            if values[0] == values[-1]:
                continue
            for k in range(1, n):
                counts = list(subset_sum_counts(values, k).values())
                denominator = comb(n, k)
                # Independently verify every strict-gap chain majorization.
                for i in range(1, n):
                    if values[i - 1] < values[i]:
                        require(majorized(counts, masses(n, i, k)),
                                ("population majorization", values, k, i))
                        chain_comparisons += 1
                for alpha in orders:
                    actual = Fraction(sum(c ** alpha for c in counts), denominator ** alpha)
                    b = Fraction((n - k) ** alpha + k ** alpha, n ** alpha)
                    q = None
                    if n == 2 * k and n >= 4:
                        q = Fraction((2 * k) ** alpha + 2 * (k - 1) ** alpha,
                                     (2 * (2 * k - 1)) ** alpha)
                    target = max(b, q) if q is not None else b
                    require(actual <= target, ("entropy", values, k, alpha))
                    if actual == target:
                        multiplicities = sorted(Counter(values).values())
                        allowed = []
                        if b == target:
                            allowed.append(sorted([1, n - 1]))
                        if q == target:
                            allowed.append(sorted([2, n - 2]))
                        require(multiplicities in allowed,
                                ("entropy equality", values, k, alpha, allowed))
                        equalities += 1
                    powers += 1
                laws += 1
    return dict(n_range=[2, 10], integer_alphabet=list(range(4)),
                slice_laws=laws, entropy_orders=list(orders),
                exact_power_sum_comparisons=powers, classified_equalities=equalities,
                strict_gap_majorization_comparisons=chain_comparisons)


def threshold(m):
    if m == 2:
        return Decimal(2)
    with localcontext() as context:
        context.prec = 75
        a = Decimal(2 * m) / (2 * m - 1)
        b = Decimal(m - 1) / (2 * m - 1)
        def f(x):
            return (x * a.ln()).exp() / 2 + (x * b.ln()).exp() - 1
        lo, hi = Decimal(2), Decimal(4)
        require(f(lo) < 0, ("threshold lower bracket", m))
        while f(hi) < 0:
            hi *= 2
        for _ in range(210):
            mid = (lo + hi) / 2
            if f(mid) > 0:
                hi = mid
            else:
                lo = mid
        return +(lo + hi) / 2


def check_examples():
    values = (-1, -1, 1, 1)
    counts = subset_sum_counts(values, 2)
    cube_sum = sum(Fraction(c, 6) ** 3 for c in counts.values())
    require(cube_sum == Fraction(11, 36) > Fraction(1, 4), "Negative control failed")
    five = subset_sum_counts((-1, -1, 0, 1, 1), 2)
    require(five[0] == 4 and sum(five.values()) == 10,
            "Missing published equality-case example failed")
    thresholds = {str(m): str(threshold(m)) for m in (2, 3, 4, 5, 10, 50)}
    approximations = list(map(Decimal, thresholds.values()))
    require(all(a < b for a, b in zip(approximations, approximations[1:])),
            "Sampled thresholds failed monotonicity")
    return dict(negative_control=dict(n=4, k=2, order=3, power_sum=str(cube_sum),
                bernoulli_power_sum="1/4", expected_universal_claim="fails"),
                omitted_equality_example=dict(n=5, k=2, zero_sums=4, support=6),
                threshold_decimal_approximations=thresholds,
                threshold_method="75-digit Decimal bisection; approximations, not interval certificates")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="verification.json")
    args = parser.parse_args()
    start = time.perf_counter()
    result = dict(status="PASS", python=platform.python_version(),
                  arithmetic="Integers and Fraction, except labelled Decimal threshold approximations",
                  finite_checks_are_not_proofs=True, checks={})
    for name, function in [("support_grid", check_support_grid),
                           ("hypergeometric_atoms", check_hypergeometric_atoms),
                           ("parity_majorization", check_parity_majorization),
                           ("entropy_grid", check_entropy_grid),
                           ("examples", check_examples)]:
        result["checks"][name] = function()
        print(name + ": PASS", flush=True)
    result["elapsed_seconds"] = round(time.perf_counter() - start, 3)
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("All checks passed; results written to " + args.output)


if __name__ == "__main__":
    main()
