from sys import stdin

n = int(input())

visited = []
for _ in range(n):
    l = list(map(int, stdin.readline().split()))
    visited.append(l)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if visited[i][k] and visited[k][j]:
                visited[i][j] = 1

for i in range(n):
    print(*visited[i][:])
