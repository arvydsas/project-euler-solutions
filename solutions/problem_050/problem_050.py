"""Problem 50: Consecutive prime sum."""


def prime_sieve(limit: int) -> list[bool]:
    sieve = [True] * limit
    sieve[:2] = [False, False]

    for number in range(2, int(limit**0.5) + 1):
        if sieve[number]:
            for multiple in range(number * number, limit, number):
                sieve[multiple] = False

    return sieve


def solve(limit: int = 1_000_000) -> int:
    sieve = prime_sieve(limit)
    primes = [number for number, is_prime in enumerate(sieve) if is_prime]
    prefix = [0]

    for prime in primes:
        prefix.append(prefix[-1] + prime)

    best_length = 0
    best_prime = 0

    for start in range(len(prefix)):
        for end in range(start + best_length + 1, len(prefix)):
            total = prefix[end] - prefix[start]
            if total >= limit:
                break
            if sieve[total]:
                best_length = end - start
                best_prime = total

    return best_prime


if __name__ == "__main__":
    print(solve())
