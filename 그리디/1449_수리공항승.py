N,L = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
count = locate = 0
i = 0
while(i < N):
    if(locate < l[i]):
        locate = l[i] + L-1
        count += 1
    i += 1
print(count)
