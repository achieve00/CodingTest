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