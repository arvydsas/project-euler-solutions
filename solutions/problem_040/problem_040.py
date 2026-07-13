"""Problem 40: Champernowne's constant."""

from math import prod


def digit_at(position: int) -> int:
    length = 1
    count = 9
    start = 1

    while position > length * count:
        position -= length * count
        length += 1
        count *= 10
        start *= 10

    number = start + (position - 1) // length
    return int(str(number)[(position - 1) % length])


def solve() -> int:
    return prod(digit_at(10**power) for power in range(7))


if __name__ == "__main__":
    print(solve())
