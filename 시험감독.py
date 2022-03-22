# https://www.acmicpc.net/problem/13458

N = int(input())
A = list(map(int, input().split()))
B,C = map(int, input().split())

count = N

for i in range(N):
    r = (A[i]-B)%C
    if A[i]-B>0:
        if r==0:
            count += (A[i]-B)//C
        else:
            count += (A[i]-B)//C+1
        
print(count)