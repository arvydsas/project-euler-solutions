"""Problem 23: Non-abundant sums."""


def divisor_sums(limit: int) -> list[int]:
    sums = [0] * (limit + 1)

    for divisor in range(1, limit // 2 + 1):
        for multiple in range(divisor * 2, limit + 1, divisor):
            sums[multiple] += divisor

    return sums


def solve(limit: int = 28_123) -> int:
    sums = divisor_sums(limit)
    abundant = [number for number in range(1, limit + 1) if sums[number] > number]
    can_be_written = [False] * (limit + 1)

    for index, first in enumerate(abundant):
        for second in abundant[index:]:
            total = first + second
            if total > limit:
                break
            can_be_written[total] = True

    return sum(number for number in range(1, limit + 1) if not can_be_written[number])


if __name__ == "__main__":
    print(solve())
