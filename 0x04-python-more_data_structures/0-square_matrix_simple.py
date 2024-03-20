#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[row[i] ** 2 for row in matrix] for i in range (3)]
    return (result)
