#!/usr/bin/env python
# coding: utf-8

import numpy as np
from numba import njit
import sys


print(sys.getrecursionlimit())
sys.setrecursionlimit(48000)

# validity check sudoku
@njit
def check_pos_val(y, x, val):
    global field
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


@njit
def solve():
    global field
    for y in range(9):
        for x in range(9):
            if field[y][x] == 0:
                for val in range(1, 10):
                    if check_pos_val(y, x, val):
                        field[y][x] == val
                        solve()
                        field[y][x] == 0
                return
    print(field)


path_to_sudoku_field = '../data/sudoku_field.txt'

field = np.loadtxt(path_to_sudoku_field, dtype=int)

solve()
