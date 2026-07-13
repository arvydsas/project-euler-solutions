"""Problem 13: Large sum."""

from pathlib import Path


NUMBER_FILE = Path(__file__).with_name("problem_013_numbers.txt")


def solve(path: Path = NUMBER_FILE) -> int:
    numbers = [int(line) for line in path.read_text().splitlines() if line.isdigit()]
    return int(str(sum(numbers))[:10])


if __name__ == "__main__":
    print(solve())
