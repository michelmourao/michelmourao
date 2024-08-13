from app.math import Math
import pytest

# def test_sum_positive():
#     assert Math.sum(1, 2) == 3

# def test_sum_negative():
#     assert Math.sum(-1, -2) == -3

@pytest.mark.parametrize("v1, v2, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2),
    (1.5, 1.5, 3),
])

def test_sum(v1, v2, expected):
    result =  Math.sum(v1, v2)
    assert result == expected, f'Using v1={v1} and v2={v2} expected {expected}, but got {result}'