import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

board = [0] * (100_001)

q = deque()
q.append(N)

while q :
    x = q.popleft()
    if x == K :
        break
    
    for nx in [x+1, x-1, x*2] :
        if 0 <= nx < (100_001) and board[nx] == 0 :
            board[nx] = board[x] + 1
            q.append(nx)

print (board[K])