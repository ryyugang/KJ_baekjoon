import sys
input = sys.stdin.readline
N, K = map(int, input().split())
ans = 0
coins = []
for _ in range (N) :
    coins.append(int(input()))

for coin in reversed (coins) :
    ans += K // coin
    K = K % coin

print (ans)