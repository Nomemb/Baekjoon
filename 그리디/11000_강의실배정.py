import sys, heapq

N = int(input())
T = []
l = []
for i in range(N):
    s,t = map(int, sys.stdin.readline().split())
    l.append([s,t])

l.sort()
heapq.heappush(T, l[0][1])
for i in range(1,N):
    if(l[i][0] < T[0]):
        heapq.heappush(T,l[i][1])
    else:
        heapq.heappop(T)
        heapq.heappush(T,l[i][1])

print(len(T))


