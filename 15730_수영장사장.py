N = int(input())

count = 0
start = 1
sum = 0
end = start
while True:
    if sum >= N:
        sum -= start
        start += 1
    elif end == N:
        count += 1
        break
    else:
        sum += end
        end += 1
    
    if sum == N:
        count += 1

print(count)