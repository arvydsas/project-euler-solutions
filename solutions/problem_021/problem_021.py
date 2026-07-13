"""Problem 21: Amicable numbers."""


def divisor_sums(limit: int) -> list[int]:
    sums = [0] * limit

    for divisor in range(1, limit // 2 + 1):
        for multiple in range(divisor * 2, limit, divisor):
            sums[multiple] += divisor

    return sums


def solve(limit: int = 10_000) -> int:
    sums = divisor_sums(limit)
    total = 0

    for number in range(2, limit):
        partner = sums[number]
        if partner < limit and partner != number and sums[partner] == number:
            total += number

    return total


if __name__ == "__main__":
    print(solve())
