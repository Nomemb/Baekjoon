n = int(input())

dp = [0] * (n+1)
if n == 0:
    print(0)
elif n < 3:
    print(1)
else:
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])
