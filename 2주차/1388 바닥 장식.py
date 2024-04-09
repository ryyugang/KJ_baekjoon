import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range (N) :
    graph.append(list(input()))

def dfs (x, y) :
    if graph[x][y] == '-' :
        graph[x][y] = 1
        for i in [1, -1] :
            dy = y + i
            if 0 <= dy < M and graph[x][dy] == '-' :
                dfs (x, dy)

    if graph[x][y] == '|' :
        graph[x][y] = 1
        for i in [1, -1] :
            dx = x + i
            if 0 <= dx < N and graph[dx][y] == '|' :
                dfs (dx, y)
                
ans = 0
for i in range (N) :
    for j in range (M) :
        if graph[i][j] == '-' or graph[i][j] == '|' :
            dfs(i,j)
            ans += 1
            
print (ans)