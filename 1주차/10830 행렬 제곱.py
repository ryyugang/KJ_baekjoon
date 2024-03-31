import sys
input = sys.stdin.readline

N, B = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range (N)]

def calculate (matrix1, matrix2) :
    new_matrix = [[0]* N for _ in range (N)]
    
    for row in range (N) :
        for col in range (N) :
            for i in range (N) :
                new_matrix[row][col] += matrix1[row][i] * matrix2[i][col]
                new_matrix[row][col] %= 1000
    
    return new_matrix

def sol (N, arr) :
    if N == 1 :
        return arr
    elif N % 2 == 0 :
        half = sol (N // 2, arr)
        return calculate (half, half)
    else :
        return calculate (arr, sol(N-1, arr))
        
result = sol (B, arr)

for i in range (N) :
    for j in range (N) :
        result [i][j] %= 1000


for i in result:
    print(*[j % 1000 for j in i])