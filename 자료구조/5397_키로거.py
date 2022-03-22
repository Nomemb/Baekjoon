from sys import stdin

m = int(input())
for i in range(m):
    key = 0
    s = list(stdin.readline().strip())
    s1 = []
    s2 = []
    while (s[key] =='<' or s[key] =='>' or s[key]=='-'):
        key += 1
    
    for j in range(key, len(s)):
        if s[j] == "<" and s1:
            s2.append(s1.pop())
        elif s[j] == ">" and s2:
            s1.append(s2.pop())
        elif s[j] == "-" and s1:
            s1.pop()
        elif s[j] !='<' and s[j] !='>' and s[j] !='-':
            s1.append(s[j])
    print(''.join(s1+s2[::-1]))

