# https://www.acmicpc.net/problem/2493

N = input()
l = list(map(int, input().split()))
s = []
n = []
ans = "0"
for i in range(len(l)):
    if not s:
        s.append(l[i])
        n.append(i)
    elif s[-1] <= l[i]:
        while s and s[-1] <= l[i]:
            s.pop()
            n.pop()
        if not s:
            ans += " " + str(0)
        else:
            ans += " " + str(n[-1]+1)
        s.append(l[i])
        n.append(i)
    else:
        ans += " " + str(n[-1]+1)
        s.append(l[i])
        n.append(i)

print(ans)

