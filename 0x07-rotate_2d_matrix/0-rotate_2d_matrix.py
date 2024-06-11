#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ Rotate 2D Matrix 90 degrees clockwise """
    new_matrix = [[matrix[j][i] for j in range(len(matrix[i])-1, -1, -1)]
                  for i in range(len(matrix))]
    matrix.clear()
    matrix.extend(new_matrix)
