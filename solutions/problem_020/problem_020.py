"""Problem 20: Factorial digit sum."""

from math import factorial


def solve(number: int = 100) -> int:
    return sum(int(digit) for digit in str(factorial(number)))


if __name__ == "__main__":
    print(solve())
