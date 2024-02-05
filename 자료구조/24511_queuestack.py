# https://www.acmicpc.net/problem/24511

import collections

n = int(input())
queue_stack = list(map(int, input().split()))
queue_counter = collections.Counter(queue_stack)[0]

cur_list = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

ans = []
q = collections.deque()
for i in range(len(queue_stack)):
    if queue_stack[i] == 0:
        q.append(cur_list[i])

for i in c:
    q.appendleft(i)
    ans.append(q.pop())

print(*ans)
