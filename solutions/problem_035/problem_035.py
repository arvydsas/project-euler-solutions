"""Problem 35: Circular primes."""


def prime_sieve(limit: int) -> list[bool]:
    sieve = [True] * limit
    sieve[:2] = [False, False]

    for number in range(2, int(limit**0.5) + 1):
        if sieve[number]:
            for multiple in range(number * number, limit, number):
                sieve[multiple] = False

    return sieve


def rotations(number: int) -> list[int]:
    text = str(number)
    return [int(text[index:] + text[:index]) for index in range(len(text))]


def solve(limit: int = 1_000_000) -> int:
    primes = prime_sieve(limit)
    return sum(1 for number in range(limit) if all(primes[rotation] for rotation in rotations(number)))


if __name__ == "__main__":
    print(solve())
