def charge(N):
  # Input: 거슬러 줘야 할 돈(N)
  # Output: 동전의 최소 개수(cnt)

  cnt = 0 # 동전의 개수

  # 500원 개수 +
  cnt += (N//500)

  # 500원을 거슬러주고 남은 돈
  N = N % 500

  # 100원
  cnt += (N//100)
  N = N % 100

  # 50원
  cnt += (N//50)
  N = N % 50

  # 10원
  cnt += (N//10)
  N = N % 10

  return cnt

def charge_new(N):
  # Input: 거슬러 줘야 할 돈(N)
  # Output: 동전의 최소 개수(cnt)
  cnt = 0
  coins = [500, 100, 50, 10]
  for coin in coins:
    cnt += (N // coin)
    N %= coin

  return cnt