# 문제: 숫자 카드 게임
# 유형: 그리디
# 난이도: 하
# 풀이 요약: 각 행에서 가장 작은 수를 고르고, 그 중에서 가장 큰 수를 선택
# 시간복잡도: O(n * m) – 모든 행을 한 번씩 순회

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