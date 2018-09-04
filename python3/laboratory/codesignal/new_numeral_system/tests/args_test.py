#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from consts import cargs
import mods

import pytest


def test_args():

    modules = (m for m in dir(mods) if not m.startswith("__"))

    for module in modules:
        for args, ex in cargs:
            assert getattr(mods, module)(args) == ex


if __name__ == "__main__":
    pytest.main([__file__])
