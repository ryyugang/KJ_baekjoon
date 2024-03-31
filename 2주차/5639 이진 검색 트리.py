import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []

while True :
    try :
        a = int(input())
        arr.append(a)
    except :
        break
            
    

def search (list) :
    
    if not list :
        return
    
    root = list[0]
    left, right = [], []
    
    for i in list[1:] :
        if i > root :
            right.append(i)
        else :
            left.append(i)
            
    search (left)
    search (right)
    print (root)


search (arr)