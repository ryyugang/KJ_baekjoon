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
    while queue and queue[0][1] < i[0] :
        heapq.heappop(queue)
        print (queue)
    
    heapq.heappush(queue, i)
    