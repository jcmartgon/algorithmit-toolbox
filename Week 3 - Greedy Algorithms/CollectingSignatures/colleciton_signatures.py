# Jesus Carlos Martinez Gonzalez
# 26/06/23
# Colleciton Signatures

"""
Find the maximum dot product of two sequences of numbers.
"""


def main():
    n = int(input())
    lines = []

    for _ in range(n):
        lines.append(tuple(map(int, input().split())))

    lines = sorted(lines, key=lambda x: (x[0], x[0] - x[1]))

    points = [lines[0][1]]

    for line in lines:
        if line[0] > points[-1]:
            points.append(line[1])
        elif line[1] < points[-1]:
            points[-1] = line[1]

    print(len(points))
    print(*points)


if __name__ == "__main__":
    main()
