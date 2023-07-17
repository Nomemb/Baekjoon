triangle = list(map(int, input().split()))
triangle.sort()
answer = sum(triangle[0:2]) * 2 - 1 if sum(triangle[0:2]) - 1 < triangle[2] else sum(triangle[0:3])
print(answer)
