# https://www.acmicpc.net/problem/10830

def pow_matrix(mat, num):
    if num == 1:
        for i in range(len(mat)):
            for j in range(len(mat)):
                mat[i][j] %= 1000
        return mat

    tmp = pow_matrix(mat, num//2)
    if num % 2:
        return mul_matrix(mul_matrix(tmp, tmp), mat)

    return mul_matrix(tmp, tmp)


def mul_matrix(mat_a, mat_b):
    length = len(mat_a)

    temp = [[0] * length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            for w in range(length):
                temp[i][j] += mat_a[i][w] * mat_b[w][j]
                temp[i][j] %= 1000

    return temp


N, B = map(int, input().split())

matrix = []
for _ in range(N):
    m = list(map(int, input().split()))

    matrix.append(m)

answer = pow_matrix(matrix, B)

for i in range(N):
    print(*answer[i])

