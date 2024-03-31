import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
M = int(input())
edges = []

for i in range (M) :
    a, b = map(int, input().split())
    edges.append ((a, b))
    
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
    c, d = edge
    union (set_list, c, d)
        
for l in range (1, N + 1) :
    find (set_list, l)

print (set_list.count(set_list[1]) - 1)