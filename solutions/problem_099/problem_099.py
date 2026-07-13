"""Problem 99: Largest exponential."""

from math import log
from pathlib import Path


BASE_EXP_FILE = Path(__file__).with_name("problem_099_base_exp.txt")


def solve(path: Path = BASE_EXP_FILE) -> int:
    best_line = 0
    best_value = 0.0

    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        base, exponent = (int(value) for value in line.split(","))
        value = exponent * log(base)

        if value > best_value:
            best_line = line_number
            best_value = value

    return best_line


if __name__ == "__main__":
    print(solve())
