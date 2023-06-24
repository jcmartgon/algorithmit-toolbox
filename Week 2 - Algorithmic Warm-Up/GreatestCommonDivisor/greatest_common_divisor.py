# Jesus Carlos Martinez Gonzalez
# 10/06/23
# Greatest Common Divisor


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))
    # print(gcd_naive(a, b))


def gcd(a, b):
    """Returns the greatest common denominator for a and b"""
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def gcd_naive(a, b):
    """Returns the greatest common denominator for a and b"""
    if b > a:
        a, b = b, a
    c = b
    while True:
        if a % c == 0 and b % c == 0:
            break
        c -= 1
    return c


if __name__ == "__main__":
    main()
