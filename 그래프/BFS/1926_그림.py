from collections import deque
import queue

n,m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

def BFS(y,x):
    count = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    queue.append((y,x))
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx, ny = x+ dx[i], y+ dy[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny,nx))
                    count += 1
    return count

cnt, max_count = 0,0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_count = max(max_count, BFS(i,j))

print(cnt)
print(max_count)