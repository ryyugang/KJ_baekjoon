import sys
input = sys.stdin.readline
sys.setrecursionlimit (10**6)

N = int(input())

arr = [0, 1]
ans = 0

def fibonacci () :
    global ans
    if 0 < N <= 90 :
        for i in range (2, N + 1) :            
                ans = arr[-1] + arr[-2]
                arr.append(ans)
                
    return arr[-1]

fibonacci()
print (arr[-1])