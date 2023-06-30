# Jesus Carlos Martinez Gonzalez
# 26/06/23
# Maximum number of prizes

"""
Find the maximum dot product of two sequences of numbers.
"""


def main():
    n = int(input())
    prizes = []

    for i in range(1, n + 1):
        total = sum(prizes)
        if total == n:
            break
        if total + i == n:
            prizes.append(i)
            break
        if total + i > n:
            prizes[-1] = i
            continue
        if n - (total + i) > i:
            prizes.append(i)
    print(len(prizes))
    print(*prizes)


if __name__ == "__main__":
    main()
