def rotate(arr):
    n = len(arr)
    temp_arr = [[0] * n for _ in range(N)]

    for r in range(n):
        for c in range(n):
            temp_arr[c][n - 1 - r] = arr[r][c]

    return temp_arr


def solve(N, arr):
    cnt = 0
    for i in range(N):
        idx = 0
        can_cross = True
        bridge = [0] * N

        while idx < len(arr[i]) - 1:
            if abs(arr[i][idx] - arr[i][idx + 1]) > 1:
                can_cross = False
                break

            if arr[i][idx] == arr[i][idx + 1]:
                idx += 1
                continue

            if arr[i][idx] - 1 == arr[i][idx + 1]:
                if idx + L < len(arr[i]):
                    temp = set(arr[i][idx + 1: idx + L + 1])
                    if len(temp) != 1 or 1 in bridge[idx + 1: idx + L + 1]:
                        can_cross = False
                        break

                    bridge[idx + 1: idx + L + 1] = [1] * L
                    idx += L - 1

                else:
                    can_cross = False
                    break

            elif arr[i][idx] + 1 == arr[i][idx + 1]:
                if idx - L + 1 >= 0:
                    temp = set(arr[i][idx - L + 1: idx + 1])
                    if len(temp) != 1 or 1 in bridge[idx - L + 1: idx + 1]:
                        can_cross = False
                        break

                    bridge[idx - L + 1: idx + 1] = [1] * L

                else:
                    can_cross = False
                    break

            idx += 1

        if can_cross:
            cnt += 1

    return cnt


N, L = map(int, input().split())

grounds = []

for _ in range(N):
    ground = list(map(int, input().split()))
    grounds.append(ground)

cnt = 0

cnt += solve(N, grounds)
cnt += solve(N, rotate(grounds))
print(cnt)






