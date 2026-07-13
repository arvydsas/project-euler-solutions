"""Problem 46: Goldbach's other conjecture."""


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


def follows_conjecture(number: int) -> bool:
    prime = 2
    while prime < number:
        remainder = (number - prime) // 2
        root = int(remainder**0.5)
        if root * root == remainder:
            return True
        prime += 1
        while prime < number and not is_prime(prime):
            prime += 1
    return False


def solve() -> int:
    number = 9
    while True:
        if not is_prime(number) and not follows_conjecture(number):
            return number
        number += 2


if __name__ == "__main__":
    print(solve())
