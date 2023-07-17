N, M = map(int, input().split())
array = list(map(int, input().split()))
start, end = sum(array) // M, sum(array)
ans = end

while start <= end:
    mid = (start + end) // 2
    sum = 0
    count = 0

    if mid < max(array):
        start = mid + 1
        continue

    for i in range(N):
        if array[i] > mid:
            break
        elif sum + array[i] <= mid:
            sum += array[i]
        else:
            sum = array[i]
            count += 1

    if count <= M - 1:
        end = mid - 1
        ans = min((mid, ans))

    else:
        start = mid + 1

print(ans)
