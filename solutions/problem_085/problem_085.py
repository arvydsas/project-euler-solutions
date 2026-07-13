"""Problem 85: Counting rectangles."""


def rectangle_count(width: int, height: int) -> int:
    return width * (width + 1) * height * (height + 1) // 4


def solve(target: int = 2_000_000) -> int:
    best_area = 0
    best_difference = target

    for width in range(1, 2_000):
        for height in range(1, 2_000):
            count = rectangle_count(width, height)
            difference = abs(target - count)

            if difference < best_difference:
                best_area = width * height
                best_difference = difference

            if count > target and height > width:
                break

    return best_area


if __name__ == "__main__":
    print(solve())
