# https://www.acmicpc.net/problem/14503

N, M = map(int, input().split())
r, c, direction = map(int, input().split())

grounds = []

for _ in range(N):
    ground = list(map(int, input().split()))
    grounds.append(ground)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def doing(row, col, direction):
    cnt = 0

    while True:
        if grounds[row][col] == 0:
            grounds[row][col] = -1
            cnt += 1

        else:
            is_cleaned = True
            for i in range(4):
                nx = row + dx[i]
                ny = col + dy[i]

                if 0 <= nx < N and 0 <= ny < M:
                    if grounds[nx][ny] == 0:
                        is_cleaned = False
                        break

            if is_cleaned:
                nx = row - dx[direction]
                ny = col - dy[direction]

                if 0 <= nx < N and 0 <= ny < M:
                    if grounds[nx][ny] != 1:
                        row, col = nx, ny
                        continue

                    else:
                        break

            else:
                direction = (direction + 3) % 4
                nx = row + dx[direction]
                ny = col + dy[direction]

                if 0 <= nx < N and 0 <= ny < M:
                    if grounds[nx][ny] == 0:
                        row, col = nx, ny

    return cnt


print(doing(r,c,direction))