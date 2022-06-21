from pickle import TRUE
import queue
import sys
from collections import deque

N,M,R = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
head_node = [0 for _ in range(N+1)]

for i in range(M):
    u,v =  map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()


def BFS(start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = 1
    count = 1
    head_node[start_node] = count
    
    
    while queue:
        u = queue.popleft()
        for x in graph[u]:
            if not visited[x]:
                count += 1
                visited[x] = 1
                queue.append(x)
                head_node[x] = count

BFS(R)
for i in head_node[1::]:
    print(i)
