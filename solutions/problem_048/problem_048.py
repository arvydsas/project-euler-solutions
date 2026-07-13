"""Problem 48: Self powers."""


def solve(limit: int = 1000) -> int:
    return sum(pow(number, number, 10_000_000_000) for number in range(1, limit + 1)) % 10_000_000_000


if __name__ == "__main__":
    print(solve())
