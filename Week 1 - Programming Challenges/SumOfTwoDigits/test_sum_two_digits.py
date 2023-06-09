# Jesus Carlos Martinez Gonzalez
# 08/06/23
# Test sum of two digits

from sum_two_digits import sum_two_ints


def test_sum_two_ints():
    assert sum_two_ints(0, 1) == 1
    assert sum_two_ints(5, 3) == 8
    assert sum_two_ints(-5, -3) == -8
