def add_one(x):
    return x + 1


def test_that_fails():
    assert add_one(3) == 5


def test_that_passes():
    assert add_one(4) == 5
