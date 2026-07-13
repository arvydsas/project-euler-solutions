"""Problem 4: Largest palindrome product."""


def is_palindrome(number: int) -> bool:
    text = str(number)
    return text == text[::-1]


def solve() -> int:
    return max(
        a * b
        for a in range(100, 1000)
        for b in range(a, 1000)
        if is_palindrome(a * b)
    )


if __name__ == "__main__":
    print(solve())
