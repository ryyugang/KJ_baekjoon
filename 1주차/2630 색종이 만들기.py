import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range (N)]

    
cnt_blue = 0
cnt_white = 0

def check (x, y, length) :
    global cnt_blue, cnt_white, res    
    
    if length == 0 : # 더이상 쪼갤 수 없을때까지
        return
    
    res = 0 
    # 모든 위치를 탐색하는게 아님
    for i in range (x, x+length) :
        for j in range (y, y+length) :
            res += board[i][j] 
            
    if res == length*length :
        cnt_blue += 1
    elif res == 0 :
        cnt_white += 1
    else: 
        check (x, y, length // 2)
        check (x + length // 2, y, length // 2)
        check (x, y + length // 2, length // 2)
        check (x + length // 2, y + length // 2, length // 2)
        
check (0, 0, N)
print(cnt_white)
print(cnt_blue)