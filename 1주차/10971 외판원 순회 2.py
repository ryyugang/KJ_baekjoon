import sys


def TSP(start, now, cost, visited):
    global ans

    if len(visited) == N:
        if W[now][start] != 0:
            ans = min(ans, cost + W[now][start])
        return

    for next in range(N):
        if W[now][next] != 0 and next not in visited and cost < ans:
            visited.append(next)
            TSP(start, next, cost + W[now][next], visited)
            visited.pop()


N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = float("inf")

for i in range(N):
    TSP(i, i, 0, [i])
print(ans)