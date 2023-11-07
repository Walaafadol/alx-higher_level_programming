#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        m = 1
        for j in i:
            if m == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
                m = m + 1
        print()
