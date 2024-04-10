import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range (M) :
    data = input().strip().split()
    if len(data) == 2 :
        Instruction = data[0]
        number = int(data[1])
    else :
        Instruction = data[0]
    
    if Instruction == 'add' :
        S.add(number)
    
    if Instruction == 'remove' :
        S.discard(number)
            
    if Instruction == 'check' :
        if number in S :
            print (1)
        else :
            print (0)
            
    if Instruction == 'toggle' :
        if number in S :
            S.remove(number)
        else :
            S.add(number)
            
    if Instruction == 'all' :
        S = set(range(1, 21))
            
    if Instruction == 'empty' :
        S = set()