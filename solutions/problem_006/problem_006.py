"""Problem 6: Sum square difference."""


def solve(limit: int = 100) -> int:
    numbers = range(1, limit + 1)
    return sum(numbers) ** 2 - sum(number * number for number in numbers)


if __name__ == "__main__":
    print(solve())
