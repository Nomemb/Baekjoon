# https://www.acmicpc.net/problem/14501

N = int(input())
A = []
for i in range(N):
    T,P = map(int, input().split())
    A.append((T,P))

ans = [0]*(N+1)
for i in range(N):
    ans[i+1] = max(ans[i],ans[i+1])

    if i+A[i][0] <= N:
        ans[i+A[i][0]] = max(ans[i+A[i][0]], ans[i]+A[i][1])

print(ans[N])