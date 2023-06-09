# Jesus Carlos Martinez Gonzalez
# 08/06/23
# Test maximum pairwise product

from maximum_pairwise_product import max_pairwise_product


def test_max_pairwise_product():
    assert max_pairwise_product([1, 2, 3]) == 6
    assert max_pairwise_product([3, 3, 3]) == 9
    assert max_pairwise_product([0, 1]) == 0
    assert max_pairwise_product([3, 2, 1]) == 6
