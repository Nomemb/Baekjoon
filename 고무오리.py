str1 = input()
problem = 0
while(1):
    command = input()
    if command == "고무오리 디버깅 끝":
        break
    elif command == "문제":
        problem += 1
    elif command == "고무오리":
        if problem > 0:
            problem -= 1
        else:
            problem += 2

print("힝구" if (problem > 0)  else "고무오리야 사랑해")
