"""Problem 80: Square root digital expansion."""

from decimal import Decimal, getcontext
from math import isqrt


getcontext().prec = 102


def digit_sum(number: int, digits: int = 100) -> int:
    root_digits = str(Decimal(number).sqrt()).replace(".", "")[:digits]
    return sum(int(digit) for digit in root_digits)


def solve(limit: int = 100) -> int:
    return sum(
        digit_sum(number)
        for number in range(1, limit)
        if isqrt(number) ** 2 != number
    )


if __name__ == "__main__":
    print(solve())
