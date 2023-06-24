# Jesus Carlos Martinez Gonzalez
# 10/06/23
# Last digit of the sum of squares of fibonacci number


def main():
    n = int(input())
    print(fibonacci_doubling_sum_squares(n) % 10)


def fibonacci_doubling_sum_squares(n):
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

    fib_sum = 0
    for i in range(n + 1):
        fib_i = fib_helper(i)[0]
        fib_sum += fib_i * fib_i

    return fib_sum


if __name__ == "__main__":
    main()
