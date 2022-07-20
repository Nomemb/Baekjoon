n,k = map(int,input().split())
coin = [int(input()) for i in range(n)]
dp = [10001 for i in range(k+1)]
dp[0] = 0

for i in range(1,k+1):
    for c in coin:
        if i>=c:
            dp[i] = min(dp[i], dp[i-c]+1)

print(-1 if dp[k] == 10001 else dp[k])