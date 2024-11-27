#!/usr/bin/python3
'''Script that Solves the N queen problem'''


import sys


def nqueens(N):
    '''
    function that solves for nqueens'''
    # Helper function to check if a position is safe
    def is_safe(board, row, col):
        for r, c in board:
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    # Backtracking function to solve the puzzle
    def backtrack(board, row):
        if row == N:
            # Solution found, print it
            print(board)
            return

        for col in range(N):
            if is_safe(board, row, col):
                board.append([row, col])
                backtrack(board, row + 1)
                board.pop()  # Backtrack

    board = []
    backtrack(board, 0)


def main():
    '''
    running suit for nqueens() fucntion
    '''
    # Check the command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)


if __name__ == "__main__":
    main()
