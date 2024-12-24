# https://www.acmicpc.net/problem/9576

import heapq

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    num_set = set([i for i in range(1, n+1)])
    cnt = 0
    hq = []
    for i in range(m):
        a, b = map(int, input().split())
        heapq.heappush(hq, (b, a))

    while hq:
        h = heapq.heappop(hq)
        start, end = h[1], h[0]

        for j in range(start, end+1):
            if j in num_set:
                cnt += 1
                num_set.remove(j)
                break

    print(cnt)