import pytest

def test_convert_weight():
    from dependency import convert_weight
    answer = convert_weight()
    assert pytest.approx(9.0703, 0.01) == answer
