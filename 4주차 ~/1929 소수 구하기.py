import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def check_sosu(n) :
    if n == 1 :
        return False
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0 :
            return False
    
    return True

x = M

while (x <= N) :
    if check_sosu(x) == True :
        print (x)
    x += 1