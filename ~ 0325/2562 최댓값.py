list = []

for i in range (9) :
    list.append(int(input()))
    
M = max(list)    
print (M)
print (list.index(M) + 1)