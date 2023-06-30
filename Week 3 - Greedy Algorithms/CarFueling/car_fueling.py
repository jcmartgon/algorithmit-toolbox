# Jesus Carlos Martinez Gonzalez
# 25/06/23
# Car Fueling

"""
Compute the minimum number of gas tank refills to get from one city to another.
"""


def main():
    distance = int(input())
    capacity = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    print(min_stops(distance, capacity, n, stops))


def min_stops(distance, capacity, n, stops):
    count = 0
    traversed = 0
    fuel = capacity

    for i in range(n):
        if i == n - 1:
            if fuel + traversed >= distance:
                continue
            if capacity + traversed >= distance:
                count += 1
                continue
            else:
                return -1
        if fuel + traversed >= stops[i + 1]:
            fuel -= stops[i]
            traversed = stops[i]
            continue
        if capacity + traversed >= stops[i + 1]:
            traversed = stops[i]
            fuel = capacity
            count += 1
        else:
            return -1

    return count


if __name__ == "__main__":
    main()
