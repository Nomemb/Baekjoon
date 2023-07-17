N = int(input())
time = [0 for _ in range(10001)]
dp = [0 for _ in range(10001)]

s = [0]
for i in range(N):
    array = list(map(int, input().split()))
    time[i + 1] = array[0]

    if len(array) > 2:
        a = array[2:]
        for j in range(len(a)):
            a[j] = time[a[j]]
        time[i + 1] = max(a) + array[0]

print(max(time))
