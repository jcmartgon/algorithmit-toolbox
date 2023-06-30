# Jesus Carlos Martinez Gonzalez
# 25/06/23
# Maximum Value of the Loot

"""
Maximizing the Value of the Loot Problem.
Find the maximal value of items that fit into the backpack.
"""


def main():
    n, w = map(int, input().split())
    spices = []
    for _ in range(n):
        cost, weight = map(int, input().split())
        spices.append((cost, weight))
    print(
        f"{max_value(sorted(spices, key=lambda x: x[0] / x[1], reverse=True), w):.4f}"
    )


def max_value(spices, w):
    total_value = 0
    for cost, weight in spices:
        if w >= weight:
            total_value += cost
            w -= weight
        else:
            total_value += (w / weight) * cost
            break
    return total_value


if __name__ == "__main__":
    main()
