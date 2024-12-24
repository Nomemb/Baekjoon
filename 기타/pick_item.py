from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    ground = [[-1 for _ in range(102)] for i in range(102)]

    def make_square(rect):
        x1, y1, x2, y2 = map(lambda x: x * 2, rect)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    ground[i][j] = 0
                elif ground[i][j] != 0:
                    ground[i][j] = 1

    for rect in rectangle:
        make_square(rect)

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    x, y = characterX * 2, characterY * 2

    q = deque()

    visited = [[False for _ in range(102)] for i in range(102)]

    visited[x][y] = True
    q.append((x,y,0))

    while q:
        cur_x, cur_y, dist = q.popleft()

        if cur_x == itemX*2 and cur_y == itemY*2:
            return dist//2

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]

            if 0 <= nx < 102 and 0 <= ny < 102 and not visited[nx][ny]:
                if ground[nx][ny] == 1:
                    q.append((nx,ny,dist+1))
                    visited[nx][ny] = True


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],
         1,3,7,8) == 17)
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]],
         9,7,6,1) == 11)
print(solution([[1,1,5,7]],
         1,1,4,7) == 9)