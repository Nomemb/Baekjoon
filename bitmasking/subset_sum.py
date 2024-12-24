N = int(input())

for test_case in range(1, N+1):
    lst_nums = list(map(int, input().split()))[1:]

    n = len(lst_nums)
    for i in range(1, 1 << n):
        subset_sum = 0

        for j in range(n):
            if i & (1 << j):
                subset_sum += lst_nums[j]

        if subset_sum == 0:
            print(f"#{test_case} True")
            break
