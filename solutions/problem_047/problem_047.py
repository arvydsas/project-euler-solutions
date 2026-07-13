"""Problem 47: Distinct primes factors."""


def factor_counts(limit: int) -> list[int]:
    counts = [0] * limit

    for number in range(2, limit):
        if counts[number] == 0:
            for multiple in range(number, limit, number):
                counts[multiple] += 1

    return counts


def solve(target: int = 4) -> int:
    limit = 200_000
    counts = factor_counts(limit)
    streak = 0

    for number in range(2, limit):
        if counts[number] == target:
            streak += 1
            if streak == target:
                return number - target + 1
        else:
            streak = 0

    raise ValueError("Increase the search limit")


if __name__ == "__main__":
    print(solve())
