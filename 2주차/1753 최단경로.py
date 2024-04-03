import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit (10**6)

INF = float('inf')
V, E = map(int, input().split())
K = int(input())

edge = [[] for _ in range (V + 1)]
for i in range (1, E + 1) :
    a, b, cost = map(int, input().split())
    edge[a].append((cost, b))

edge_cost = [INF for _ in range (V + 1)]

def dijkstra (x) :
    
    edge_cost[x] = 0
    queue = [[0, x]]
    
    while queue :
        cost, node = heapq.heappop(queue)
        if cost > edge_cost[node] :
            continue
        for n_cost, n_node in edge[node] :            
            if edge_cost[n_node] > edge_cost[node] + n_cost :
                edge_cost[n_node] = edge_cost[node] + n_cost
                heapq.heappush(queue, [edge_cost[n_node], n_node])
    return edge_cost

dijkstra(K)

for j in range (1, V + 1) :
    if edge_cost[j] == INF :
        print ('INF')
    else :
        print (edge_cost[j])