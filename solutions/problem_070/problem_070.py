"""Problem 70: Totient permutation."""


def totients(limit: int) -> list[int]:
    phi = list(range(limit + 1))

    for number in range(2, limit + 1):
        if phi[number] == number:
            for multiple in range(number, limit + 1, number):
                phi[multiple] -= phi[multiple] // number

    return phi


def is_permutation(first: int, second: int) -> bool:
    return sorted(str(first)) == sorted(str(second))


def solve(limit: int = 10_000_000) -> int:
    phi = totients(limit)
    best_number = 0
    best_ratio = float("inf")

    for number in range(2, limit):
        if is_permutation(number, phi[number]):
            ratio = number / phi[number]
            if ratio < best_ratio:
                best_number = number
                best_ratio = ratio

    return best_number


if __name__ == "__main__":
    print(solve())
