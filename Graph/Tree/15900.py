# https://www.acmicpc.net/problem/15900

from sys import stdin

n = int(stdin.readline())

tree = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

count = 0

stack = [[1, 0]]

while stack:
    node, depth = stack.pop()
    visited[node] = True

    if node != 1 and len(tree[node]) == 1:
        count += depth
        continue

    for nextNode in tree[node]:
        if not visited[nextNode]:
            stack.append([nextNode, depth + 1])

print("Yes" if count % 2 else "No")
