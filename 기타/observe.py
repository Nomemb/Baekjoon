# https://www.acmicpc.net/problem/15683

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())

office = []
cctvs = []
walls = []
answer = 1e9
for i in range(N):
    o = list(map(int, input().split()))
    office.append(o)

    for j in range(len(o)):
        if o[j] == 6:
            walls.append([i, j])

        elif o[j] > 0:
            cctvs.append([i, j, o[j]])


def observe(office, idx, direction):
    x, y = cctvs[idx][0], cctvs[idx][1]
    nx, ny = x + dx[direction], y + dy[direction]

    while 0 <= nx < N and 0 <= ny < M:
        if office[nx][ny] == 6:
            break

        if office[nx][ny] == 0:
            office[nx][ny] = '#'

        nx, ny = nx + dx[direction], ny + dy[direction]

    # for i in range(len(office)):
    #     print(office[i])
    # print()
    return office

def back_tracking(office, cnt):
    global answer
    if cnt == len(cctvs):
        zone_count = 0
        for i in range(len(office)):
            zone_count += office[i].count(0)

        answer = min(answer, zone_count)
        return

    origin = [arr[:] for arr in office]

    if cctvs[cnt][2] == 1:
        for i in range(4):
            office = observe(office, cnt, i)
            back_tracking(office, cnt + 1)
            office = [arr[:] for arr in origin]

    elif cctvs[cnt][2] == 2:
        for i in range(0, 3, 2):
            office = observe(observe(office, cnt, i), cnt, i + 1)
            back_tracking(office, cnt + 1)
            office = [arr[:] for arr in origin]

    elif cctvs[cnt][2] == 3:
        for i in range(2):
            for j in range(2):
                office = observe(observe(office, cnt, i), cnt, 3 - j)
                back_tracking(office, cnt + 1)
                office = [arr[:] for arr in origin]

    elif cctvs[cnt][2] == 4:
        for i in range(4):
            office = observe(observe(observe(office, cnt, i), cnt, (i+1)%4), cnt, (i+2)%4)
            back_tracking(office, cnt + 1)
            office = [arr[:] for arr in origin]

    else:
        office = observe(observe(observe(observe(office, cnt, 0), cnt, 1), cnt, 2), cnt, 3)
        back_tracking(office, cnt + 1)

back_tracking(office, 0)
print(answer)