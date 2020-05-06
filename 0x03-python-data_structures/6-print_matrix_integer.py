#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        a = ""
        for j in i:
            print("{:s}{:d}".format(a, j), end='')
            a = " "
        print()
