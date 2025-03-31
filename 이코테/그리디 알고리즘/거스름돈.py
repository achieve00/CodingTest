# 문제: 거스름돈
# 유형: 그리디
# 난이도: 하
# 풀이 요약: 큰 단위 동전부터 차례로 거슬러주는 방식 (동전 단위가 서로 배수 관계일 때 최적)
# 시간복잡도: O(1) – 고정된 동전 수에 대해 반복

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