N = int(input())
s = list(map(int, str(N)))

if 0 not in s or sum(s) % 3 != 0:
    print(-1)
else:
    s.sort(reverse=True)
    print(*s,sep='')

