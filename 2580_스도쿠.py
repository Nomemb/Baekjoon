array = []
for i in range(9):
    array.append(list(map(int, input().split())))

zeros = [(i,j) for i in range(9) for j in range(9) if array[i][j] == 0]

def solve(i,j):
    numbers = [1,2,3,4,5,6,7,8,9]

    for k in range(9):
        if array[i][k] in numbers:
            numbers.remove(array[i][k])
        if array[k][j] in numbers:
            numbers.remove(array[k][j])
    
    i = i//3
    j = j//3
 
    for y in range(i*3, (i+1)*3):
        for x in range(j*3, (j+1)*3):
            if array[y][x] in numbers:
                numbers.remove(array[y][x])
    
    return numbers

def dfs(count):
    if count == len(zeros):
        for row in array:
            print(*row)
        return
    (i,j) = zeros[count]
    sol = solve(i,j)
    for num in sol:
        array[i][j] = num
        dfs(count + 1)
        array[i][j] = 0


dfs(0)