#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda my_list: list(map(lambda x: x * x, my_list)), matrix))
