import sys
input = sys.stdin.readline

class Stack :
    def __init__(self) :
        self.items= []
    
    def push (self, item) :
        self.items.append(item)
        
    def pop (self) :
        if self.empty() == 0 :
            return self.items.pop()
        else :
            raise IndexError("스택이 비어있따")
        
    def size (self) :
        return len(self.items)
        
    def empty (self) :
        if self.size() == 0 :
            return 1
        else :
            return 0
    
    def peek (self) :
        if self.empty() == 0 :
            return self.items[-1]
        else :
            return -1

N = int(input())
stack = Stack ()
command = ""


for i in range (N) :
    command = input().strip().lower().split()
    Instruction = command[0]
    if len(command) > 1 :
        number = command[1]
    
    if Instruction == 'push' :
        try :
            stack.push(int(number))
        except ValueError :
            print ('다시')
    elif Instruction == 'pop' :
        try :
            print (stack.pop())
        except IndexError :
            print (-1)
    elif Instruction == 'size' :
        print (stack.size())
    elif Instruction == 'empty' :
        print (stack.empty())
    elif Instruction == 'top' :
        print (stack.peek())
        