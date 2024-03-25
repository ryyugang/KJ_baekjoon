N = int(input())
list = []
for i in range(N):
    list.append(int(input()))

temp = 0

for i in range(N - 1):
    for j in range(N - 1):
        if list[j] > list[j + 1]:
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp

for k in list:
    print(k)
