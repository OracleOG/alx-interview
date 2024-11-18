#!/usr/bin/python3
'''method that determines if all the boxes can be opened.
'''
# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# def canUnlockAll(boxes)
'''
keys will be stored in a set
keys will be added to the set as they are found
keys will be removed from the set as they are used
'''
# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]


def canUnlockAll(boxes):
    '''method that determines if all the boxes can be opened.'''
    keys = set([0])
    leftover = [0]

    while (leftover):
        box = leftover.pop()
        for key in boxes[box]:
            if key not in keys and key < len(boxes):
                keys.add(key)
                leftover.append(key)

    return len(keys) == len(boxes)
    