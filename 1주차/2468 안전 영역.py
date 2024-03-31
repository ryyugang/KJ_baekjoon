import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range (N)]

dx = [1, 0, -1, 0] # 동서남북 탐색을 위한 dx, dy
dy = [0, 1, 0, -1]

def bfs (x,y,h) :
    q = [(x,y)]
    check[x][y] = True
    
    while q :
        ex, ey = q.pop()
        for k in range(4) :
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0 <= nx < N and 0 <= ny < N :
                if board[nx][ny] > h and check[nx][ny] == False :
                    q.append((nx, ny))
                    check[nx][ny] = True
    

ans = 0
for h in range (100) :
    cnt = 0 # h가 바뀔 때마다 cnt 초기화 (cnt = 영역 개수)
    check = [[False]*N for _ in range (N)] # h가 바뀔 때마다 방문 확인용 배열도 초기화
    for i in range (N) :
        for j in range (N) :
            if board[i][j] > h and check[i][j] == False : # 물 높이보다 높아야 하며, 방문하지 않았어야 탐색 함
                bfs (i, j, h) # 리턴값이 없는 함수다. 입력 h에 대해 모든 경우 (NxN)를 탐색한다.
                cnt += 1 # bfs 함수가 동작한 횟수만큼 cnt를 1씩 올린다. 
    ans = max (ans, cnt) # 총 4개의 cnt가 들어올 것이고, 더 큰놈만 ans에 집어 넣는다
    
print (ans)