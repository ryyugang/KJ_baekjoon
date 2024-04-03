import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())

graph = [[0] * (N + 1) for _ in range (N + 1)]
indegree = [0] * (N + 1)

for _ in range (M) :
    a, b, cost = map(int, input().split())
    graph[b][a] = cost
    indegree[a] += 1

queue = deque()
gibon_arr = []

for i in range (1, N + 1) :
    if indegree[i] == 0 :
        gibon_arr.append(i)
        queue.append(i)
        
for gibon in gibon_arr :
    graph[gibon][gibon] = 1
    
while queue :
    start = queue.popleft()
    
    for next in range (1, N + 1) :
        if graph[start][next] > 0 and indegree[next] > 0 :
            for gibon in gibon_arr :
                graph[next][gibon] += graph[start][gibon] * graph[start][next]
            indegree[next] -= 1
            if indegree[next] == 0 :
                queue.append(next)

for gibon in gibon_arr :
    print (gibon, graph[N][gibon])