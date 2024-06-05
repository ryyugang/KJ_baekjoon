import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ans = [-1] * N
idx = []

for i in range (N) :
    while idx and A[idx[-1]] < A[i] :
        ans[idx.pop()] = A[i]
    idx.append(i)

print (*ans)