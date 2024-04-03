import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

N, M, K, X = map(int, input().split())
edges = [[] for _ in range (N + 1)]

for i in range (M) :
    a, b = map(int, input().split())
    edges[a].append((1, b))
    
distance = [INF for _ in range (N + 1)]
    
def dijkstra (x) :
    distance[x] = 0
    queue = [[0, x]]
    
    while queue :
        cost, node = heapq.heappop(queue)
        if cost > distance[node] :
            continue
        for n_cost, n_node in edges[node] :
            if distance[n_node] > distance[node] + n_cost :
                distance[n_node] = distance[node] + n_cost
                heapq.heappush(queue, [distance[n_node], n_node])
                
    return distance

dijkstra(X)

if K not in distance :
    print ('-1')
for j in range (1, N + 1) :
    if distance[j] == K :
        print (j)