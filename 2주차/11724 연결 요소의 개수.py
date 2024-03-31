import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
edges = []

for i in range (M) :
    a, b = map(int, input().split())
    edges.append((a, b))

set_list = [0] * (N + 1)

for j in range (1, N + 1) :
    set_list[j] = j
    
def find (parent, x) :
    if parent[x] != x :
        parent[x] = find (parent, parent[x])
    return parent[x]


def union (parent, x, y) :
    x = find (parent, x)
    y = find (parent, y)
    if x > y :
        parent[x] = y
    else :
        parent[y] = x

for edge in edges :
    a, b = edge
    if find (set_list, a) != find (set_list, b) :
        union (set_list, a, b)
    
for l in range (1, N + 1) :
    find (set_list, l)

res = []
for k in set_list :
    if k not in res and k != 0:
        res.append(k)
        
print (len(res))