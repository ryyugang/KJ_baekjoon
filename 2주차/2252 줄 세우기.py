import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

indegree = [0] * (N + 1)
graph = [[] for _ in range (N + 1)]
for i in range (M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort () :
    result = []
    queue = deque ()
    
    for i in range (1, N + 1) :
        if indegree[i] == 0 :
            queue.append(i)
    
    while queue :
        now = queue.popleft()
        result.append(now)
        
        for j in graph[now] :
            indegree[j] -= 1
            if indegree[j] == 0 :
                queue.append(j)
    
    for k in result :
        print (k, end = ' ')

topology_sort()