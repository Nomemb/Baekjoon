import sys
from collections import deque
input = sys.stdin.readline
R, C = map(int, input().split())

swans = []
lake = []
for i in range(R):
    l = list(input().strip())
    if 'L' in l:
        swans.append((i, l.index('L')))
    lake.append(l)

day = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs():
    start = swans[0]
    end = swans[1]
    visited = [[False] * C for _ in range(R)]
    dq = deque()
    dq.append(start)

    while dq:
        x, y = dq.popleft()
        visited[x][y] = True

        if x == end[0] and y == end[1]:
            return True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and lake[nx][ny] != 'X':
                    dq.append((nx,ny))
                    visited[nx][ny] = True

    return False


def melt():
    melt_lake = set()
    for i in range(R):
        for j in range(C):
            if lake[i][j] == 'X':
                for w in range(4):
                    nx = i + dx[w]
                    ny = j + dy[w]

                    if 0 <= nx < R and 0 <= ny < C:
                        if lake[nx][ny] == '.' and (i,j) not in melt_lake:
                            melt_lake.add((i,j))

    for i in range(R):
        for j in range(C):
            if (i,j) in melt_lake:
                lake[i][j] = '.'


while True:
    if bfs():
        break

    day += 1
    melt()

print(day)


