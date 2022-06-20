import sys
input = sys.stdin.readline
N = int(input())
p = [list(map(int, input().split())) for i in range(N)]
m = [[0] * N for i in range(N)]

for i in range(1,N):
    for j in range(N-i):
        x = i+j
        m[j][x] = 2 ** 32
        for k in range(j,x):
            m[j][x] = min(m[j][x], m[j][k] + m[k+1][x] + p[j][0]*p[k][1]*p[x][1])

print(m)