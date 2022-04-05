s = input()
stack = []

def solve(s):
    if len(s) % 2 == 1:
        print(0)
        return
    else:
        for i in s:
            if i == "(" or i == "[":
                stack.append(i)
            elif i == ")":
                ans = 1
                mul = 2
                while stack:
                    top = stack.pop()
                    if top == "[":
                        print(0)
                        return
                    elif top == "(":
                        stack.append(ans*mul)
                        ans = 1
                        break
                    else:
                        if len(stack) == 0:
                            print(0)
                            return

                        elif type(stack[-1]) is int:
                            stack[-1] += top
                        else:
                            ans = top
            else:
                ans = 1
                mul = 3
                while stack:
                    top = stack.pop()
                    if top == "(":
                        print(0)
                        return
                    elif top == "[":
                        stack.append(ans*mul)
                        ans = 1
                        break
                    else:
                        if len(stack) == 0:
                            print(0)
                            return
                        elif type(stack[-1]) is int:
                            stack[-1] += top
                        else:
                            ans = top
    for i in stack:
        if type(i) == str:
            print(0)
            return
    print(sum(stack))
solve(s)
