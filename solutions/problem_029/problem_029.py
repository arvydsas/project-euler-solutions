"""Problem 29: Distinct powers."""


def solve(limit: int = 100) -> int:
    return len({base**exponent for base in range(2, limit + 1) for exponent in range(2, limit + 1)})


if __name__ == "__main__":
    print(solve())
