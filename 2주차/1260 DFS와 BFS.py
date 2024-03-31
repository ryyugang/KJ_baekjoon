import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range (N + 1)]
visited1 = [0] * (N + 1)
visited2 = [0] * (N + 1)



for i in range (1, M + 1) :
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
def dfs (x) :
    visited1[x] = 1
    print (x, end = ' ')
    
    for j in range (1, N + 1) :
        if graph[x][j] == 1 and visited1[j] == 0 :
            dfs (j)


def bfs (y) :
    queue = [y]
    visited2[y] = 1
    
    while queue :
        y = queue.pop(0)
        print (y, end = ' ')
        for k in range (1, N + 1) :
            if graph[y][k] == 1 and visited2[k] == 0 :
                queue.append(k)
                visited2[k] = 1
                
dfs (V)
print ()
bfs (V)