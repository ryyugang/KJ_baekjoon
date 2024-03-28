def check_sosu(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


N = int(input())

for i in range(N):
    num = int(input())

    a = num // 2
    b = num // 2

    for i in range(num // 2):
        if check_sosu(a) and check_sosu(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
