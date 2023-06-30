# Jesus Carlos Martinez Gonzalez
# 27/06/23
# Maximum Salary

"""
Find the maximum dot product of two sequences of numbers.
"""


def main():
    n = int(input())

    ints = "".join(input().split())
    ints = sorted(ints, key=lambda x: int(x), reverse=True)
    print("".join(ints))


if __name__ == "__main__":
    main()
