"""Problem 2: Even Fibonacci numbers."""


def solve(limit: int = 4_000_000) -> int:
    total = 0
    a, b = 1, 2

    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b

    return total


if __name__ == "__main__":
    print(solve())
