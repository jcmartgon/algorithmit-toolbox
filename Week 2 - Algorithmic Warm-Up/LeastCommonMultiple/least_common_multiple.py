# Jesus Carlos Martinez Gonzalez
# 10/06/23
# Least common multiple


def main():
    a, b = map(int, input().split())
    print(int(lcm(a, b)))
    # print(int(lcm_naive(a, b)))


def lcm(a, b):
    if b > a:
        a, b = b, a
    return a * b / gcd(a, b)


def lcm_naive(a, b):
    if b > a:
        a, b = b, a
    c = a
    while True:
        if c % a == 0 and c % b == 0:
            break
        c += 1
    return c


def gcd(a, b):
    """Returns the greatest common denominator for a and b"""
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    main()
