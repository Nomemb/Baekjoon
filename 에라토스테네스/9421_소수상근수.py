n = int(input())
a = []
ans = []

array = [False,False] + [True]*(n-1)

for i in range(2, int(n**0.5)+1):
    if not array[i]:
        continue
    for j in range(i*i, n+1, i):
        array[j] = False

for i in range(2,n+1):
    if array[i]:
        a.append(i)

def solve(n):
    s = set()
    N = n
    while(True):
        _sum = 0
        for i in str(N):
            _sum += int(i)**2
        if _sum in s:
            return
        if _sum == 1:
            ans.append(n)
            return
        s.add(_sum)
        N = _sum

        

for i in range(0,len(a)):
    solve(a[i])

for i in range(len(ans)):
    print(ans[i])