# Jesus Carlos Martinez Gonzalez
# 25/06/23
# Money Change

"""
Compute the minimum number of coins needed
to change the given value into coins with denominations 1, 5, and 10.
"""


def main():
    denominations = [10, 5, 1]

    money = int(input())

    print(change(money, denominations))


def change(money, denominations):
    coins = 0

    for denomination in denominations:
        coins += money // denomination
        money %= denomination

    return coins


if __name__ == "__main__":
    main()
