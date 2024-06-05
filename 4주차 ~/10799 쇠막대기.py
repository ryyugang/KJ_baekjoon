import sys
input = sys.stdin.readline

tmp = list(input().strip())
stack = []
cnt = 0

for x in range(len(tmp)) :
    if tmp[x] == "(" :        
        stack.append("(")
    elif tmp[x] == ")" and tmp[x-1] == "(" : # 레이저
        stack.pop()
        cnt += len(stack)                    # 쇠막대기 개수만큼 컷
    else :
        stack.pop()
        cnt += 1                             # 쇠막대기

print (cnt)