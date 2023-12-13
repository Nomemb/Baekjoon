# https://www.acmicpc.net/problem/1890

from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for i in range(n)]
visited = [[False]*n for i in range(n)]

start = (0,0)
answer = 0
dp[0][0] = 1
visited[0][0] = True
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            continue
        if visited[i][j]:
            cur = graph[i][j]
            if i+cur < n:
                if dp[i+cur][j] == 0:
                    dp[i+cur][j] = dp[i][j]
                else:
                    dp[i+cur][j] += dp[i][j]
                visited[i+cur][j] = True
            if j+cur < n:
                if dp[i][j+cur] == 0:
                    dp[i][j+cur] = dp[i][j]
                else:
                    dp[i][j+cur] += dp[i][j]
                visited[i][j+cur] = True

print(dp[n-1][n-1])