# 시간초과 때문에 pypy3으로 제출함
import copy
from collections import deque

max_Area = 0


def BFS():
    global max_Area

    queue = deque()
    temp_graph = copy.deepcopy(graph)

    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                queue.append((nx, ny))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                cnt += 1
    max_Area = max(max_Area, cnt)


def makeWall(count):
    if count == 3:
        BFS()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(count + 1)
                graph[i][j] = 0


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

makeWall(0)
print(max_Area)
