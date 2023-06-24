# Jesus Carlos Martinez Gonzalez
# 09/06/23
# Fibonacci Number


def main():
    n = int(input())
    # print(fibonacci_naive(n))
    # print(fibonacci_memoization(n))
    # print(fibonacci_iterative(n))
    print(fibonacci_doubling(n))


def fibonacci_naive(n):
    """Returns the nth element of the fibonacci sequence"""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_memoization(n, memo={}):
    """Returns the nth element of the fibonacci sequence"""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


def fibonacci_iterative(n):
    if n <= 1:
        return n

    a = b = 1

    for _ in range(2, n):
        a, b = b, a + b

    return b


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
