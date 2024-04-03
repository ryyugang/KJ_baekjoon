import sys
import heapq
input = sys.stdin.readline


N = int(input())
graph = [list(map(int, input().strip())) for _ in range (N)]
visited = [[0] * N for _ in range (N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dijkstra (x, y) :
    visited[x][y] = 1
    queue = [[0, x, y]]
    
    while queue :
        cost, ex, ey = heapq.heappop(queue)
        
        if ex == N - 1 and ey == N - 1 :
            return cost
        
        for i in range (4) :
            nx = ex + dx[i]
            ny = ey + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                if graph[nx][ny] == 1 :
                    heapq.heappush(queue, (cost, nx, ny))
                if graph[nx][ny] == 0 :
                    heapq.heappush(queue, (cost + 1, nx, ny))

    return cost

print (dijkstra(0,0))