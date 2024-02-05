# https://www.acmicpc.net/problem/10986

import collections

n,m = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0
remains = [0]*n
for i in range(len(remains)):
    if i == 0:
        remains[i] = nums[i] % m
    else:
        remains[i] = (remains[i-1] + nums[i]) % m
        
    if remains[i] == 0:
        cnt += 1

counter = dict(collections.Counter(remains))
for i in counter.values():
    if i < 2:
        continue
    # 같은 나머지끼리 조합을 만들면 해당 구간의 부분합도 무조건 나머지가 0
    cnt += i*(i-1)/2

print(int(cnt))
