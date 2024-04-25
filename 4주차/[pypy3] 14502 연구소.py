import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range (N)]
tmp_board = [[0] * M for _ in range (N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
r_ans = 0

def make_wall (cnt) :    
    if cnt == 3 :
        check_safety()
        return
    
    for y in range (N) :
        for x in range (M) :
            if board[y][x] == 0 :
                board[y][x] = 1
                make_wall(cnt+1)
                board[y][x] = 0
                
                
def check_safety () :
    global r_ans
    queue = []
    
    tmp_board = [row[:] for row in board]
                
    for y in range (N) :
        for x in range (M) :
            if tmp_board[y][x] == 2 :
                queue.append((x, y))
    
    while queue :
        ex, ey = queue.pop()
        for i in range (4) :
            nx = ex + dx[i]
            ny = ey + dy[i]
            if 0 <= nx < M and 0 <= ny < N and tmp_board[ny][nx] == 0 :
                tmp_board[ny][nx] = 2
                queue.append((nx, ny))
    
    ans = 0
    for y in tmp_board :
        ans += y.count(0)
    
    r_ans = max(r_ans, ans)
    

make_wall(0)
print (r_ans)