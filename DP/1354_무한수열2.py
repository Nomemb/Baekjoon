N,P,Q,X,Y = map(int,input().split())

a = [0 for _ in range(10000000)]
def solve(number):
    if number <= 0:
        return 1
    if number < 10000000:
        if a[number] > 0:
            return a[number]
        a[number] = solve(number//P-X) + solve(number//Q-Y)
        return a[number]
    else:
        return solve(number//P-X) + solve(number//Q-Y)

print(solve(N))