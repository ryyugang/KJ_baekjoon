import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

graph = []

for _ in range (N) :
    graph.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue = []
for i in range (N) :
    for j in range (N) :
        if graph[i][j] != 0 :
            queue.append((graph[i][j], i, j, 0))

queue.sort()

queue = deque(queue)

while queue :
    virus, x, y, day = queue.popleft()
    if day == S :
        break
    for _ in range (4) :
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0 :
            graph[nx][ny] = virus
            queue.append((virus, nx, ny, day + 1))

if graph[X-1][Y-1] != 0 :
    print (graph[X-1][Y-1])
else :
    print (0)