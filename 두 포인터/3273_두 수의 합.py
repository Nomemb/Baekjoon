# https://www.acmicpc.net/problem/3273

n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()
count = 0
for s in range(n):
    # 이진 탐색으로 찾아야 하므로 미리 빼줌
    k = x - a[s]
    # 배열의 첫 수를 미리 빼 줬기 때문에 두번째 인덱스부터 시작함
    l = s + 1
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == k:
            count += 1
            break
        elif a[m] < k:
            l = m + 1
        else:
            r = m - 1

print(count)
