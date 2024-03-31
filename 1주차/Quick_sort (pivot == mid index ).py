numbers = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort (arr, left, right) :
    
    if len(arr) < 2 :
        return arr
    
    pl = left
    pr = right
    pivot = arr[(left + right) // 2]
    
    while pl <= pr :
        while arr[pl] < pivot :
            pl += 1
        while arr[pr] > pivot :
            pr -= 1
        if pl <= pr :
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
            
    if left < pr :
        quick_sort(arr, left, pr)
    if pl < right :
        quick_sort(arr, pl, right)
        
quick_sort(numbers, 0, len(numbers) - 1)
print (numbers)