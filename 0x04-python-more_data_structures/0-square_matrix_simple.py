#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][j] * matrix[i][j])
        matrix2.append(row)
    return matrix2
