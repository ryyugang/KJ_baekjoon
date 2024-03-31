import sys


def calculate(tree_list, mid):
    total = 0
    for tree in tree_list:
        diff = tree - mid
        if diff > 0:
            total += diff
    return total


def search_tree(tree_list, M):
    left, right = 0, max(tree_list)

    while left <= right:
        mid = (left + right) // 2
        total = calculate(tree_list, mid)

        if total == M:
            return mid
        elif total < M:
            right = mid - 1
        else:
            left = mid + 1

    return right


N, M = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))
tree_list.sort()

print(search_tree(tree_list, M))
