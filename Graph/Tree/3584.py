# https://www.acmicpc.net/problem/3584
# 가장 가까운 공통 조상

T = int(input())
for i in range(T):
    N = int(input())
    p = [0 for i in range(N+1)]
    for j in range(N-1):
        A, B = map(int, input().split())
        p[B] = A
    
    a, b = map(int,input().split())
    parent_a = [0,a]
    parent_b = [0,b]
    while p[a]:
        parent_a.append(p[a])
        a = p[a]
    while p[b]:
        parent_b.append(p[b])
        b = p[b]
    
    x = 1
    while parent_a[-x]==parent_b[-x]:
        x+=1
    
    print(parent_a[-x+1])



