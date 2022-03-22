n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

def division(startX,startY,endX,endY):
    jewelry = 0
    impurities = 0
    for i in range(startY, endY+1):
        for j in range(startX, endX+1):
            if arr[i][j] == 2:
                jewelry += 1
            elif arr[i][j] == -1:
                impurities += 1
    
    if jewelry == 0:
        return
    elif jewelry == 1 and impurities == 0:
        return 1
