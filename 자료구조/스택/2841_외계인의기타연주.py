import sys
input = sys.stdin.readline

N,P = map(int,input().split())
stack = [[] for i in range(7)]
count = 0
for i in range(N):
    a,b = map(int,input().rstrip().split())
    if not stack[a]:
        stack[a].append(b)
        count += 1
    else:
        while stack[a] and stack[a][-1] > b:
            del stack[a][-1]
            count += 1
        if not stack[a] or stack[a][-1] != b:
            stack[a].append(b)
            count += 1

print(count)



