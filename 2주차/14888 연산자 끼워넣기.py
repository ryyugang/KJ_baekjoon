import sys
input = sys.stdin.readline
sys.setrecursionlimit (10**6)

N = int(input())
number = list(map(int, input().split()))
giho = list(map(int, input().split()))

minimum = float('inf')
maximum = -float('inf')

def dfs (depth, total, plus, minus, multiply, divide) :
    global maximum, minimum
    
    if depth == N :
        maximum = max (total, maximum)
        minimum = min (total, minimum)
        return
    
    if plus :
        dfs (depth + 1, total + number[depth], plus - 1, minus, multiply, divide)
    if minus :
        dfs (depth + 1, total - number[depth], plus, minus - 1, multiply, divide)
    if multiply :
        dfs (depth + 1, total * number[depth], plus, minus, multiply - 1, divide)
    if divide : 
        dfs (depth + 1, int(total / number[depth]), plus, minus, multiply, divide - 1)
        
dfs(1, number[0], giho[0], giho[1], giho[2], giho[3])
print (maximum)
print (minimum)