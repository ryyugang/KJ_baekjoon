import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

if M != 0 :
    arr = list(input().split())
else :
    arr = []
    
ans = abs(100 - N)

for i in range (1_000_001) :
    for j in str(i) :
        if j in arr :
            break
    else :
        ans = min(ans, len(str(i)) + abs(i - N))
        
print (ans)