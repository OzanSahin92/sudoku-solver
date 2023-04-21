"""Solving sudoku"""
import numpy as np


def check_pos_val(field, y, x, val):
    """Checks if val is possible on positions y,x on the sudoku field"""
    # check row of pos
    for i in range(9):
        if field[y][i] == val:
            return False
    # check col of pos
    for i in range(9):
        if field[i][x] == val:
            return False
    # check box of pos
    y0 = (y // 3) * 3
    x0 = (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if field[y0 + i][x0 + j] == val:
                return False
    # if all checks got through, the val is possible for pos
    return True


def solve(field):
    """Solve function uses backtracking recursively"""
    for y in range(9):
        for x in range(9):
            if field[y][x] == 0:
                for val in range(1, 10):
                    # Check values 1 to 9 if they are possible on position y,x
                    if check_pos_val(field, y, x, val):
                        # if the check was successful field square is set as val
                        field[y][x] = val
                        # solve function is recursively called here to check the next empty square in the sudoku field
                        solve(field)
                        # if all checks went through without a valid value to set in the position y,x, the original
                        # field is set to zero again and a new value is checked based on the for loop (backtracking)
                        field[y][x] = 0
                return
    print(field)
    np.savetxt("data/processed/solved_sudoku_field.txt", field, fmt="%.0f")


def main():
    path_to_sudoku_field = "data/raw/sudoku_field.txt"

    sudoku_field = np.loadtxt(path_to_sudoku_field, dtype=int)

    print("Solving the following Sudoku field: \n")

    print(sudoku_field)

    print("\n\n")

    print("Solved Sudoku field: \n")
    solve(sudoku_field)


if __name__ == "__main__":
    main()
