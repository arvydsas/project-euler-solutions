"""Problem 74: Digit factorial chains."""

from math import factorial


FACTORIALS = [factorial(number) for number in range(10)]


def next_term(number: int) -> int:
    return sum(FACTORIALS[int(digit)] for digit in str(number))


def chain_length(number: int, cache: dict[int, int]) -> int:
    start = number
    seen = []

    while number not in cache and number not in seen:
        seen.append(number)
        number = next_term(number)

    if number in cache:
        length = cache[number]
    else:
        cycle_start = seen.index(number)
        cycle = seen[cycle_start:]
        length = len(cycle)
        for value in cycle:
            cache[value] = length
        seen = seen[:cycle_start]

    for value in reversed(seen):
        length += 1
        cache[value] = length

    return cache[start]


def solve(limit: int = 1_000_000) -> int:
    cache = {1: 1}
    return sum(1 for number in range(1, limit) if chain_length(number, cache) == 60)


if __name__ == "__main__":
    print(solve())
