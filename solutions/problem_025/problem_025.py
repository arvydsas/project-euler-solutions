"""Problem 25: 1000-digit Fibonacci number."""


def solve(digits: int = 1000) -> int:
    index = 2
    a, b = 1, 1

    while len(str(b)) < digits:
        a, b = b, a + b
        index += 1

    return index


if __name__ == "__main__":
    print(solve())
