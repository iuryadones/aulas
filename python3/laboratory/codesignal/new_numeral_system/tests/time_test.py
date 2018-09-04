#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import mods
from decoretors import cronometer

import pytest


@cronometer
def test_getattr():
    modules = [m for m in dir(mods) if not m.startswith("__")]

    for module in modules:
        getattr(mods, module)("G")


@cronometer
def test_exec():
    modules = [m for m in dir(mods) if not m.startswith("__")]

    for module in modules:
        exec(f"{mods.__name__}.{module}('G')")


@cronometer
def test_eval():
    modules = [m for m in dir(mods) if not m.startswith("__")]

    for module in modules:
        eval(f"{mods.__name__}.{module}('G')")


def main():
    _map = map(lambda k: globals()[k] if "test_" in k else None, globals())
    _filter = filter(lambda f: f if f is not None else None, _map)

    for func in _filter:
        func()


if __name__ == "__main__":
    main()
    pytest.main([__file__])
