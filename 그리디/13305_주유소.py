N = int(input())
road_length = list(map(int, input().split()))
price = list(map(int, input().split()))
min = price[0]
ans = price[0]*road_length[0]
for i in range(1,N-1):
    if price[i] < min:
        min = price[i]
    ans += road_length[i] * min

print(ans)
