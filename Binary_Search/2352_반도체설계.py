N = int(input())
a = list(map(int, input().split()))

s = []


def binary_search(key, low, high):
    while low < high:
        mid = (low + high) // 2
        if s[mid] < key:
            low = mid + 1
        else:
            high = mid
    return high


s.append(a[0])
for i in range(1, len(a)):
    if a[i] > s[-1]:
        s.append(a[i])
    else:
        s[binary_search(a[i], 0, len(s))] = a[i]

print(len(s))
