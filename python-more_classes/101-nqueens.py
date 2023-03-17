#!/usr/bin/python3
"""Finding all posible solutions of the N queens puzzle

"""
from sys import argv

if len(argv) is not 2:
    print("Usage: nqueens N")
    exit(1)

if not argv[1].isdigit():
    print("N must be a number")
    exit(1)

N = int(argv[1])

if N < 4:
    print("N must be at least 4")
    exit(1)


def board_column_gen(board=[]):
    """adds a column of zeroes to the right of any boad about to be tested
    for queen argumnets in that column

    """
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def add_queen(board, row, col):
    """Sets "queen" or 1 to coordinates given in board

    args:
        board (list) of (list) of (int): 2D list of ints
        row (int)
        col (int)

    """
    board[row][col] = 1

def coordinate_format(candidates):
    """converts a board (matrix 1 of 0) into a series of row/column indices of each queen

    Args:
        candidate (matrix of 3 by 2)

    Attributes:
        list_t

    Returns:
        List_l
    
    """
    list_t = []
    for x, attempt in enumerate(candidates):
        list_t.append([])
        for i, row in enumerate(attempt):
            list_t[x].append([])
            for j, col in enumerate(row):
                if col:
                    list_t[x][i].append(i)
                    list_t[x][i].append(j)
    return list_t

candidates = []
candidates.append(board_column_gen())

# process column by column testing
for col in range(N):
    new_candidates = []
    for matrix in candidates:
        for row in range(N):
            if new_queen_safe(matrix, row, col):
                temp = [line[:] for line in matrix]
                # place queen in the position
                add_queen(temp, row, col)

                if col < N - 1:
                    board_column_gen(temp)

                new_candidates>append(temp)

    candidates = new_candidates

    for item in coordinate_format(candidates):
        print(item)
