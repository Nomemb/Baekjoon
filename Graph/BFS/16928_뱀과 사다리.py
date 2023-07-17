from collections import deque


def BFS(graph):
    queue = deque()
    queue.append(1)

    while queue:
        x = queue.popleft()
        if x == 100:
            print(graph[100])
            return

        dx = [1, 2, 3, 4, 5, 6]
        for i in range(6):
            nx = x + dx[i]
            if nx < 101 and graph[nx] == 0:
                graph[nx] = graph[x] + 1
                if nx in ladder:
                    tmpx = ladder[nx]
                    if graph[tmpx] == 0:
                        graph[tmpx] = graph[nx]
                        queue.append(tmpx)

                elif nx in snake:
                    tmpx = snake[nx]
                    if graph[tmpx] == 0:
                        graph[tmpx] = graph[nx]
                        queue.append(tmpx)

                else:
                    queue.append(nx)


N, M = map(int, input().split())
graph = [0] * 101

ladder = {}
for i in range(N):
    l, h = map(int, input().split())
    ladder[l] = h
snake = {}
for i in range(M):
    h, l = map(int, input().split())
    snake[h] = l

BFS(graph)
