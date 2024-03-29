n, k = map(int, input().split())
coin = [int(input()) for i in range(n)]

dp = [0 for i in range(k + 1)]
dp[0] = 1

for i in coin:
    for j in range(i, k + 1):
        if j >= i:
            dp[j] += dp[j - i]

print(dp[k])
