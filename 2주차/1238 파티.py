import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit (10 ** 6)

INF = float('inf')
N, M, X = map(int, input().split())
edges = [[] for _ in range (N + 1)]

for i in range (M) :
    a, b, cost = map(int, input().split())
    edges[a].append((cost, b))

def dijkstra (x) :
    distance = [INF for _ in range (M + 1)]
    
    distance[x] = 0
    queue = [[0, x]]
    
    while queue :
        cost, node = heapq.heappop(queue)
        if cost > distance[node] :
            continue
        for n_cost, n_node in edges[node] :
            if distance[n_node] > distance[node] + n_cost :
                distance[n_node] = distance[node] + n_cost
                heapq.heappush(queue, (distance[n_node], n_node))
    
    return distance

result = 0
for j in range (1, N + 1) :
    start = dijkstra(j)
    end = dijkstra(X)
    result = max(result, start[X] + end[j])

print (result)