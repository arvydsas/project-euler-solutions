"""Problem 58: Spiral primes."""


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    factor = 5
    while factor * factor <= number:
        if number % factor == 0 or number % (factor + 2) == 0:
            return False
        factor += 6

    return True


def solve() -> int:
    prime_count = 0
    diagonal_count = 1
    side_length = 1

    while True:
        side_length += 2
        square = side_length * side_length
        step = side_length - 1
        prime_count += sum(is_prime(square - step * offset) for offset in range(1, 4))
        diagonal_count += 4

        if prime_count * 10 < diagonal_count:
            return side_length


if __name__ == "__main__":
    print(solve())
