import sys
input = sys.stdin.readline
sys.setrecursionlimit (10**6)

V = int(input())
isIn = [0] + list(map(int, input().strip()))
graph = [[] for _ in range (V + 1)]
visited = [0] * (V + 1) 

cnt = 0
ans = 0

for i in range (V - 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    if isIn[a] == 1 and isIn[b] == 1 :
        ans += 2

def dfs (x) :
    visited[x] = 1
    inside_count = 0
    for j in graph[x] :
        if isIn[j] == 1 :
            inside_count += 1
        elif not visited[j] and isIn[k] == 0 :
            inside_count += dfs (j)
    return inside_count

for k in range (1, V + 1) :
    if isIn[k] == 0 and not visited[k] :
        number_inside = dfs (k)
        cnt += (number_inside) * (number_inside - 1)
        
print (cnt + ans)