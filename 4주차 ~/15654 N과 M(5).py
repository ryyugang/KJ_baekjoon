import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
tmp = list(map(int, input().split()))
tmp.sort()
arr = []

def solve() :
    if len(arr) == M :
        print (' '.join(map(str, arr)))
        return
    
    for num in tmp :
        if num not in arr :
            arr.append(num)
            solve()
            arr.pop()
            
solve()