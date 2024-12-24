a, b = input().split()

len_diff = len(b) - len(a)
len_a = len(a)
min_cnt = 50
for i in range(len_diff+1):
    temp = b[i:i+len_a]
    cnt = 0
    for pair in zip(temp, a):
        if pair[0] != pair[1]:
            cnt += 1

    if min_cnt > cnt:
        min_cnt = cnt

print(min_cnt)
