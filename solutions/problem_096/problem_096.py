# My solution note: I solve each Sudoku using deterministic fills first, then recursive guessing when needed.
import random
from pathlib import Path


SUDOKU_FILE = Path(__file__).with_name("0096_sudoku.txt")


class Sudoku:
    def __init__(self):
        self.sud = [[0 for _ in range(9)] for _ in range(9)]

    def assign(self, sud):
        self.sud = sud

    def row_verification(self):
        for row in self.sud:
            values = [number for number in row if number != 0]
            if len(values) != len(set(values)):
                return False

        return True

    def column_verification(self):
        for column_index in range(9):
            values = []

            for row_index in range(9):
                number = self.sud[row_index][column_index]

                if number != 0:
                    values.append(number)

            if len(values) != len(set(values)):
                return False

        return True

    def square_verification(self):
        for square_row in range(0, 9, 3):
            for square_column in range(0, 9, 3):
                values = []

                for row_index in range(square_row, square_row + 3):
                    for column_index in range(square_column, square_column + 3):
                        number = self.sud[row_index][column_index]

                        if number != 0:
                            values.append(number)

                if len(values) != len(set(values)):
                    return False

        return True

    def possible_values(self, row_index, column_index):
        if self.sud[row_index][column_index] != 0:
            return []

        # Remove every value already present in the same row, column, or 3x3 square.
        used_values = set(self.sud[row_index])

        for row in self.sud:
            used_values.add(row[column_index])

        square_row = (row_index // 3) * 3
        square_column = (column_index // 3) * 3

        for row in range(square_row, square_row + 3):
            for column in range(square_column, square_column + 3):
                used_values.add(self.sud[row][column])

        return [number for number in range(1, 10) if number not in used_values]

    def fill_single_possible_values(self):
        changed = False

        for row_index in range(9):
            for column_index in range(9):
                if self.sud[row_index][column_index] != 0:
                    continue

                values = self.possible_values(row_index, column_index)

                if len(values) == 1:
                    self.sud[row_index][column_index] = values[0]
                    changed = True

        return changed

    def fill_square_unique_locations(self):
        changed = False

        for square_row in range(0, 9, 3):
            for square_column in range(0, 9, 3):
                square_values = []

                for row_index in range(square_row, square_row + 3):
                    for column_index in range(square_column, square_column + 3):
                        square_values.append(self.sud[row_index][column_index])

                missing_values = [
                    number for number in range(1, 10) if number not in square_values
                ]

                for number in missing_values:
                    locations = []

                    for row_index in range(square_row, square_row + 3):
                        for column_index in range(square_column, square_column + 3):
                            if self.sud[row_index][column_index] != 0:
                                continue

                            if number in self.possible_values(row_index, column_index):
                                locations.append((row_index, column_index))

                    if len(locations) == 1:
                        row_index, column_index = locations[0]
                        self.sud[row_index][column_index] = number
                        changed = True

        return changed

    def fill_row_unique_locations(self):
        changed = False

        for row_index in range(9):
            row_values = self.sud[row_index]
            missing_values = [
                number for number in range(1, 10) if number not in row_values
            ]

            for number in missing_values:
                locations = []

                for column_index in range(9):
                    if self.sud[row_index][column_index] != 0:
                        continue

                    if number in self.possible_values(row_index, column_index):
                        locations.append((row_index, column_index))

                if len(locations) == 1:
                    row_index, column_index = locations[0]
                    self.sud[row_index][column_index] = number
                    changed = True

        return changed

    def fill_column_unique_locations(self):
        changed = False

        for column_index in range(9):
            column_values = []

            for row_index in range(9):
                column_values.append(self.sud[row_index][column_index])

            missing_values = [
                number for number in range(1, 10) if number not in column_values
            ]

            for number in missing_values:
                locations = []

                for row_index in range(9):
                    if self.sud[row_index][column_index] != 0:
                        continue

                    if number in self.possible_values(row_index, column_index):
                        locations.append((row_index, column_index))

                if len(locations) == 1:
                    row_index, column_index = locations[0]
                    self.sud[row_index][column_index] = number
                    changed = True

        return changed

    def solve_deterministic(self):
        changed = True

        # Repeat simple deductions until none of them changes the grid.
        while changed:
            changed = self.fill_single_possible_values()
            changed = self.fill_square_unique_locations() or changed
            changed = self.fill_row_unique_locations() or changed
            changed = self.fill_column_unique_locations() or changed

        return self.sud

    def is_eligible(self):
        return (
            self.row_verification()
            and self.column_verification()
            and self.square_verification()
        )

    def find_guess_location(self):
        best_location = None
        best_values = []

        # Choose the empty cell with the fewest candidates to keep guessing narrow.
        for row_index in range(9):
            for column_index in range(9):
                if self.sud[row_index][column_index] != 0:
                    continue

                values = self.possible_values(row_index, column_index)

                if len(values) == 0:
                    return row_index, column_index, []

                if best_location is None or len(values) < len(best_values):
                    best_location = (row_index, column_index)
                    best_values = values

        if best_location is None:
            return None, None, []

        return best_location[0], best_location[1], best_values

    def solve_with_guesses(self):
        self.solve_deterministic()

        if not self.is_eligible():
            return False

        if self.is_solved():
            return True

        row_index, column_index, values = self.find_guess_location()

        if len(values) == 0:
            return False

        random.shuffle(values)

        for value in values:
            saved_sudoku = [row[:] for row in self.sud]
            self.sud[row_index][column_index] = value

            # Backtrack if the guessed value eventually leads to a contradiction.
            if self.solve_with_guesses():
                return True

            self.sud = saved_sudoku

        return False

    def solve(self):
        self.solve_with_guesses()
        return self.sud

    def is_solved(self):
        for row in self.sud:
            if 0 in row:
                return False

        return self.is_eligible()

    def top_left_number(self):
        return self.sud[0][0] * 100 + self.sud[0][1] * 10 + self.sud[0][2]


def read_sudokus(file_name):
    sudokus = []

    with open(file_name) as file:
        rows = []

        for line in file:
            line = line.strip()

            if line.startswith("Grid"):
                rows = []
                continue

            rows.append([int(number) for number in line])

            if len(rows) == 9:
                sudoku = Sudoku()
                sudoku.assign(rows)
                sudokus.append(sudoku)

    return sudokus


def answer(file_name):
    puzzles = read_sudokus(file_name)
    total = 0

    for puzzle in puzzles:
        puzzle.solve()

        if not puzzle.is_solved():
            raise ValueError("Not all puzzles were solved")

        total += puzzle.top_left_number()

    return total


if __name__ == "__main__":
    puzzles = read_sudokus(SUDOKU_FILE)
    solved_count = 0

    for puzzle in puzzles:
        puzzle.solve()

        if puzzle.is_solved():
            solved_count += 1

    print(f"{solved_count} out of {len(puzzles)} puzzles solved")
    print(f"All puzzles solved: {solved_count == len(puzzles)}")
    print(f"Answer: {answer(SUDOKU_FILE)}")


