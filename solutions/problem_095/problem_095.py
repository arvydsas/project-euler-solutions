"""Problem 95: Amicable chains."""


def divisor_sums(limit: int) -> list[int]:
    sums = [0] * (limit + 1)

    for divisor in range(1, limit // 2 + 1):
        for multiple in range(divisor * 2, limit + 1, divisor):
            sums[multiple] += divisor

    return sums


def solve(limit: int = 1_000_000) -> int:
    sums = divisor_sums(limit)
    visited = [False] * (limit + 1)
    best_chain = []

    for start in range(2, limit + 1):
        if visited[start]:
            continue

        seen = {}
        chain = []
        number = start

        while 0 < number <= limit and number not in seen:
            if visited[number]:
                break

            seen[number] = len(chain)
            chain.append(number)
            number = sums[number]

        if number in seen:
            cycle = chain[seen[number] :]

            if len(cycle) > len(best_chain):
                best_chain = cycle

        for number in chain:
            visited[number] = True

    return min(best_chain)


if __name__ == "__main__":
    print(solve())
