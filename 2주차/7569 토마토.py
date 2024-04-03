import sys
import heapq
input = sys.stdin.readline

M, N, H = map(int, input().split())

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

board = [[] for _ in range (H)]
visited = [[] for _ in range (H)]

for h in range(H):
    for n in range(N):
        tmp = list(map(int,input().split()))
        board[h].append(tmp)
        visited[h].append([0] * M)
        
def bfs () :
    queue = []
    for h in range (H) :
        for y in range (N) :
            for x in range (M) :
                if board[h][y][x] == 1 :
                    queue.append((0, h, y, x))
                    visited[h][y][x] = 1
    day = 0
    while queue :
        
        day, h, y, x = heapq.heappop(queue)
        
        for i in range (6) :
            nh = h + dh[i]
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= nx < M and 0 <= ny < N and 0 <= nh < H and visited[nh][ny][nx] == 0 :
                if board[nh][ny][nx] == 0 :
                    board[nh][ny][nx] = 1
                    visited[nh][ny][nx] = 1
                    heapq.heappush(queue, (day + 1, nh, ny, nx))
    
    for h in range (H) :
        for y in range (N) :
            for x in range (M) :
                if board[h][y][x] == 0 :
                    return -1
                
    return day
                    
print (bfs())