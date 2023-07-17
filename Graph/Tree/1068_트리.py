import sys

input = sys.stdin.readline

N = int(input())
graph = list(map(int, input().split()))
del_Node = int(input())
leaf_count = 0
tree = [[] for _ in range(N + 2)]
for i in range(N):
    if graph[i] == -1:
        tree[N + 1].append(i)
    else:
        tree[graph[i]].append(i)


def DFS(node):
    global leaf_count

    if len(tree[node]) == 0:
        leaf_count += 1
        return leaf_count

    for i in range(len(tree[node])):
        if tree[node][i] == del_Node:
            if len(tree[node]) == 1:
                leaf_count += 1
                return leaf_count
        else:
            DFS(tree[node][i])


if graph[del_Node] == -1:
    print(0)
else:
    DFS(N + 1)
    print(leaf_count)
