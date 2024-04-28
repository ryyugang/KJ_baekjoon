import sys
import heapq
input = sys.stdin.readline

INF = float('inf')
N, E = map(int, input().split())
edge = [[] for _ in range (N + 1)]

for i in range (1, E + 1) :
    start, end, cost = map(int, input().split())
    edge[start].append((cost, end))
    edge[end].append((cost, start))

v1, v2 = map(int, input().split())

def dijkstra (x) :
    
    edge_cost = [INF for _ in range (N + 1)]
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

tmp1 = dijkstra(1)
tmp_v1 = dijkstra(v1)
tmp_v2 = dijkstra(v2)

ans = min(tmp1[v1] + tmp_v1[v2] + tmp_v2[N], tmp1[v2] + tmp_v2[v1] + tmp_v1[N])

if ans >= INF :
    print (-1)
else :
    print (ans)