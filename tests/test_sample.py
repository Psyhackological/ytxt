# content of test_sample.py
def func(x):
    return x + 1


def test_fails():
    assert func(3) == 5


def test_passes():
    assert func(4) == 5
