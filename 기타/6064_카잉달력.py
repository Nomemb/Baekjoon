from math import gcd


def LCM(x, y):
    return x * y // gcd(x, y)


def solve(M, N, x, y):
    r = LCM(M, N)
    y %= N
    for i in range(r // M + 1):
        ans = (i * M + x)
        if ans % N == y:
            return ans
    return -1


T = int(input())

for i in range(T):
    M, N, x, y = map(int, input().split())
    print(solve(M, N, x, y))
