N, M = map(int, input().split())

C = [0 for _ in range(9)]
L = [0 for _ in range(9)]


def DFS(k):
    if (k == M):
        for i in range(M):
            print(str(L[i]) + " ", end="")
        print()
        return
    for i in range(1, N + 1):
        if C[i] == 1:
            continue
        C[i] = 1
        L[k] = i
        DFS(k + 1)
        C[i] = 0


DFS(0)
