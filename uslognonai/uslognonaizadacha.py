# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Найти интеграл вероятности.

import math
import sys

EPS = 10 ** -10

if __name__ == '__main__':
    x = float(input("add value for x: "))
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)

    a = x
    S, n = a, 0

    while math.fabs(a) > EPS:
        a *= ((-1) * x ** 2 * (2 * n + 1)) / ((2 * n + 3) * (n + 1))
        S += a
        n += 1

    print(f"erf({x}) = {(2 / math.sqrt(math.pi)) * S}")
