import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range (n) :
    arr.append(int(input()))
    
arr1 = []
arr2 = []
cnt = 1

for num in arr :
    while cnt <= num :
        arr1.append(cnt)
        arr2.append("+")
        cnt += 1
    
    if arr1[-1] == num :
        arr1.pop()
        arr2.append("-")
    else :
        print("NO")
        exit()

for ans in arr2 :
    print (ans)