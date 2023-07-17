# https://www.acmicpc.net/problem/14888
N = int(input())
A = list(map(int, input().split()))
a, s, m, d = map(int, input().split())

min_, max_ = 1e9, -1e9


def dfs(i, res, a, s, m, d):
    global max_, min_
    if i == N:
        max_ = max(res, max_)
        min_ = min(res, min_)
        return
    else:
        if a:
            dfs(i + 1, res + A[i], a - 1, s, m, d)
        if s:
            dfs(i + 1, res - A[i], a, s - 1, m, d)
        if m:
            dfs(i + 1, res * A[i], a, s, m - 1, d)
        if d:
            dfs(i + 1, int(res / A[i]), a, s, m, d - 1)


dfs(1, A[0], a, s, m, d)
print(max_)
print(min_)
