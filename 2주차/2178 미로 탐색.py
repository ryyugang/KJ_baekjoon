import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
graph = []

for _ in range (N) :
    graph.append(list(map(int, input().strip())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs (x, y) :
    
    queue = deque([(x, y)])
    
    while queue :
        ex, ey = queue.popleft()
        for i in range (4) :
            nx = ex + dx[i]
            ny = ey + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if graph[nx][ny] == 1 :
                    graph[nx][ny] = graph[ex][ey] + 1
                    queue.append((nx, ny))
                    
    return graph[N-1][M-1]

print (bfs(0,0))