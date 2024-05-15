import sys
input = sys.stdin.readline

N = int(input())

for _ in range (N) :
    ans = 0
    arr = list(input().strip())
    
    for i in range (len(arr)) :
        if arr[i] == "(" :
            ans += 1
        else :
            ans -= 1
            
        if ans < 0 :
            break
            
    if ans == 0 :
        print ("YES")
    else :
        print ("NO") 