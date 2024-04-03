import sys
input = sys.stdin.readline
sys.setrecursionlimit (10**6)

N = int(input())

def dfs (x) :
    global isValid
    visited[x] = 1
    
    for i in graph[x] :
        if not visited[i] :
            group[i] = (group[x] + 1) % 2
            dfs(i)
        elif group[i] == group[x] :
            isValid = False


for _ in range (N) :
    isValid = True
    V, E = map(int, input().split())
    visited = [0] * (V + 1)
    graph = [[] * (V + 1) for _ in range (V + 1)]
    group = [0] * (V + 1)
    
    for i in range (E) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for j in range (1, V + 1) :
        if isValid :
            dfs(j)
        else :
            break
    
    if isValid :
        print ('YES')
    else :
        print ('NO')

