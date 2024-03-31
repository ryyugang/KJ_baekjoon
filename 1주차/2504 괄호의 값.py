import sys
input = sys.stdin.readline

arr = [_ for _ in input().strip()]
stack = []


ans = 1
res = 0

for i in range (len(arr)) :
    
    if arr[i] == '(' :
        ans *= 2
        stack.append(arr[i])
    elif arr[i] == '[' :
        ans *= 3
        stack.append(arr[i])
    elif arr[i] == ')' :
        if not stack or stack[-1] == '[' :
            res = 0
            break
        if arr[i-1] == '(' :
            res += ans
        stack.pop()
        ans //= 2
    elif arr[i] == ']' :
        if not stack or stack[-1] == '(' :
            res = 0
            break
        if arr[i-1] == '[' :
            res += ans
        stack.pop()
        ans //= 3
    
if stack :
    print (0)
else :
    print (res)