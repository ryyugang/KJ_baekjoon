import sys
import heapq
input = sys.stdin.readline

M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range (N)]
visited = [[False] * M for _ in range (N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs () :
    queue = []
    # 값이 1인 위치를 찾고 그 자리에서부터 이동 시작
    for y in range (N) :
        for x in range (M) :
            if board[y][x] == 1 :
                visited[y][x] = True
                queue.append((0, x, y))
    
    # day를 0으로 초기화해주고, 값이 1인 위치부터 동서남북으로 탐색 돌림
    day = 0
    while queue :
        day, ex, ey = heapq.heappop(queue)
        for i in range (4) :
            nx = ex + dx[i]
            ny = ey + dy[i]
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == False :
                if board[ny][nx] == 0 :
                    board[ny][nx] = 1
                    visited[ny][nx] = True
                    heapq.heappush(queue, (day + 1, nx, ny))
    
    # 탐색이 끝난 이후, 0이 있다면 -1 리턴
    for y in range (N) :
        for x in range (M) :
            if board[y][x] == 0 :
                return -1
            
    return day

print (bfs())