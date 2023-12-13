n = int(input())
count = 0
s = set()
s.add("ChongChong")
for i in range(n):
    p1, p2 = map(str, input().split())
    if p1 in s or p2 in s:
        s.add(p1)
        s.add(p2)
    
print(len(s))
