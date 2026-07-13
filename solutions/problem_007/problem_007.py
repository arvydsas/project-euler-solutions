"""Problem 7: 10001st prime."""


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


def solve(position: int = 10_001) -> int:
    count = 1
    candidate = 1

    while count < position:
        candidate += 2
        if is_prime(candidate):
            count += 1

    return candidate


if __name__ == "__main__":
    print(solve())
