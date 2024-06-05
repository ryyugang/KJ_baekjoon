import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ans = [-1] * N
idx = []
cnt = [0] * 1_000_001

for num in A :
    cnt[num] += 1

for i in range (N) :
    while idx and cnt[A[idx[-1]]] < cnt[A[i]] :
        ans[idx.pop()] = A[i]
    idx.append(i)

print (*ans)