"""Problem 34: Digit factorials."""

from math import factorial


FACTORIALS = [factorial(number) for number in range(10)]


def solve() -> int:
    return sum(
        number
        for number in range(10, 7 * FACTORIALS[9])
        if number == sum(FACTORIALS[int(digit)] for digit in str(number))
    )


if __name__ == "__main__":
    print(solve())
