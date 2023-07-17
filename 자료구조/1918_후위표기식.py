# https://www.acmicpc.net/problem/1918
a = list(input())
operator = []
ans = ""
for i in range(len(a)):
    if a[i] == '(':
        operator.append("(")
    elif a[i] == '*' or a[i] == '/':
        while operator and (operator[-1] == '*' or operator[-1] == '/'):
            ans += operator.pop()
        operator.append(a[i])
    elif a[i] == '+' or a[i] == '-':
        while operator and operator[-1] != '(':
            ans += operator.pop()
        operator.append(a[i])
    elif a[i] == ')':
        while operator and operator[-1] != '(':
            ans += operator.pop()
        operator.pop()
    else:
        ans += a[i]

while operator:
    ans += operator.pop()
print(ans)
