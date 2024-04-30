import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
tmp = list(map(int, input().split()))
tmp1 = sorted(list(set(tmp)))
tmp_dic = {}
tmp.sort()
arr = []

for num in tmp1 :
    tmp_dic[num] = tmp.count(num)
    
def solve() :
    if len(arr) == M :
        print (' '.join(map(str, arr)))
        return
    
    for num in tmp1 :
        if tmp_dic[num] > 0 :
            arr.append(num)
            # tmp_dic[num] -= 1
            solve()
            arr.pop()
            # tmp_dic[num] += 1

solve()