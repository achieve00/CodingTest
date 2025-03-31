# 문제: 1이 될 때까지
# 유형: 그리디
# 난이도: 하
# 풀이 요약: 나누어떨어질 때까지 1씩 빼고, 나눌 수 있을 땐 나누는 과정을 반복. 
#           반복적으로 1씩 빼는 대신, 한 번에 계산해서 연산 횟수 줄임
# 시간복잡도: O(log N) – 나눗셈 & 감산 반복

# 1. N에서 1을 뺸다
# 2. N을 K로 나눈다

n, k = map(int, input().split())
result = 0

while(True):
  # 만들어야하는 숫자 -> 나누어 떨어지는 수
  num = (n//k) * k
  result += (n - num)
  n = num

  if n < k: break
  result += 1
  n //= k

result += (n - 1)
print(result)