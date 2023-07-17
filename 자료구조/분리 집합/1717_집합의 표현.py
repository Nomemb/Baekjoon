# https://www.acmicpc.net/problem/1717

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def find_parent(parents, k):
    if k != parents[k]:
        parents[k] = find_parent(parents, parents[k])
    return parents[k]


def union_parent(parents, x, y):
    x = find_parent(parents, x)
    y = find_parent(parents, y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    z, a, b = map(int, input().split())
    if z == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
