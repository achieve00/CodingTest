# 문제: 큰 수의 법칙
# 유형: 그리디
# 난이도: 하
# 풀이 요약: 가장 큰 수를 K번 더하고, 두 번째로 큰 수를 1번 더하는 패턴을 반복
# 시간복잡도: O(m) – while + for 루프 반복

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