# https://www.acmicpc.net/problem/2961

N = int(input())

sourness = []
bitterness = []

min_value = 1_000_000_000

for _ in range(N):
    s, b = map(int, input().split())
    sourness.append(s)
    bitterness.append(b)

for i in range(1, 1 << N):
    total_sourness = 1
    total_bitterness = 0

    for j in range(N):
        if i & (1 << j):
            total_sourness *= sourness[j]
            total_bitterness += bitterness[j]
            min_value = min(min_value, abs(total_bitterness - total_sourness))

print(min_value)
