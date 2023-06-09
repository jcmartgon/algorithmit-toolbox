# Jesus Carlos Martinez Gonzalez
# 08/06/23
# Maximum Pairwise Product


def main():
    n = int(input())
    seq = list(map(int, input().split()))

    print(max_pairwise_product_sorted(seq))
    print(max_pairwise_product_naive(seq))
    print(max_pairwise_product_faster(seq))


def max_pairwise_product_sorted(lst):
    """Returns maximum pairwise product from lst"""
    lst = sorted(lst)
    return lst[-1] * lst[-2]


# O(n^2)
def max_pairwise_product_naive(lst):
    """Returns maximum pairwise product from lst"""
    l = len(lst)
    max_product = 0

    for i in range(l):
        for j in range(i + 1, l):
            curr_product = lst[i] * lst[j]
            if curr_product > max_product:
                max_product = curr_product

    return max_product


# O(n)
def max_pairwise_product_faster(lst):
    """Returns maximum pairwise product from lst"""
    tmp = [0, 0, 0, 0]
    for i, val in enumerate(lst):
        if val > tmp[0]:
            tmp[0] = val
            tmp[1] = i
    for i, val in enumerate(lst):
        if val > tmp[2] and i != tmp[1]:
            tmp[2] = val

    return tmp[0] * tmp[2]


if __name__ == "__main__":
    main()
