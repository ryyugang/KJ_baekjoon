import sys

N = int(sys.stdin.readline())
word = []

for i in range(N):
    word.append(sys.stdin.readline().strip())

word = list(set(word))
word.sort()
word.sort(key=len)

for i in word:
    print(i)
