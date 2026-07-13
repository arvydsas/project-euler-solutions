"""Problem 9: Special Pythagorean triplet."""


def solve(total: int = 1000) -> int:
    for a in range(1, total):
        for b in range(a + 1, total):
            c = total - a - b

            if a * a + b * b == c * c:
                return a * b * c

    raise ValueError("No triplet found")


if __name__ == "__main__":
    print(solve())
