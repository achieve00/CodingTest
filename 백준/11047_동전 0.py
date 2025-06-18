# 	11047 동전 0
# 동전 개수의 최솟값
N, K = map(int, input().split())  # N: 동전 종류, K: 그 가치의 합

values = [int(input()) for _ in range(N)]
values.sort(reverse=True)  # 큰 동전부터

cnt = 0
for coin in values:
    if K >= coin:
        cnt += K // coin
        K = K % coin

print(cnt)