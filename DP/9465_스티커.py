T = int(input())
for _ in range(T):
    n = int(input())
    a = []
    DP = [[0 for _ in range(3)] for _ in range(100001)]
    for _ in range(2):
        a.append(list(map(int, input().split())))
    for i in range(n):
        DP[i+1][0] = max(DP[i+1][0], max(DP[i][0], max(DP[i][1], DP[i][2])))
        DP[i+1][1] = max(DP[i+1][1], max(DP[i][0], DP[i][2]) + a[0][i])
        DP[i+1][2] = max(DP[i+1][2], max(DP[i][0], DP[i][1]) + a[1][i])
    print(max(DP[n][0], DP[n][1], DP[n][2]))
