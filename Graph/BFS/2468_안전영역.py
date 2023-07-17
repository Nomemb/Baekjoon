from collections import deque


def BFS(x, y, w):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > w and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


result = 0
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

max_h = max(map(max, graph))
for w in range(max_h):
    visited = [[0] * N for i in range(N)]
    c = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > w and visited[i][j] == 0:
                BFS(i, j, w)
                c += 1
    if result < c:
        result = c

print(result)
