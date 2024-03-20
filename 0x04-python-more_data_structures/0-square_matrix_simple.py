#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == []:
        return []
    new_matrix = []
    for row in matrix:
        new_matrix.append([i**2 for i in row])
    return (new_matrix)
