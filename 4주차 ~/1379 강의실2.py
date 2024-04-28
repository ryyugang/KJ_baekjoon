# import sys
# import heapq
# input = sys.stdin.readline

# N = int(input())
# time = []

# for _ in range (N) :
#     a, b, c = map(int, input().split())
#     time.append((a, b, c))

# time.sort(key = lambda x : (x[1]))

# cnt = 0
# queue = []
# num = [0] * (N + 1)

# for lecture, start, end in time :
#     if queue and queue[0][2] <= start :
#         num[lecture] = num[queue[0][0]]
#         heapq.heappop(queue)
#     else :
#         cnt += 1
#         num[lecture] = cnt
    
#     heapq.heappush(queue, [lecture, start, end])

# print (cnt)
# for i in num[1 :] :
#     print (i)

import sys
import heapq
input = sys.stdin.readline

N = int(input())
time = []

for _ in range (N) :
    a, b, c = map(int, input().split())
    time.append((a, b, c))

time.sort(key = lambda x : x[1])

room = []
for i in range (1, N + 1) :
    heapq.heappush(room, i)

lecture = [0] * (N + 1)
queue = []

for x in time :
    while queue and queue[0][0] <= x[1] :
        end, r = heapq.heappop(queue)
        heapq.heappush(room, r)
        
    r = heapq.heappop(room)
    heapq.heappush(queue, [x[2], r])
    lecture[x[0]] = r

print (max(lecture))
for k in lecture[1 :] :
    print (k)