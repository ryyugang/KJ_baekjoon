import sys
input = sys.stdin.readline

T = int(input())

for _ in range (T) :
    N = int(input()) 
    arr = []
    for _ in range (N) :
        a, b = map(int,input().split())
        arr.append((a, b))
    arr.sort()
    
    
    top = 0
    cnt = 1
    for i in range (1, N) :
        if arr[i][1] < arr[top][1] :
            cnt += 1
            top = i

    print (cnt)