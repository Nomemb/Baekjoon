N = int(input())
A = list(map(int, input().split()))

S = [1 for _ in range(N)]
S[0] = A[0]
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            S[i] = max(S[i], S[j] + A[i])
        else:
            S[i] = max(S[i], A[i])

print(max(S))
