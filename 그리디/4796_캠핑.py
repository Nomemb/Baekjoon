case = 0
while(True):
    case += 1
    L,P,V = map(int,input().split())
    if(L==0 and P==0 and V==0):
        break
    ans = 0
    day = 0
    while(day < V):
        ans += L
        day += L
        if(day > V):
            ans -= (day - V)
            break
        day = day + P - L

    print("Case " + str(case) +": " + str(ans))

