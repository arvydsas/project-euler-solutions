"""Problem 64: Odd period square roots."""

from math import isqrt


def period(number: int) -> int:
    root = isqrt(number)
    if root * root == number:
        return 0

    m = 0
    d = 1
    a = root
    length = 0

    while True:
        m = d * a - m
        d = (number - m * m) // d
        a = (root + m) // d
        length += 1

        if a == 2 * root:
            return length


def solve(limit: int = 10_000) -> int:
    return sum(1 for number in range(1, limit + 1) if period(number) % 2 == 1)


if __name__ == "__main__":
    print(solve())
