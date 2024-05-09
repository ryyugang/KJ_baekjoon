import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = list(int(input()) for _ in range (K))


def calculate (mid) :
    total = 0
    for x in arr :
        diff = x // mid
        total += diff
    return total

def solve () :
    left, right = 1, max(arr)
    
    while left <= right :
        mid = (left + right) // 2
        total = calculate(mid)
    
        if total < N :
            right = mid - 1
        else :
            left = mid + 1
    
    return right

print (solve())