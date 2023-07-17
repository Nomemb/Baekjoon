T = int(input())
DP = [0 for i in range(1000001)]
DP[0], DP[1], DP[2] = 1, 1, 2
l = []
for i in range(T):
    n = int(input())
    l.append(n)

for i in range(3, max(l) + 1):
    DP[i] = (DP[i - 1] + DP[i - 2] + DP[i - 3]) % 1000000009
for i in l:
    print(DP[i])
