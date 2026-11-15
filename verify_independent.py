"""Exact, finite corroboration of the proof audit. No third-party packages.

Run with Python 3. These checks are not substitutes for the unrestricted proofs.
"""



def require(condition, detail=None):
    """Explicit check that also runs under python -O."""
    if not condition:
        raise RuntimeError(f"verification failed: {detail!r}")

from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import comb
import json
import random


def independent_weight(weights):
    old, new = 0, 0
    for weight in weights:
        old, new = new, max(new, old + weight)
    return new


def johnson_mean_audit():
    count = 0
    cases = {1: 0, 2: 0}
    worst = None
    for n in range(11, 301):
        for k in range(5, (n - 1) // 2 + 1):
            target = Fraction(n * (n - 1) - 2 * k * (n - k), n * (n - 1))
            for i in range(1, n // 2 + 1):
                if i * k % n:
                    continue
                j = i * k // n
                a, b, c, d = j, i - j, k - j, n - i - k + j
                require(min(a, b, c, d) > 0)
                require(a <= c and a < b and c < d and a * d == b * c)
                atom = Fraction(comb(i, j) * comb(n - i, k - j), comb(n, k))
                require(atom < target, ((n, k, i, atom, target)))
                r_minus = Fraction(a * d, (b + 1) * (c + 1))
                r_plus = Fraction(b * c, (a + 1) * (d + 1))
                if a == 1:
                    require(r_minus >= Fraction(8, 15) and r_plus >= Fraction(4, 9))
                    require(atom <= Fraction(45, 89) < Fraction(11, 21) <= target)
                    cases[1] += 1
                else:
                    r_mm = Fraction(a * (a - 1) * d * (d - 1),
                                    (b + 1) * (b + 2) * (c + 1) * (c + 2))
                    r_pp = Fraction(b * (b - 1) * c * (c - 1),
                                    (a + 1) * (a + 2) * (d + 1) * (d + 2))
                    require(r_minus >= Fraction(9, 16) and r_plus >= Fraction(8, 15))
                    require(r_mm >= Fraction(243, 3200) > Fraction(1, 16))
                    require(r_pp >= Fraction(32, 405) > Fraction(1, 16))
                    require(atom < Fraction(240, 533) < Fraction(5, 11) <= target)
                    cases[2] += 1
                if worst is None or target - atom < worst[0]:
                    worst = (target - atom, n, k, i, atom, target)
                count += 1
    return dict(n_max=300, integer_mean_cases=count,
                a1_cases=cases[1], a_ge_2_cases=cases[2],
                minimum_gap=str(worst[0]), minimum_gap_parameters=worst[1:4],
                atom=str(worst[4]), target=str(worst[5]))


def unimodal_path_audit():
    rng = random.Random(681)
    count = 100_000
    for _ in range(count):
        length = rng.randrange(2, 100)
        mode = rng.randrange(length)
        left = [rng.randrange(1, 100) for _ in range(mode)]
        right = [rng.randrange(1, 100) for _ in range(length - mode - 1)]
        peak = rng.randrange(max(left + right + [1]), 101)
        weights = sorted(left) + [peak] + sorted(right, reverse=True)
        require(independent_weight(weights) == max(sum(weights[::2]), sum(weights[1::2])))
    # Include zero weights, plateaux, and every weakly unimodal sequence of
    # length at most 8 whose entries are in {0,1,2,3}. Generate by the mode.
    exhaustive = set()
    for length in range(1, 9):
        for mode in range(length):
            for peak in range(4):
                for left in combinations_with_replacement(range(peak + 1), mode):
                    for right in combinations_with_replacement(range(peak + 1), length - mode - 1):
                        exhaustive.add(left + (peak,) + right[::-1])
    for weights in exhaustive:
        require(independent_weight(weights) == max(sum(weights[::2]), sum(weights[1::2])))
    return dict(random_positive_cases=count, random_seed=681,
                exhaustive_weakly_unimodal_cases=len(exhaustive),
                exhaustive_max_length=8, exhaustive_alphabet=[0, 1, 2, 3])


def hypergeometric_modular_audit():
    laws = periods = 0
    for n in range(2, 81):
        for k in range(1, n // 2 + 1):
            denominator = comb(n, k)
            # i and n-i have the same atom and modular maxima.
            for i in range(1, n // 2 + 1):
                lo, hi = max(0, k - n + i), min(i, k)
                weights = [comb(i, j) * comb(n - i, k - j) for j in range(lo, hi + 1)]
                require(sum(weights) == denominator)
                parity = max(sum(weights[::2]), sum(weights[1::2]))
                require(independent_weight(weights) == parity)
                if n == 2 and k == 1:
                    require(2 * parity <= denominator)
                elif n == 2 * k:
                    require(parity * (n - 1) <= k * denominator)
                else:
                    require(parity * n <= (n - k) * denominator)
                # Period greater than the support span only yields singletons.
                for period in range(2, len(weights) + 1):
                    residues = [0] * period
                    for j, weight in enumerate(weights, lo):
                        residues[j % period] += weight
                    require(max(residues) <= parity)
                    periods += 1
                laws += 1
    return dict(n_max=80, hypergeometric_laws=laws, modular_periods=periods)


def finite_group_audit():
    laws = 0
    groups = [(f'Z{m}', m, lambda a, b, modulus=m: (a + b) % modulus)
              for m in range(2, 7)]
    groups.append(('Z2xZ2', 4, lambda a, b: a ^ b))
    for name, order, add in groups:
        for n in range(2, 9):
            for coefficients in combinations_with_replacement(range(order), n):
                if coefficients[0] == coefficients[-1]:
                    continue
                for k in range(1, n // 2 + 1):
                    values = Counter()
                    for subset in combinations(range(n), k):
                        value = 0
                        for index in subset:
                            value = add(value, coefficients[index])
                        values[value] += 1
                    denominator = comb(n, k)
                    largest = max(values.values())
                    if n == 2 and k == 1:
                        require(2 * largest <= denominator)
                    elif n == 2 * k:
                        require(largest * (n - 1) <= k * denominator)
                    else:
                        require(largest * n <= (n - k) * denominator)
                    laws += 1
    return dict(n_max=8, groups=[item[0] for item in groups], coefficient_slice_laws=laws)


if __name__ == '__main__':
    for name, function in [
        ('johnson_mean', johnson_mean_audit),
        ('unimodal_path', unimodal_path_audit),
        ('hypergeometric_modular', hypergeometric_modular_audit),
        ('finite_group', finite_group_audit),
    ]:
        print(json.dumps({'check': name, 'result': function()}, sort_keys=True), flush=True)
