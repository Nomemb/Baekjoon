m = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    for j in range(10):
        for w in range(10):
            m[a+j][b+w] = 1

s = 0
for i in range(100):
    s += sum(m[i])

print(s)