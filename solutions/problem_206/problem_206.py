"""Problem 206: Concealed square."""

from math import isqrt


def has_required_pattern(square: int) -> bool:
    text = str(square)
    return text[::2] == "1234567890"


def solve() -> int:
    lower = isqrt(1_020_304_050_607_080_900)
    upper = isqrt(1_929_394_959_697_989_990)

    for prefix in range(upper // 100, lower // 100 - 1, -1):
        for ending in (70, 30):
            number = prefix * 100 + ending

            if has_required_pattern(number * number):
                return number

    raise ValueError("No solution found")


if __name__ == "__main__":
    print(solve())
