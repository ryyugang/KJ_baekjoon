# 1 -> 11 -> 2 
import sys
input = sys.stdin.readline

N = int(input())
M = N
cnt = 0
ans = 0

while True :
    a = N // 10
    b = N % 10
    c = (a + b) % 10
    
    N = (10*b) + c
    cnt += 1
    
    if N == M :
        break
    
print (cnt)