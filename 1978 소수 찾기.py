n = int(input())
s = list(map(int, input().split()))
cnt = 0

for i in s:
    if i == 1:
        continue

    for j in range(2, int(i)):
        if i % j == 0:
            break
    else:
        cnt += 1

print(cnt)
