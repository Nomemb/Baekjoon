N = int(input())
arr = [0 for i in range(1001)]
arr[1] = 1
arr[2] = 2
arr[3] = 1
for i in range(4,N+1):
    if arr[i-1] == 1 or arr[i-3] == 1:
        arr[i] = 2
    else:
        arr[i] = 1
    
 
print("SK" if arr[N] == 1 else "CY")