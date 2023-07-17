import sys

N, C = map(int, input().split())
house = []
ans = 0
house = sorted([int(sys.stdin.readline()) for _ in range(N)])


def solve(start, end):
    global ans
    while start <= end:
        count = 1
        mid = (start + end) // 2
        distance = house[0]
        for i in range(1, N):
            if house[i] - distance >= mid:
                count += 1
                distance = house[i]

        if count >= C:
            ans = ans if ans > mid else mid
            start = mid + 1
        else:
            end = mid - 1

    return ans


print(solve(1, house[-1] - house[0]))
