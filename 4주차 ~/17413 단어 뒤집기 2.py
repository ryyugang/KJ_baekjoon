import sys
input = sys.stdin.readline

S = input().strip()

stack = []
tag = False
result = ""

for x in S:
    if x == '<':
        while stack:
            result += stack.pop()
        tag = True
        result += x
    elif x == '>':
        tag = False
        result += x
    elif x == ' ':
        if not tag:
            while stack:
                result += stack.pop()
            result += x
        else:
            result += x
    else:
        if tag:
            result += x
        else:
            stack.append(x)

while stack:
    result += stack.pop()

print(result)