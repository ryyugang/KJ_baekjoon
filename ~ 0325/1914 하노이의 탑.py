def hannoi(n, a, b):
    if n == 1:
        print(a, b)
        return
    hannoi(n - 1, a, 6 - a - b)
    print(a, b)
    hannoi(n - 1, 6 - a - b, b)


n = int(input())
print(2**n - 1)

if n <= 20:
    hannoi(n, 1, 3)
