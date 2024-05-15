import sys
input = sys.stdin.readline

N = int(input())

for _ in range (N) :
    arr = list(input().split())
    for word in arr :
        print (word[::-1], end= " ")