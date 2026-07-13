"""Problem 63: Powerful digit counts."""


def solve() -> int:
    count = 0
    exponent = 1

    while True:
        matches = sum(1 for base in range(1, 10) if len(str(base**exponent)) == exponent)
        if matches == 0:
            return count
        count += matches
        exponent += 1


if __name__ == "__main__":
    print(solve())
