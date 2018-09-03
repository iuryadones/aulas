#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from statistics import mean
from statistics import median
from statistics import variance
from statistics import stdev

from time import time

import mods


def cronometer(func):
    def running():
        num = 30

        _r = []
        for _ in range(num):
            init = time()
            func()
            end = time()
            _r.append(end - init)

        print(end="\n")
        print(f"function: {func.__name__}")
        print(f"iterations: {num}")
        print(f"time mean: {mean(_r):2.4e}")
        print(f"time median: {median(_r):2.4e}")
        print(f"time stdev: {stdev(_r):2.4e}")
        print(f"time variance: {variance(_r):2.4e}")
        print(end="\n")

    return running


@cronometer
def lafunc_1():
    modules = [m for m in dir(mods) if not m.startswith("__")]
    print(getattr(mods, modules[0])("G"))


@cronometer
def func_2():
    modules = list(m for m in dir(mods) if not m.startswith("__"))
    print(getattr(mods, modules[1])("G"))


def main():
    lafunc_1()
    func_2()


if __name__ == "__main__":
    main()
