import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
tc = int(input())

for i in range(tc):
    # n : 지점 수, m : 도로 수, w : 웜홀 수
    n, m, w = map(int, input().split())
    edges = []

    visited = [False] * (n+1)
    for j in range(m):
        # s: 시작 , e: 도착, t: 줄어든 시간
        s, e, t = map(int, input().split())
        edges.append((s, e, t))

    for j in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    print(f"graph: {edges}")
    print(f"visited: {visited}")

    dq = deque()

    dq.append([1,0])
    visited[1] = True

    while dq:
        cur = dq.popleft()
