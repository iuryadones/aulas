"""
Install pytest:

```bash
$ pip install -U pytest
```

Run:

```bash
$ pytest
````
"""


def inc(x):
    return x + 1


def test_diff():
    assert inc(3) != 4


def test_equal():
    assert inc(3) == 5
