import sys
input = sys.stdin.readline

N, K = map(int, input().split())
queue = []
ans = []
idx = 0

for i in range (1, N + 1) :
    queue.append(i)
    
while queue :
    idx += K - 1
    if idx >= len(queue) :
        idx = idx % len(queue)
    ans.append(queue.pop(idx))

print ('<' + ', '.join(map(str, ans)) + '>')