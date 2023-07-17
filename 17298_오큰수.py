n = int(input())
arr = list(map(int, input().split()))
ans = [0 for _ in range(n)]
stack = []
for i in range(n - 1, -1, -1):
    while (len(stack) != 0 and stack[-1] <= arr[i]):
        stack.pop()
    if len(stack) == 0:
        ans[i] = -1
    else:
        ans[i] = stack[-1]
    stack.append(arr[i])
print(*ans)
