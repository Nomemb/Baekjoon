# https://www.acmicpc.net/problem/3190

from collections import deque

n = int(input())
k = int(input())  # 사과 개수

board = [[False] * n for _ in range(n)]
snake = deque()
snake.append((0,0))

direction = [
    (0,1), # 우(기본값)
    (1,0), # 하
    (0,-1),# 좌
    (-1,0)  # 상
]
nextDir = 0
second = 0
order = []

for i in range(k):
    row, col = map(int, input().split()) # 사과 위치
    board[row-1][col-1] = True           # 사과가 있으면 True로 표시

l = int(input())  # 방향
for i in range(l):
    order.append(input().split())

while True:
    second += 1
    head = (snake[0][0]+direction[nextDir][0], snake[0][1]+direction[nextDir][1])
    # 종료 조건 ( 몸통과 닿거나, 맵 밖으로 나갈 때)
    if head in snake or head[0] < 0 or head[0] >= n or head[1] < 0 or head[1] >= n:
        print(second)
        break

    snake.appendleft(head)
    if not board[snake[0][0]][snake[0][1]]:
        snake.pop()
    else:
        board[snake[0][0]][snake[0][1]] = False
    
    if order and second == int(order[0][0]):
        if order[0][1] == "L":
            nextDir = (nextDir - 1)%4
        else:
            nextDir = (nextDir + 1)%4
        order.pop(0)
