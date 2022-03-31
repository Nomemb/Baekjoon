N = 1299710
array = [False,False] + [True]*(N-2)

for i in range(2,N):
    for j in range(2*i, N, i):
        array[j] = False

T = int(input())
for t in range(T):
    k = int(input())
    if array[k]:
        print(0)
    else:
        l = k - 1
        r = k + 1
        while(True):
            if array[l]:
                break
            l -= 1
        while(True):
            if array[r]:
                break
            r += 1
        print(r-l)


                

