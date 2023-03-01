#!/usr/bin/env python3

from sudoku import Sudoku

file_path = "sudoku.txt"

def main():
    s = Sudoku(9)
    s.load_from_file(file_path)

    s.print()
    print("")
    s.solve()

    s.print()

if __name__ == "__main__":
    main()
