import sys

input=sys.stdin.readline

arr = []
N = int(input())

visited = [0 for _ in range(N+1)]

for _ in range(N):
    arr.append([*map(int, input().split())])

minDiff = 1e8

def backTracking(depth, idx):
    global minDiff
    if depth == N//2:
        aTeamScore = 0
        bTeamScore = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    aTeamScore += arr[i][j]
                elif not visited[i] and not visited[j]:
                    bTeamScore += arr[i][j]
        
        minDiff = min(minDiff, abs(aTeamScore - bTeamScore))
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            backTracking(depth+1, i+1)
            visited[i] = False
        
        

backTracking(0,0)
print(minDiff)