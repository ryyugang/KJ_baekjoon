import sys
input = sys.stdin.readline

N = int(input())
times = []

for _ in range (N) :
    a, b = map(int, input().split())
    times.append ((a, b))
        
times.sort(key = lambda x : (x[1], x[0]))
cnt = 1

end = times[0][1]
for i in range (1, N) :
    if times[i][0] >= end :
        cnt += 1
        end = times[i][1]
        
print (cnt)
