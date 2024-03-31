import sys
input = sys.stdin.readline
sys.setrecursionlimit (10**6)

N = int(input())

graph = [[] * (N + 1) for _ in range (N + 1)]
check = [0] * (N + 1)

for i in range (N - 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs (x) :
    for j in graph[x] :
        if not check[j] :
            check[j] = x
            dfs(j)
            
dfs (1)

for k in check[2:] :
    print (k, end = ' ')