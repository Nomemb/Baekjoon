import bisect

n = int(input())
a = list(map(int,input().split()))
s=[]
s.append(a[0])
j=0
for i in range(1,len(a)):
    if s[j]<a[i]:
        s.append(a[i])
        j += 1
    elif a[i] in s: continue
    elif s[0]>a[i]: s[0]=a[i]
    else:
        t=bisect.bisect_right(s,a[i])
        s[t]=a[i]
print(len(s))