"""Problem 72: Counting fractions."""


def solve(limit: int = 1_000_000) -> int:
    phi = list(range(limit + 1))

    for number in range(2, limit + 1):
        if phi[number] == number:
            for multiple in range(number, limit + 1, number):
                phi[multiple] -= phi[multiple] // number

    return sum(phi[2:])


if __name__ == "__main__":
    print(solve())
