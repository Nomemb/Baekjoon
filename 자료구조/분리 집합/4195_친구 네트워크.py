# https://www.acmicpc.net/problem/4195
import sys
input = sys.stdin.readline

def getParent(parents, k):
    if parents[k] == k:
        return k
    p = getParent(parents, parents[k])
    parents[k] = p
    return p

def unionParent(parents, x, y, count):
    a = getParent(parents, x)
    b = getParent(parents, y)
    if a != b:
        parents[b] = a
        count[a] += count[b]

for _ in range(int(input())):
    parents = {}
    count = {}

    for i in range(int(input())):
        x, y = input().split()
        if x not in parents:
            parents[x] = x
            count[x] = 1
        if y not in parents:
            parents[y] = y
            count[y] = 1
        
        unionParent(parents, x,y,count)
        print(count[getParent(parents,x)])




