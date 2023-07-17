# https://www.acmicpc.net/problem/9934
# 완전 이진 트리

K = int(input())
building = list(map(int, input().split()))
tree = [[] for _ in range(K)]


def dfs(building, depth):
    mid = len(building) // 2
    tree[depth].append(building[mid])

    if len(building) == 1:
        return
    dfs(building[:mid], depth + 1)
    dfs(building[mid + 1:], depth + 1)


dfs(building, 0)

for i in tree:
    print(*i)
