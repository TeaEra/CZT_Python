#!/usr/bin/python
# _*_ coding: utf-8 _*_
#
# Author: TeaEra
# Created date: 2014-11-08

# Two blank lines;


def is_valid_sudoku(board):
    #
    rows = len(board)
    cols = len(board[0])
    #
    for i in range(rows):
        for j in range(cols):
            curr = board[i][j]
            if curr != '.':
                #
                # check row
                count = board[i].count(curr)
                if count > 1:
                    return False
                #
                # check col
                cl = list()
                for ridx in range(rows):
                    cl.append(board[ridx][j])
                count = cl.count(curr)
                if count > 1:
                    return False
                #
                # check mat
                r_start = (i / 3) * 3
                c_start = (j / 3) * 3
                ml = list()
                for ridx in range(r_start, r_start + 3):
                    for cidx in range(c_start, c_start + 3):
                        ml.append(board[ridx][cidx])
                count = ml.count(curr)
                if count > 1:
                    return False
    return True


if __name__ == "__main__":
    #
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
    print is_valid_sudoku(board)