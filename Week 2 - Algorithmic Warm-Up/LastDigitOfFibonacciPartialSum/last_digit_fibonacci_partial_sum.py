# Jesus Carlos Martinez Gonzalez
# 10/06/23
# Last digit of fibonacci partial sum


def main():
    a, b = map(int, input().split())
    print((fibonacci_doubling_sum(b) - fibonacci_doubling_sum(a - 1)) % 10)


def fibonacci_doubling_sum(n):
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

    fib_n_plus_2 = fib_helper(n + 2)[0]
    return fib_n_plus_2 - 1


if __name__ == "__main__":
    main()
