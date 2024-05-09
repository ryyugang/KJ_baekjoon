import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = []

for i in range (N) :
    arr.append(int(input()))

arr.sort()

mean = round(sum(arr) / N)
median = arr[N // 2]

print (mean)
print (median)

tmp = list(set(arr))
# cnt_tmp = {}
# for num in tmp :
#     cnt_tmp[num] = arr.count(num)
# cnt = sorted(cnt_tmp.items(), key = lambda x : (-x[1], x[0]))

cnt = sorted(Counter(arr).items(), key = lambda x : (-x[1], x[0]))

if len(cnt) > 1 and cnt[0][1] == cnt[1][1] : # len(cnt) > 1 조건 중요
    print (cnt[1][0])
else :
    print (cnt[0][0])
    
print (max(arr) - min(arr))

