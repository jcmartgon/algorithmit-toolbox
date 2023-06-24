# Jesus Carlos Martinez Gonzalez
# 09/06/23
# Last digit from fibonacci number


def main():
    n = int(input())
    print(fibonacci_doubling(n) % 10)


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
