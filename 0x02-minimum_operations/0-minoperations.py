#!/usr/bin/python3
'''Module that contains the method minOperations
'''


def minOperations(n):
    '''method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.'''
    if type(n) is not int or n <= 1:
        return 0

    count = 0
    div = 2

    while (n > 1):
        while (n % div == 0):
            n = n/div
            count += div
        div += 1

    return count
