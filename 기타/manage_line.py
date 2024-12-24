P = int(input())

for i in range(P):
    students = list(map(int, input().split()))
    T, students = students[0], students[1:]

    line = []
    total = 0
    for i in range(len(students)):
        if len(line) == 0:
            line.append(students[i])

        else:
            is_most_taller = True
            for j in range(len(line)):
                if students[i] < line[j]:
                    total += len(line[j:])
                    line.insert(j, students[i])
                    is_most_taller = False
                    break

            if is_most_taller:
                line.append(students[i])

    print(T, total)


