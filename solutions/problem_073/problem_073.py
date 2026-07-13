"""Problem 73: Counting fractions in a range."""

from math import gcd


def solve(limit: int = 12_000) -> int:
    total = 0

    for denominator in range(2, limit + 1):
        for numerator in range(denominator // 3 + 1, (denominator - 1) // 2 + 1):
            if gcd(numerator, denominator) == 1:
                total += 1

    return total


if __name__ == "__main__":
    print(solve())
