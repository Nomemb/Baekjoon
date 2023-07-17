arr = []
N = int(input())

visited = [0 for _ in range(N)]
team = [0 for _ in range(N)]

for _ in range(N):
    arr.append(list(map(int, input().split())))


def solve(k):
    if k == N // 2:
        point_a = 0
        point_b = 0
        for i in range(N):
            for j in range(N):
                if visited[j] == 1:
                    point_a += arr[i][j]
                else:
                    point_b += arr[i][j]

        print(point_a - point_b)
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        team[k] = i
        solve(k + 1)
        visited[i] = 0


solve(0)
