import sys
import heapq
input = sys.stdin.readline

N = int(input())
time = []

for _ in range (N) :
    a, b, c = map(int, input().split())
    time.append((b, c))

time.sort(key = lambda x : (x[0]))

cnt = 0
queue = []

for i in time :
    while queue and queue[0] <= i[0] :
        heapq.heappop(queue)
    
    heapq.heappush(queue, i[1])
    cnt = max(cnt, len(queue))
    
print (cnt)