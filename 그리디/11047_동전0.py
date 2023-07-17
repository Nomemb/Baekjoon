N, K = map(int, input().split())
price = []
for i in range(N):
    price.append(int(input()))

price.reverse()
count = 0
for i in range(N):
    if (price[i] <= K):
        c = K // price[i]
        K -= c * price[i]
        count += c

print(count)
