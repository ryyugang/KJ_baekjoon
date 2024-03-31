import sys
input = sys.stdin.readline

N, K = map(int, input().split())
queue = list(i+1 for i in range (N))
arr = []
J = 0

while queue :
    J += K - 1
    if J >= len(queue) :
        J %= len(queue)
    arr.append(queue.pop(J))

print ('<' + ', '.join(map(str,arr)) + '>')