# Jesus Carlos Martinez Gonzalez
# 25/06/23
# Maximum Advertisement Revenue

"""
Find the maximum dot product of two sequences of numbers.
"""


def main():
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    print(max_cross(sorted(prices), sorted(clicks), n))


def max_cross(a, b, n):
    total = 0
    for i in range(n):
        total += a[i] * b[i]
    return total


if __name__ == "__main__":
    main()
