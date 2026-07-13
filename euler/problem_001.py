"""Problem 1: Multiples of 3 or 5."""


def solve(limit: int = 1000) -> int:
    """Return the sum of multiples of 3 or 5 below ``limit``."""
    return sum(number for number in range(limit) if number % 3 == 0 or number % 5 == 0)
