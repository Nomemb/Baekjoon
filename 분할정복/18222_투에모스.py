import math

k = int(input())
a = True

def solve(k,a):
    if k == 1:
        return a
    elif k == 2:
        return not a

    else:
        z = int(math.log(k-1,2))
        a = not a
        b = k-2**z
        return solve(b,a)

ans = solve(k,a)
print(0 if ans else 1)