import sys


def N_Queen(row, board):
    global result

    if len(board) == N:
        result += 1
        return

    for col in range(N):
        check = True
        for x, y in board:
            if y == col:
                check = False
                break
            if abs(x - row) == abs(y - col):
                check = False
                break

        if check:
            board.append((row, col))
            N_Queen(row + 1, board)
            board.pop()

import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
result = 0

N_Queen(0, [])
print(result)
