N = int(input())
K = int(input())
low = 1
high = K
ans = 0
while low <= high:
    count = 0
    mid = (low+high)//2
    for i in range(1,N+1):
        count += min(mid//i,N)
    if count < K:
        low = mid + 1
    else:
        ans = mid
        high = mid - 1
print(ans)