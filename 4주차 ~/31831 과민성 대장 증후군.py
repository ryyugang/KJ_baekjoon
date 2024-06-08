import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tmp = list(map(int, input().split()))
tmp1 = [0] * N
a = 0
ans = 0

for x in range (N) :
    a += tmp[x]
    if a <= 0 :
        a = 0
    tmp1[x] = a

for num in tmp1 :
    if num >= M :
        ans += 1
        
print (ans)