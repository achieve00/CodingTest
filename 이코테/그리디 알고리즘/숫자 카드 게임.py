# N: 행의 개수
# M: 열의 개수
# 이후: 적힌 숫자

n, m = map(int, input().split())

result = 0

for row in range(n):
  ary = list(map(int, input().split()))
  min_value = min(ary)
  result = max(result, min_value)

print(result)