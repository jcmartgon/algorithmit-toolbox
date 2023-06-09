# Jesus Carlos Martinez Gonzalez
# 08/06/23
# Test maximum pairwise product

from maximum_pairwise_product import (
    max_pairwise_product_sorted,
    max_pairwise_product_naive,
    max_pairwise_product_faster,
)
import random

lst = []
for _ in range(10000):
    lst.append(random.randint(0, 10000))

naive = max_pairwise_product_naive(lst)


def test_max_pairwise_product__sortedordered():
    assert max_pairwise_product_sorted([1, 2, 3]) == 6
    assert max_pairwise_product_sorted([3, 3, 3]) == 9
    assert max_pairwise_product_sorted([0, 1]) == 0


def test_max_pairwise_product_sorted_reversed():
    assert max_pairwise_product_sorted([3, 2, 1]) == 6


def test_max_pairwise_product_naive_ordered():
    assert max_pairwise_product_naive([1, 2, 3]) == 6
    assert max_pairwise_product_naive([3, 3, 3]) == 9
    assert max_pairwise_product_naive([0, 1]) == 0


def test_max_pairwise_product_naive_reversed():
    assert max_pairwise_product_naive([3, 2, 1]) == 6


def test_max_pairwise_product_faster_ordered():
    assert max_pairwise_product_faster([1, 2, 3]) == 6
    assert max_pairwise_product_faster([3, 3, 3]) == 9
    assert max_pairwise_product_faster([0, 1]) == 0


def test_max_pairwise_product_faster_reversed():
    assert max_pairwise_product_faster([3, 2, 1]) == 6


def test_stress_sorted():
    assert max_pairwise_product_sorted(lst) == naive


def test_stress_faster():
    assert max_pairwise_product_faster(lst) == naive
