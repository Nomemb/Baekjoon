ans = []
max = 1000001
f = [1] * max
g = [0] * max

for i in range(2, max):
    j = 1
    while i * j <= max - 1:
        f[i * j] += i
        j += 1

for i in range(1, max):
    g[i] = g[i - 1] + f[i]

T = int(input())
for _ in range(T):
    N = int(input())
    ans.append(g[N])
print(*ans, sep='\n')
