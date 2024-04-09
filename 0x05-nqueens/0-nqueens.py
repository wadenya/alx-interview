#!/usr/bin/python3

"""0. N queens"""


import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    n_q = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if n_q < 4:
    print('N must be a number')
    exit(1)


def solve_nqueens(n):
    """self descriptive"""
    if n == 0:
        return [[]]
    inner_sltn = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_sltn
            if safe_queen((n, i + 1), solution)]


def attack_queen(square, queen):
    """self descriptive"""
    (row1, colm1) = square
    (row2, colm2) = queen
    return (row1 == row2) or (colm1 == colm2) or\
            abs(row1 - row2) == abs (colm1 - colm2)


def safe_queen(sqr, queens):
    """"self descriptive"""
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
        return True
