x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())

def solve(a1, b1, a2, b2):
    return a1*b2 - a2*b1

c = solve(x2-x1, y2-y1, x3-x1, y3-y1)
if c > 0:
    print(1)
elif c < 0:
    print(-1)
else:
    print(0)