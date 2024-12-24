from collections import deque

N, M = map(int, input().split())

computers = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    computers[b].append(a)


def bfs(num):
    q = deque()
    q.append(num)
    cnt = 0
    visited = [False] * (N + 1)
    visited[num] = True
    while q:
        cur = q.popleft()
        for next in computers[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt += 1
    return cnt


result = []
answer = []
for start in range(1, len(computers)):
    result.append(bfs(start))
for i in range(len(result)):
    if max(result) == result[i]:
        answer.append(i+1)

print(*answer)

