# https://www.acmicpc.net/problem/16235
import sys
from collections import deque

N, M, K = map(int, input().split())
input = sys.stdin.readline

ground = [[5] * N for _ in range(N)]
nutrient = [list(map(int, input().split())) for _ in range(N)]

trees = [[deque() for _ in range(N)] for _ in range(N)]

death_tree = []
for _ in range(M):
    x, y, age = map(int, input().split())

    trees[x-1][y-1].append(age)

direction = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
)


def spring_summer():
    for i in range(N):
        for j in range(N):
            new_trees = deque()
            dead_amount = 0
            for age in trees[i][j]:
                if ground[i][j] >= age:
                    ground[i][j] -= age
                    new_trees.append(age+1)

                else:
                    dead_amount += age//2

            trees[i][j] = new_trees
            ground[i][j] += dead_amount


def fall_winter():
    temp_tree = []
    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for dir in direction:
                        nx, ny = i + dir[0], j + dir[1]
                        if not (0 <= nx < N and 0 <= ny < N):
                            continue
                        temp_tree.append((nx, ny))
            ground[i][j] += nutrient[i][j]

    for tree_pos in temp_tree:
        x, y = tree_pos[0], tree_pos[1]
        trees[x][y].appendleft(1)


for year in range(K):
    spring_summer()
    fall_winter()

cnt = 0
for i in range(N):
    for j in range(N):
        for tree in range(len(trees[i][j])):
            cnt += 1

print(cnt)