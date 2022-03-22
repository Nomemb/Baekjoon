"""
1 2 3 4 5 6 7 8 9 10
1 2 3 1 2 3 4 2 1 2
"""

N = int(input())
lst = [i for i in range(N+1)]
ans = [0 for _ in range(N+1)]

for i in range(1,N+1):
    k = int(i**0.5)
    K = k//2
    if k**2==i:
        ans[i]=1
    else:
        ans[i] = lst[i]
        while k>K:
            if ans[i] > ans[i-k*k]+1:
                ans[i] = ans[i-k*k]+1
            k -= 1

print(ans[N])
