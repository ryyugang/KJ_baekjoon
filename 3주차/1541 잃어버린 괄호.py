import sys
input = sys.stdin.readline

arr = input().strip().split('-')
ans = 0

for i in arr[0].split('+') :
    ans += int(i)

for j in arr[1 :] :
    for k in j.split('+') :
        ans -= int(k)
        
print (ans)