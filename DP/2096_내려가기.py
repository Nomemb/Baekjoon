import sys

input = sys.stdin.readline
N = int(input())
maxDp = [0] * 3
minDp = [0] * 3

maxTmp = [0] * 3
minTmp = [0] * 3
for i in range(N):
    x, y, z = map(int, input().rstrip().split())

    maxDp = max(maxDp[0], maxDp[1]) + x, max(maxDp[0], maxDp[1], maxDp[2]) + y, max(maxDp[1], maxDp[2]) + z
    minDp = min(minDp[0], minDp[1]) + x, min(minDp[0], minDp[1], minDp[2]) + y, min(minDp[1], minDp[2]) + z

print(max(maxDp), min(minDp))
