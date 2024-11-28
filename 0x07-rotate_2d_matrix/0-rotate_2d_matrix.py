#!/usr/bin/python3
"""
Script that rotates a n x n 2D matrix 90 degrees clockwise."""



def rotate_2d_matrix(matrix):
    """
    function that rotates a matrix"""

    leng = len(matrix)

    
    # Transpose the matrix
    for i in range(leng):
        for j in range(i + 1, leng):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(leng):
        matrix[i].reverse()