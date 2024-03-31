nanjaang = [int(input()) for _ in range(9)]
seven_nanjaang = []


def dfs(depth, start):
    if depth == 7:
        if sum(seven_nanjaang) == 100:
            for i in sorted(seven_nanjaang):
                print(i)
            exit()
        else:
            return

    for i in range(start, 9):
        seven_nanjaang.append(nanjaang[i])
        dfs(depth + 1, i + 1)
        seven_nanjaang.pop()


dfs(0, 0)
