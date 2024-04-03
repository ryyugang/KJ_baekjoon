import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit (10**6)

INF = float('inf')
N = int(input())
M = int(input())
edges = [[] for _ in range (N + 1)]

for i in range (1, M + 1) :
    a, b, cost = map(int, input().split())
    edges[a].append((cost, b))

edges_cost = [INF for _ in range (N + 1)]

start, last = map(int, input().split())

def dijkstra (x) :
    edges_cost[x] = 0
    queue = [[0, x]]
    
    while queue :
        cost, node = heapq.heappop(queue)
        if cost > edges_cost[node] :
            continue
        
        for n_cost, n_node in edges[node] :
            if edges_cost[n_node] > edges_cost[node] + n_cost :
                edges_cost[n_node] = edges_cost[node] + n_cost
                heapq.heappush(queue, [edges_cost[n_node] , n_node])

    return edges_cost

dijkstra (start)

print (edges_cost[last])