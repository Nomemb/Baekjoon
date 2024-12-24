# https://www.acmicpc.net/problem/16236

N = int(input())

grounds= []
shark = []
for i in range(N):
    ground = list(map(int, input().split()))
    grounds.append(ground)

    for j in range(len(ground)):
        if ground[j] == 9:
            shark = [[i,j]]

