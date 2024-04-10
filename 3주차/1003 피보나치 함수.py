T = int(input())
arr = [0, 1]

def fib (N) :
    if 0 <= N <= 40 :
        for i in range (2, N + 1) :
            ans = arr[-1] + arr[-2] 
            arr.append(ans)
    
    return arr

for _ in range (T) :
    N = int(input())
    result = fib(N)
    
    if N == 0 :
        print (result[1], result[0],end='\n')
    elif N == 1 :
        print (result[0], result[1],end='\n')
    else :
        print (result[N - 1], result[N],end='\n')