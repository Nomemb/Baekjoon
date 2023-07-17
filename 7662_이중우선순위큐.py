# pypy3 성공, python3 실패
import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    h = []
    maxh = []
    visited = [False] * 1000001
    for i in range(k):
        operation = input().split()
        if operation[0] == 'I':
            num = int(operation[1])
            heapq.heappush(h, (num, i))
            heapq.heappush(maxh, (-num, i))
            visited[i] = True
        else:
            if len(h) == 0:
                pass
            elif operation[1] == '1':
                while maxh and not visited[maxh[0][1]]:
                    heapq.heappop(maxh)
                if maxh:
                    visited[maxh[0][1]] = False
                    heapq.heappop(maxh)
            elif operation[1] == '-1':
                while h and not visited[h[0][1]]:
                    heapq.heappop(h)
                if h:
                    visited[h[0][1]] = False
                    heapq.heappop(h)

    while maxh and not visited[maxh[0][1]]:
        heapq.heappop(maxh)
    while h and not visited[h[0][1]]:
        heapq.heappop(h)

    if h:
        print(f"{-maxh[0][0]} {h[0][0]}")
    else:
        print("EMPTY")
