def binary_search(index, arr):
    left, right = 0, len(arr) - 1

    while right >= left:
        mid = (left + right) // 2
        if arr[mid] == index:
            return 1
        elif arr[mid] < index:
            left = mid + 1
        else:
            right = mid - 1
    return 0


N = int(input())
temp1 = list(map(int, input().split()))
temp1.sort()

M = int(input())
temp2 = list(map(int, input().split()))

for i in range(M):
    print(binary_search(temp2[i], temp1))
