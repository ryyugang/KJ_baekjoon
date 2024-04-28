import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

res = 0
def check (x, y, length, res) :
    
    if length == 1 :
        return res
    
    half = length // 2
    cnt = half * half
    
    if r < x + half : 
        if c < y + half :
            return check (x, y, half, res)
        else :
            return check (x, y + half, half, res + cnt)
    else:
        if c < y + half :
            return check (x + half, y, half, res + 2*cnt)
        else :
            return check (x + half, y + half, half, res + 3*cnt)

print (check (0, 0, 2 ** N, 0))