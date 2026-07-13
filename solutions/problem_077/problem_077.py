"""Problem 77: Prime summations."""


def primes_up_to(limit: int) -> list[int]:
    sieve = [True] * (limit + 1)
    sieve[:2] = [False, False]

    for number in range(2, int(limit**0.5) + 1):
        if sieve[number]:
            for multiple in range(number * number, limit + 1, number):
                sieve[multiple] = False

    return [number for number, is_prime in enumerate(sieve) if is_prime]


def ways_to_write(total: int) -> int:
    ways = [0] * (total + 1)
    ways[0] = 1

    for prime in primes_up_to(total):
        for amount in range(prime, total + 1):
            ways[amount] += ways[amount - prime]

    return ways[total]


def solve(minimum_ways: int = 5_000) -> int:
    number = 2

    while ways_to_write(number) <= minimum_ways:
        number += 1

    return number


if __name__ == "__main__":
    print(solve())
