# https://www.acmicpc.net/problem/1459
'''
X,Y : 집의 위치
W,S : 한 블록, 대각선 한 블록 가는데 걸리는 시간
시작점 : (0,0)
'''
X, Y, W, S = map(int, input().split())

if X > Y:
    X, Y = Y, X

# 경우의 수
# 대각선 이동이 손해일 때
if W * 2 < S:
    spend_time = (X+Y) * W
# 대각선 이동이 무조건 이득일 때
elif W < S:
    spend_time = X * S + (Y - X) * W
# 이외의 경우
else:
    if (X+Y) % 2 == 0:
        spend_time = Y * S
    else:
        spend_time = (Y-1) * S + W

print(spend_time)
