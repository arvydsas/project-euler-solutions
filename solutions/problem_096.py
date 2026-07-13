"""Problem 96: Su Doku."""

from pathlib import Path


PUZZLE_FILE = Path(__file__).with_name("problem_096_sudoku.txt")

Grid = list[list[int]]


def read_grids(path: Path = PUZZLE_FILE) -> list[Grid]:
    grids = []
    rows = []

    for line in path.read_text().splitlines():
        if line.startswith("Grid"):
            rows = []
            continue

        rows.append([int(digit) for digit in line])

        if len(rows) == 9:
            grids.append(rows)

    return grids


def candidates(grid: Grid, row: int, col: int) -> set[int]:
    used = set(grid[row])
    used.update(grid[r][col] for r in range(9))

    box_row = row - row % 3
    box_col = col - col % 3

    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            used.add(grid[r][c])

    return set(range(1, 10)) - used


def next_empty_cell(grid: Grid) -> tuple[int, int, set[int]] | None:
    best = None

    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                continue

            values = candidates(grid, row, col)

            if best is None or len(values) < len(best[2]):
                best = (row, col, values)

            if len(values) == 0:
                return best

    return best


def solve_grid(grid: Grid) -> Grid | None:
    cell = next_empty_cell(grid)

    if cell is None:
        return grid

    row, col, values = cell

    for value in sorted(values):
        grid[row][col] = value

        if solve_grid(grid) is not None:
            return grid

        grid[row][col] = 0

    return None


def top_left_number(grid: Grid) -> int:
    return grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]


def solve() -> int:
    total = 0

    for grid in read_grids():
        solved = solve_grid([row[:] for row in grid])

        if solved is None:
            raise ValueError("A puzzle could not be solved")

        total += top_left_number(solved)

    return total


if __name__ == "__main__":
    print(solve())
