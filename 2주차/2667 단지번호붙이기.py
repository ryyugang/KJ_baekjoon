import sys
input = sys.stdin.readline
sys.setrecursionlimit (10 ** 6)

N = int(input())

graph = [list(map(int, input().strip())) for _ in range (N)]

visited = [[0] * N for _ in range (N)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs (y, x) :
    cnt = 1
    queue = []
    queue.append ((y, x))
    
    while queue :
        ey, ex = queue.pop()
        for i in range (4) :
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < N and 0 <= nx < N :
                if visited[ny][nx] == 0 and graph[ny][nx] == 1 :
                    cnt += 1
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
        
    return cnt

res = 0
ans = []
for j in range (N) :
    for i in range (N) :
        if graph[j][i] == 1 and visited[j][i] == 0 :
            visited[j][i] = 1
            ans.append(bfs(j,i))
            res += 1

ans.sort()

print (res)
for i in ans :
    print (i)