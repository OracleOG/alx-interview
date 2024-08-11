#!/usr/bin/python3
'''
creating a function
that returns pascals triangle
'''


def pascal_triangle(k):
    '''returns an
    array representing pascals triangle
    '''
    if k <= 0:
        return []

    pasc_array = []

    for nth_row in range(k):
        row = []
        for nth_col in range(nth_row + 1):
            if nth_col == 0 or nth_col == nth_row:
                row.append(1)
            else:
                row.append(pasc_array[nth_row - 1][nth_col - 1]
                           + pasc_array[nth_row - 1][nth_col])
        pasc_array.append(row)

    return pasc_array
