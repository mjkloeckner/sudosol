class Sudoku:
    def __init__(self, dim):
        self.dim = dim  # Dimension of the sudoku
        self.sudoku = []

    # Load the sudoku into a 2D-List
    def load_from_file(self, filename):
        self.sudoku = [[0] * self.dim for i in range(self.dim)]

        with open(filename, "rt") as f:
            for line, i in zip(f, range(self.dim)):
                for char, j in zip(line, range(self.dim)):
                    if char != '\n':
                        self.sudoku[i][j] = int(char)

    # Prints the sudoku in a list format
    def print(self):
        for x in range(len(self.sudoku)):
            print(self.sudoku[x])

    def set_value(self, val, r, c):
        self.sudoku[r][c] = val

    def get_value(self, r, c) -> int:
        return self.sudoku[r][c]

    def find_empty_cell(self) -> tuple[bool, int, int]:
        for r in range(self.dim):
            for c in range(self.dim):
                if self.sudoku[r][c] == 0:
                    return True, r, c

        return False, 0, 0

    def is_value_valid(self, value, r, c):
        if value in self.sudoku[r]:
            return False

        col_values = [self.sudoku[i][c] for i in range(self.dim)]

        if value in col_values:
            return False

        row_start = (r // 3) * 3
        col_start = (c // 3) * 3

        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if self.sudoku[r][c] == value:
                    return False

        return True


    def solve(self):
        find, r, c = self.find_empty_cell()
        if find == False:
            # Sudoku solved!
            return True

        for value in range(1, self.dim + 1):
            if self.is_value_valid(value, r, c):
                self.set_value(value, r, c)
                if self.solve():
                    return True

            self.set_value(0, r, c)
        return False
