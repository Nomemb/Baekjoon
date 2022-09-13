from math import inf

N,M = map(int, input().split())
friend = [[inf] * N for _ in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    friend[a-1][b-1] = 1
    friend[b-1][a-1] = 1

for k in range(N):
    friend[k][k] = 0
    for i in range(N):
        for j in range(N):
            friend[i][j] = min(friend[i][j], friend[i][k]+friend[k][j])

minValue = inf
ans = [0] * N
for i in range(N):
    sum = 0
    for j in range(N):
        sum += friend[i][j]
    ans[i] = sum
    if sum < minValue:
        minValue = sum

for i in range(N):
    if ans[i] == minValue:
        print(i+1)
        break
        