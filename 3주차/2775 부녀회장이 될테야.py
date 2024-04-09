import sys
input = sys.stdin.readline

T = int(input())

for _ in range (T) :
    k = int(input())
    n = int(input())
    board = [[0] * (n + 1) for _ in range (k + 1)]
    temp = 0
    
    for i in range (1, k + 1) :
        for j in range (1, n + 1) :
            board[0][j] = j
            board[i][j] = board[i][j - 1] + board[i - 1][j]
            
    
    print (board[k][n])