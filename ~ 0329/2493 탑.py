import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = [0] * N
stack = []

for i in range (N) :
    while stack :
        if stack[-1][1] < arr[i] :
            stack.pop()
        else :
            result[i] = stack[-1][0] + 1
            break
    
    stack.append([i,arr[i]])
    
print (*result)