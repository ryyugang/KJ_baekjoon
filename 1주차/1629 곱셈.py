import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
A = numbers[0]
B = numbers[1]
C = numbers[2]

def Mod (A, B, C) :
    if B == 1 :
        return A % C
    elif B % 2 == 0 :
        return (Mod(A, B // 2, C) ** 2 % C)
    else :
        return ((Mod(A, B // 2, C) ** 2 * A) % C)
    
print (Mod(A,B,C))