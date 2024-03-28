import sys
input = sys.stdin.readline

N, S = map(int,input().split())
arr = list(map(int, input().split()))
ans = []

cnt = 0
def check (depth, sum) :
    global cnt
    
    if depth >= N :
        return 0
    
    sum += arr[depth]
    if sum == S :
        cnt += 1
    
    check (depth + 1, sum)
    check (depth + 1, sum - arr[depth])

check (0,0)
print (cnt)