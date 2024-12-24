# https://www.acmicpc.net/problem/15686
from itertools import combinations

N, M = map(int, input().split())

grounds = []

houses = []
chickens = []

for i in range(N):
    ground = list(map(int, input().split()))
    grounds.append(ground)

    for j in range(len(ground)):
        if ground[j] == 1:
            houses.append([i, j])

        if ground[j] == 2:
            chickens.append([i, j])

min_distance = 1e9

opened = [False] * len(chickens)
visited = set()


def calculate_distance(house, chicken):
    distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
    return distance


def total_distance(comb):
    result = 0
    for house_idx in range(len(houses)):
        temp_distance = 1e9
        for chicken in comb:
            temp_distance = min(temp_distance,
                                calculate_distance(houses[house_idx], chicken))

        result += temp_distance
    return result


combinations = list(combinations(chickens, M))
for i in range(len(combinations)):
    min_distance = min(min_distance, total_distance(combinations[i]))

print(min_distance)