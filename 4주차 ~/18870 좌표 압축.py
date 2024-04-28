import sys
import heapq
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
tmp = {}
for i, value in enumerate(sorted(set(arr))) :
    tmp[value] = i

arr = [tmp[x] for x in arr]

print (*arr)