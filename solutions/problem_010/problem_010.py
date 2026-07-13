"""Problem 10: Summation of primes."""


def solve(limit: int = 2_000_000) -> int:
    sieve = bytearray(b"\x01") * limit
    sieve[:2] = b"\x00\x00"

    for number in range(2, int(limit**0.5) + 1):
        if sieve[number]:
            start = number * number
            sieve[start:limit:number] = b"\x00" * (((limit - 1 - start) // number) + 1)

    return sum(index for index, is_prime in enumerate(sieve) if is_prime)


if __name__ == "__main__":
    print(solve())
