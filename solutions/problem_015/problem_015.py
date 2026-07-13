"""Problem 15: Lattice paths."""

from math import comb


def solve(size: int = 20) -> int:
    return comb(size * 2, size)


if __name__ == "__main__":
    print(solve())
