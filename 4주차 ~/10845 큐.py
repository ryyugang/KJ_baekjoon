from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range (N) :
    instruction = input().strip().split()
    
    if instruction[0] == "push" :
        queue.append(instruction[1])
    elif instruction[0] == "pop" :
        if queue :
            print (queue.popleft())
        else :
            print ("-1")
    elif instruction[0] == "size" :
        print (len(queue))
    elif instruction[0] == "empty" :
        if queue :
            print ("0")
        else :
            print ("1")
    elif instruction[0] == "front" :
        if queue :
            print (queue[0])
        else :
            print ("-1")
    elif instruction[0] == "back" :
        if queue :
            print (queue[-1])
        else :
            print ("-1")