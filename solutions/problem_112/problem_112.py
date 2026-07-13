"""Problem 112: Bouncy numbers."""


def is_bouncy(number: int) -> bool:
    digits = str(number)
    return digits != "".join(sorted(digits)) and digits != "".join(sorted(digits, reverse=True))


def solve(target_numerator: int = 99, target_denominator: int = 100) -> int:
    bouncy_count = 0
    number = 0

    while True:
        number += 1
        if is_bouncy(number):
            bouncy_count += 1

        if bouncy_count * target_denominator == number * target_numerator:
            return number


if __name__ == "__main__":
    print(solve())
