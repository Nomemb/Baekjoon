line = list(input())
count = 0
stack = []
for i in range(len(line)):
    if line[i] == "(":
        stack.append(i)
    else:
        if line[i-1]=="(":
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)