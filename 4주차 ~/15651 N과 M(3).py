import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = []

def solve() :
    if len(arr) == M :
        print (' '.join(map(str, arr)))
        return
    
    for i in range (1, N + 1) :
        arr.append(i)
        solve()
        arr.pop()
        
solve()