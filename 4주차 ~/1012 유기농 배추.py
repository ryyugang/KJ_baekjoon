import sys
input = sys.stdin.readline 

T = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs (y, x) :
    q = [(y, x)]
    

    while q :
        ey, ex = q.pop()
        for d in range (4) :
            ny = ey + dy[d]
            nx = ex + dx[d]
            if 0 <= ny < N and 0 <= nx < M :
                if board[ny][nx] == 1 and check[ny][nx] == False :
                    check[ny][nx] = True
                    q.append((ny, nx))
        

for _ in range (T) :
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range (N)]
    check = [[False] * M for _ in range (N)]
    
    for _ in range (K) :
        x, y = map(int, input().split())
        board[y][x] = 1

    ans = 0
    for y in range (N) :
        for x in range (M) :
            if board[y][x] == 1 and check[y][x] == False :
                bfs(y, x)
                ans += 1
                
                
    print (ans)