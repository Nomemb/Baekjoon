# https://www.acmicpc.net/problem/2512

N = int(input())
array = list(map(int, input().split()))
M = int(input())
max = 0
array.sort()
ans = 0


def solve(start, end):
    global ans
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for i in range(len(array)):
            if array[i] >= mid:
                sum += mid
            else:
                sum += array[i]

        if sum > M:
            end = mid - 1
        else:
            start = mid + 1
            ans = mid if mid > ans else ans

    return ans


print(solve(0, array[-1]))
