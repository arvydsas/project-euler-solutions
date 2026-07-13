"""Problem 44: Pentagon numbers."""


def pentagonal(index: int) -> int:
    return index * (3 * index - 1) // 2


def is_pentagonal(number: int) -> bool:
    root = int((1 + 24 * number) ** 0.5)
    return root * root == 1 + 24 * number and (1 + root) % 6 == 0


def solve() -> int:
    pentagons = []
    index = 1

    while True:
        current = pentagonal(index)

        for previous in pentagons:
            difference = current - previous
            if is_pentagonal(difference) and is_pentagonal(current + previous):
                return difference

        pentagons.append(current)
        index += 1


if __name__ == "__main__":
    print(solve())
