"""Problem 57: Square root convergents."""


def solve(expansions: int = 1000) -> int:
    count = 0
    numerator, denominator = 3, 2

    for _ in range(expansions):
        if len(str(numerator)) > len(str(denominator)):
            count += 1
        numerator, denominator = numerator + 2 * denominator, numerator + denominator

    return count


if __name__ == "__main__":
    print(solve())
