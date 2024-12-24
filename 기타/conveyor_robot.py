from collections import deque

N, K = map(int, input().split())
belts = list(map(int,input().split()))

robots = deque()
cnt = 0


def turn():
    global belts
    global robots

    temp = belts[:]
    for i in range(len(belts)):
        temp[i] = belts[(2*N + i - 1) % (2*N)]

    # 1. 벨트 이동
    belts = temp[:]
    for i in range(len(robots)):
        # 일단 로봇도 같이 이동
        robots[i] = (robots[i] + 1) % (2*N)


def robot_move():
    for i in range(len(robots)):
        pass
    return None


def act():
    global cnt
    # 1. 각 칸 위에 있는 로봇과 함께 한 칸 회전
    turn()

    # 2. 먼저 올라간 로봇부터 회전방향으로 한칸 이동할 수 있다면 이동
    robot_move()

    # 0번에 올릴 수 있으면 로봇 넣기
    if belts[0] > 0:
        robots.append(0)
        cnt += 1
    else:
        print(cnt)


act()
act()
act()
act()