M = int(input())
key = 1
for i in range(M):
    X, Y = map(int,input().split())
    if X == key:
        key = Y
    elif Y == key:
        key = X

print(key)