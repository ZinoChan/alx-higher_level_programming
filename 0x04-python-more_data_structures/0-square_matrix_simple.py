#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtx = []
    for row in range(len(matrix)):
        new_row = []
        for el in range(len(matrix[row])):
            new_row.append(matrix[row][el] ** 2)
        new_mtx.append(new_row)
    return new_mtx
