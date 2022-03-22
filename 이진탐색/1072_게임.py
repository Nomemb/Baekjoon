X,Y = map(int, input().split())
winrate = Y*100//X
ans = 0
def solve(start, end):
    global ans
    while start <= end:
        mid = (start+end)//2
        _winrate = (Y+mid)*100//(X+mid) - winrate
        if  _winrate < 1:
            start = mid + 1
        else:            
            end = mid - 1
            ans = mid

    return ans

if winrate >= 99:
    print(-1)
else:
    print(solve(0, X))

