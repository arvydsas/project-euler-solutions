"""Problem 12: Highly divisible triangular number."""


def divisor_count(number: int) -> int:
    count = 1
    factor = 2

    while factor * factor <= number:
        exponent = 0
        while number % factor == 0:
            number //= factor
            exponent += 1

        if exponent:
            count *= exponent + 1

        factor += 1 if factor == 2 else 2

    if number > 1:
        count *= 2

    return count


def solve(min_divisors: int = 500) -> int:
    triangle = 0
    number = 1

    while True:
        triangle += number
        if divisor_count(triangle) > min_divisors:
            return triangle
        number += 1


if __name__ == "__main__":
    print(solve())
