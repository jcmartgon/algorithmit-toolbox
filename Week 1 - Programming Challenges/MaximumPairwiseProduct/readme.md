# Maximum Pairwise Product

## Problem Description

In this programming challenge, your goal is to implement a program that works in less than one second even on huge datasets.

## My solution

#### sum_two_digits.py

```python
def main():
    n = int(input())
    seq = list(map(int, input().split()))

    print(max_pairwise_product(seq))


def max_pairwise_product(lst):
    """Returns maximum pairwise product from lst"""
    lst = sorted(lst)
    return lst[-1] * lst[-2]


if __name__ == "__main__":
    main()
```

## Tests

![All passed](./resources/tests.png)

## Score

![All good](./resources/score.png)

## Usage

1. Run 'python maximum_pairwise_product.py' on your command-line.
2. Input n.
3. Input n int numbers separated by whitespace.