from src.sum import sum


def test_sum():
    assert sum(2, 5) == 7
    assert sum(-2, -2) == -4
    assert sum(0, 5) == 5
