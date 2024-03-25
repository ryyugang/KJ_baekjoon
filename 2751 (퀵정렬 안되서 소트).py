import sys

n = int(input())
list = []

for i in range(n):
    list.append(int(sys.stdin.readline()))

sorted_list = sorted(list)

for i in sorted_list:
    print(i)
