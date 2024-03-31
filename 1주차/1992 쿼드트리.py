N = int(input())
board = [list(map(int, input())) for _ in range (N)]
res = []

def check (x, y, length) :
    global res
    
    if length == 0 : 
        return
    
    res = 0 
    
    for i in range (x, x+length) :
        for j in range (y, y+length) :
            res += board[i][j] 
            
    if res == length*length :
        return '1'
    elif res == 0 :
        return '0'
    
    tmp = '('
    tmp += check (x, y, length // 2)
    tmp += check (x, y + length // 2, length // 2)
    tmp += check (x + length // 2, y, length // 2)
    tmp += check (x + length // 2, y + length // 2, length // 2)
    tmp += ')'
        
    return tmp

print (check (0, 0, N))