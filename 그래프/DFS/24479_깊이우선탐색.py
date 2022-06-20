import sys
from collections import deque

N,M,R = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
head_node = [0 for _ in range(N+1)]

for i in range(M):
    u,v =  map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort(reverse=True)

count = 1

stack = deque()
stack.append(R)

while stack:
    current_node = stack.pop()
    visited[current_node] = True
    if head_node[current_node] == 0:
        head_node[current_node] = count
        count += 1
    
    for next_node in graph[current_node]:
        if not visited[next_node]:
            stack.append(next_node)

for count in head_node[1:]:
    print(count)