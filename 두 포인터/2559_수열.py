# https://www.acmicpc.net/problem/2559

N,K = map(int, input().split())
a = list(map(int, input().split()))
# 최대값은 음수가 나올 수도 있으니 0으로 초기화하지 말자.
m = sum(a[0:K])
s = sum(a[0:K])
for i in range(1,N-K+1):
    s = s - a[i-1] + a[i+K-1]
    if m < s:
        m = s
print(m)