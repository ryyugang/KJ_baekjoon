import sys
import copy
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range (N)]
empty = []
virus = []
ans = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for y in range (N) :
    for x in range (M) :
        if board[y][x] == 0 :
            empty.append((x, y))
            
def solve() :
    global ans
    
    for combi in combinations(empty, 3) :
        tmp_board = copy.deepcopy(board)
        for wx, wy in combi :
            tmp_board[wy][wx] = 1
            
        for y in range (N) :
            for x in range (M) :
                if tmp_board[y][x] == 2 :
                    virus.append((y, x))
        
        while virus :
            y, x = virus.pop()
            for i in range (4) :
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and tmp_board[ny][nx] == 0 :
                    tmp_board[ny][nx] = 2
                    virus.append((ny, nx))
        
        cnt = 0
        for y in (tmp_board) :
            cnt += y.count(0)
        
        ans = max(ans, cnt)

solve()
print (ans)