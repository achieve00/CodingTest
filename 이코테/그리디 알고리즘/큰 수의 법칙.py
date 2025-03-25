n, m, k = map(int, input().split())
ary = list(map(int, input().split()))

# ary sort
ary.sort()

# 가장 큰 수
first = ary[n-1]
# 그 다음으로 큰 수
second = ary[n-2]

result = 0

while (m > 0):
  for i in range(k):
    result += first
    m -= 1
  result += second
  m -= 1