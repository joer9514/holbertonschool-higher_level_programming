#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    _aux_matrix = []
    for i in matrix:
        _tmp = list(map(lambda x: x * x, i))
        _aux_matrix.append(_tmp)
    return (_aux_matrix)
