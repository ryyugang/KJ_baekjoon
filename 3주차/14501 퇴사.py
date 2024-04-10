import sys
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range (N)]

dp = [0] * (N + 1)

for i in range (N) :
    for j in range (i + data[i][0], N + 1) :
        if dp[j] < dp[i] + data[i][1] :
            dp[j] = dp[i] + data[i][1]

print (max(dp))