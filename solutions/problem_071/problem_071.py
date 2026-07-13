"""Problem 71: Ordered fractions."""


def solve(limit: int = 1_000_000) -> int:
    best_numerator = 0
    best_denominator = 1

    for denominator in range(2, limit + 1):
        numerator = (3 * denominator - 1) // 7
        if numerator * best_denominator > best_numerator * denominator:
            best_numerator = numerator
            best_denominator = denominator

    return best_numerator


if __name__ == "__main__":
    print(solve())
