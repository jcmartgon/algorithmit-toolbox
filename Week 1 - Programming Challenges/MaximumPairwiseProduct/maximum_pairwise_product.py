# Jesus Carlos Martinez Gonzalez
# 08/06/23
# Maximum Pairwise Product


def main():
    n = int(input())
    seq = list(map(int, input().split()))

    print(max_pairwise_product(seq))


def max_pairwise_product(lst):
    """Returns maximum pairwise product from lst"""
    lst = sorted(lst)
    return lst[-1] * lst[-2]


if __name__ == "__main__":
    main()
