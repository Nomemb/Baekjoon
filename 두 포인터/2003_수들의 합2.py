# https://www.acmicpc.net/problem/2003

N, M = map(int, input().split())
A = list(map(int, input().split()))

s, e, count = 0, 0, 0
for _ in range(N):
    e += 1
    while sum(A[s:e]) >= M:
        if sum(A[s:e]) == M:
            count += 1
        s += 1
print(count)
