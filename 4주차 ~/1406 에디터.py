import sys
input = sys.stdin.readline

arr = list(input().strip())
stack = []
M = int(input())

for _ in range (M) :
    instruction = input().strip().split()
    
    if instruction[0] == "L" :
        if arr :
            stack.append(arr.pop())
    elif instruction[0] == "D" :
        if stack :
            arr.append(stack.pop())
    elif instruction[0] == "B" :
        if arr :
            arr.pop()
    elif instruction[0] == "P" :
        arr.append(instruction[1])

print (''.join(arr + stack[::-1]))