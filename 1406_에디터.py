# 시간 초과 남
# n = list(input())
# cursor = len(n)
# M = int(input())
# for i in range(M):
#     order = input().split()
#     if order[0] == 'L':
#         if cursor != 0:
#             cursor -= 1
#     elif order[0] == 'D':
#         if cursor != len(n):
#             cursor += 1
#     elif order[0] == 'B':
#         if cursor != 0:
#             del(n[cursor-1])
#             cursor -= 1
#     elif order[0] == 'P':
#         if cursor == len(n):
#             n.append(order[1])
#         else:
#             n.insert(cursor, order[1])
#         cursor += 1

# print(''.join(n))

from sys import stdin

stack1 = list(stdin.readline().strip())
stack2 = []
m = int(input())
for i in range(m):
    order = stdin.readline().strip()
    if order[0] == 'L' and stack1:
        stack2.append(stack1.pop())
    elif order[0] == 'D' and stack2:
        stack1.append(stack2.pop())
    elif order[0] == 'B' and stack1:
        stack1.pop()
    elif order[0] == 'P':
        stack1.append(order[2])

print(''.join(stack1 + list(reversed(stack2))))
