T = int(input())

for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = 0
    earn = 0

    # 뒤에서부터 탐색
    for i in range(N - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]  # 이 날 이후 가장 비싼 날로 갱신
        else:
            earn += (max_price - prices[i])  # 지금 사서 나중에 max_price에 판다고 가정

    print(earn)