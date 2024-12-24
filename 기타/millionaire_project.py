T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst_prices = list(map(int, input().split()))

    max_price = max(lst_prices)
    max_value = 0

    for idx in range(len(lst_prices)):
        if lst_prices[idx] == max_price:
            if idx + 1 != len(lst_prices):
                max_price = max(lst_prices[idx+1:])

        else:
            max_value += max_price - lst_prices[idx]

    print(f"#{test_case} {max_value}")