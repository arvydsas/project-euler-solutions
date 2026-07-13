"""Problem 30: Digit fifth powers."""


def solve(power: int = 5) -> int:
    upper = (power + 1) * 9**power
    return sum(
        number
        for number in range(2, upper)
        if number == sum(int(digit) ** power for digit in str(number))
    )


if __name__ == "__main__":
    print(solve())
