# https://www.acmicpc.net/problem/21608

N = int(input())

students = []
seats = [[0] * (N+1) for _ in range(N+1)]

# 입력
for i in range(N**2):
    student = list(map(int, input().split()))
    students.append(student)

# 자리 판별용
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def check_seat(row, col, student):
    cnt_nearest_favorite = 0
    cnt_nearest_null = 0

    for idx in range(4):
        nx = row + dx[idx]
        ny = col + dy[idx]

        if 0 < nx <= N and 0 < ny <= N:
            if seats[nx][ny] == 0:
                cnt_nearest_null += 1

            if seats[nx][ny] in students[student][1:]:
                cnt_nearest_favorite += 1

    return cnt_nearest_favorite, cnt_nearest_null


def confirm_seat(lst, student):
    row = lst[0][0]
    col = lst[0][1]

    seats[row][col] = students[student][0]


def print_seat():
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(seats[i][j], end=" ")
        print()
    print()


def compute_score():
    total_score = 0
    score_rank = [0, 1, 10, 100, 1000]

    temp_students = students[:]
    temp_students.sort(key=lambda x: x[0])

    for i in range(1, N+1):
        for j in range(1, N+1):
            temp_student = seats[i][j]
            score = 0

            for w in range(4):
                nx = i + dx[w]
                ny = j + dy[w]

                if 0 < nx <= N and 0 < ny <= N:
                    if seats[nx][ny] in temp_students[temp_student-1][1:]:
                        score += 1

            total_score += score_rank[score]

    return total_score


# 자리 앉기 로직
for student in range(N**2):
    max_cnt_nearest_favorite = 0
    max_cnt_nearest_null = 0

    lst_nearest_favorite = []

    for row in range(1,N+1):
        for col in range(1,N+1):
            if seats[row][col] == 0:
                cnt_nearest_favorite, cnt_nearest_null = check_seat(row, col, student)

                # 현재 seats[col][row]의 좋아하는 학생 인접수가 가장 많다면
                if max_cnt_nearest_favorite < cnt_nearest_favorite:
                    max_cnt_nearest_favorite = cnt_nearest_favorite

                    # 저장해놨던 목록 초기화
                    lst_nearest_favorite = [[row, col, cnt_nearest_null]]

                # 현재 좋아하는 학생 인접수가 최고치랑 동일하다면
                elif max_cnt_nearest_favorite == cnt_nearest_favorite:
                    lst_nearest_favorite.append([row, col, cnt_nearest_null])

    # 1번 조건을 만족하는 칸이 하나일 경우
    if len(lst_nearest_favorite) == 1:
        confirm_seat(lst_nearest_favorite, student)

    else:
        lst_nearest_favorite.sort(key=lambda x: x[2], reverse=True)

        max_cnt_nearest_null = lst_nearest_favorite[0][2]

        # 1번 조건 만족하는 여러 칸 중 비어있는 칸 가장 많은 칸만 남기기
        lst_nearest_favorite = [result for result in lst_nearest_favorite if result[2] == max_cnt_nearest_null]

        # 2번 조건 만족
        if len(lst_nearest_favorite) == 1:
            confirm_seat(lst_nearest_favorite, student)

        # 3번 조건 만족
        else:
            lst_nearest_favorite.sort(key=lambda x: (x[0],x[1]))
            confirm_seat(lst_nearest_favorite, student)

print(compute_score())

