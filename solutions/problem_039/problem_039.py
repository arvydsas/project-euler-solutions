"""Problem 39: Integer right triangles."""


def solutions(perimeter: int) -> int:
    count = 0

    for a in range(1, perimeter // 3):
        for b in range(a, perimeter // 2):
            c = perimeter - a - b
            if a * a + b * b == c * c:
                count += 1

    return count


def solve(limit: int = 1000) -> int:
    return max(range(1, limit + 1), key=solutions)


if __name__ == "__main__":
    print(solve())
