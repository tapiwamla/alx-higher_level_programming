#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda my_row: list(map(lambda el: el**2, my_row)), matrix)))
