# Jesus Carlos Martinez Gonzalez
# 10/06/23
# Huge Fibonacci Number


def main():
    n, m = map(int, input().split())
    print(fibonacci_doubling(n) % m)


def fibonacci_doubling(n):
    if n == 0:
        return 0

    def fib_helper(k):
        if k == 0:
            return (0, 1)

        a, b = fib_helper(k // 2)
        c = a * ((b << 1) - a)
        d = a * a + b * b

        if k % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return fib_helper(n)[0]


if __name__ == "__main__":
    main()
