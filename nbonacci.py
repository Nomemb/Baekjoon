T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    pibo = [0] * K
    pibo[N - 1] = 1
    for i in range(N, K):
        for j in range(i - N, i):
            pibo[i] += pibo[j]
        pibo[i] %= 100000007
    print(pibo[K - 1])
