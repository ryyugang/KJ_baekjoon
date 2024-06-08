import sys
input = sys.stdin.readline

N = int(input())
tmp = []

for i in range (N) :
    x, y = map(int, input().split())
    tmp.append((x, y))

tmp.sort(key = lambda x : (x[1], x[0]))

for res in tmp :
    print (*res)