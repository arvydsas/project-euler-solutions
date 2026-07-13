"""Problem 69: Totient maximum."""


def solve(limit: int = 1_000_000) -> int:
    result = 1

    for prime in (2, 3, 5, 7, 11, 13, 17, 19):
        if result * prime > limit:
            return result
        result *= prime

    return result


if __name__ == "__main__":
    print(solve())
