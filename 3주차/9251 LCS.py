import sys
input = sys.stdin.readline

word1 = [0] + list(map(str, input().strip()))
word2 = [0] + list(map(str, input().strip()))
a = len(word1)
b = len(word2)

board = [[0] * (b) for _ in range (a)]
for i in range (1, a) :
    for j in range (1, b) :
        if word1[i] == word2[j] :
            board[i][j] = board[i - 1][j - 1] + 1
        else :
            board[i][j] = max(board[i][j - 1], board[i - 1][j])

print (board[a - 1][b - 1])
# for k in board :
#     print (k) 