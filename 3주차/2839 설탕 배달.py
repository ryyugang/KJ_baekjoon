import sys
input = sys.stdin.readline

N = int(input())
arr = [3, 5]
ans = 0

while N >= 0 :
    if (N % 5) == 0 :
        ans += N // 5
        print (ans)
        break
    elif N >= 3 and (N % 5) != 0 :
        N -= 3
        ans += 1
    else :
        print (-1)
        break