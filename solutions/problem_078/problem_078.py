"""Problem 78: Coin partitions."""


def generalized_pentagonal(index: int) -> int:
    k = (index + 1) // 2
    if index % 2 == 0:
        k = -k
    return k * (3 * k - 1) // 2


def solve(divisor: int = 1_000_000) -> int:
    partitions = [1]
    n = 1

    while True:
        total = 0
        index = 1

        while True:
            pentagonal = generalized_pentagonal(index)
            if pentagonal > n:
                break

            sign = 1 if (index - 1) // 2 % 2 == 0 else -1
            total += sign * partitions[n - pentagonal]
            index += 1

        total %= divisor
        partitions.append(total)

        if total == 0:
            return n

        n += 1


if __name__ == "__main__":
    print(solve())
