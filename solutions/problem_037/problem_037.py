"""Problem 37: Truncatable primes."""


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


def is_truncatable_prime(number: int) -> bool:
    text = str(number)
    return number > 10 and is_prime(number) and all(
        is_prime(int(text[index:])) and is_prime(int(text[:index]))
        for index in range(1, len(text))
    )


def solve() -> int:
    total = 0
    found = 0
    number = 11

    while found < 11:
        if is_truncatable_prime(number):
            total += number
            found += 1
        number += 2

    return total


if __name__ == "__main__":
    print(solve())
