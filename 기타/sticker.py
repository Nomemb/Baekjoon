from collections import Counter

sticker1, answer1 = [14, 6, 5, 11, 3, 9, 2, 10], 36
sticker2, answer2 = [1, 3, 2, 5, 4], 8


def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]

    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])

    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])

    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = sticker[1]

    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])

    return max(dp1[n-2], dp2[n-1])


print(solution(sticker1) == answer1)
print(solution(sticker2) == answer2)