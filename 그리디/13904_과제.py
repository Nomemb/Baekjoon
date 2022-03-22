N = int(input())
l = []
do = [0 for _ in range(1001)]
for i in range(N):
    d,w = map(int, input().split())
    l.append([d,w])
l.sort(key = lambda x:-x[1])
for i in range(N):
    deadline = l[i][0]-1
    if(do[deadline] == 0):
        do[deadline] = l[i][1]
    else:
        while(do[deadline] != 0):
            deadline -= 1
            if(deadline < 0):
                break
        if(deadline < 0):
            continue
        do[deadline] = l[i][1]
print(sum(do))

