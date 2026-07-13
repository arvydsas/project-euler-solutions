"""Problem 76: Counting summations."""


def solve(total: int = 100) -> int:
    ways = [0] * (total + 1)
    ways[0] = 1

    for part in range(1, total):
        for amount in range(part, total + 1):
            ways[amount] += ways[amount - part]

    return ways[total]


if __name__ == "__main__":
    print(solve())
