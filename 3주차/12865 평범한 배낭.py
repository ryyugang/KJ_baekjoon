import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weights = [0]
prices = [0]
for _ in range (N) :
    a, b = map(int , input().split())
    weights.append(a)
    prices.append(b)

board = [[0] * (K + 1) for _ in range (N + 1)]

for y in range (1, N + 1) :
    for x in range (1, K + 1) :
        if x >= weights[y] :
            board[y][x] = max ((prices[y] + board[y - 1][x - weights[y]], board[y - 1][x]))
        else :
            board[y][x] = board[y - 1][x]

print (board[N][K])