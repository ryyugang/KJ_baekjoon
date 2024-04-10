import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range (N)]

for i in range (1, N) :
    board[i][0] = min(board[i-1][1], board[i-1][2]) + board[i][0]
    board[i][1] = min(board[i-1][0], board[i-1][2]) + board[i][1]
    board[i][2] = min(board[i-1][0], board[i-1][1]) + board[i][2]

print (min(board[N - 1]))