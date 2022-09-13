from collections import deque


def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    count = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx,ny))
                count += 1
    return count
    
M,N,K = map(int, input().split())
graph = [[0]* N for i in range(M)]

 
for i in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            graph[y][x] = 1

result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = 1
            result.append(BFS(i,j))

result.sort()
print(len(result))
print(*result)
            
