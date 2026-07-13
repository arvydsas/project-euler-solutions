"""Problem 31: Coin sums."""


def solve(total: int = 200) -> int:
    ways = [0] * (total + 1)
    ways[0] = 1

    for coin in (1, 2, 5, 10, 20, 50, 100, 200):
        for amount in range(coin, total + 1):
            ways[amount] += ways[amount - coin]

    return ways[total]


if __name__ == "__main__":
    print(solve())
