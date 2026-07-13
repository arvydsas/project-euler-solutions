"""Problem 19: Counting Sundays."""

from datetime import date


def solve() -> int:
    return sum(
        1
        for year in range(1901, 2001)
        for month in range(1, 13)
        if date(year, month, 1).weekday() == 6
    )


if __name__ == "__main__":
    print(solve())
