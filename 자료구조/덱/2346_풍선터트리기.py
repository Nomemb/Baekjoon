from collections import deque

n = int(input())
l = list(map(int, input().split()))
t = [True for i in range(n)]
dq = deque(l)
ans = []
idx = 0

ans.append(idx + 1)
t[idx] = False
for i in range(n - 1):
    length = len(dq)
    x = dq.popleft()
    if x < 0:
        X = -x
        for j in range(X - 1):
            dq.appendleft(dq.pop())
        while (X > 0):
            idx = (idx - 1) % n
            if (t[idx] == False):
                continue
            else:
                X -= 1
    else:
        for j in range(x - 1):
            dq.append(dq.popleft())
        while (x > 0):
            idx = (idx + 1) % n
            if (t[idx] == False):
                continue
            else:
                x -= 1
    ans.append(idx + 1)
    t[idx] = False
print(*ans)
