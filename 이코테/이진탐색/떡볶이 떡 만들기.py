# 문제: 떡볶이 떡 만들기
# 유형: 이진 탐색 (Parametric Search)
# 난이도: 중
# 풀이 요약: 절단기 높이를 이진 탐색으로 조절하면서, 요청한 떡의 길이를 넘길 수 있는 최대 높이 탐색
# 시간복잡도: O(n log h) – n: 떡 개수, h: 가장 긴 떡의 길이


# N: 떡의 개수
# M: 요청한 떡의 길이
# Output: 절단기에 설정할 수 있는 높이의 최대값

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))
start = 0
end = max(array)

result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2
  for x in array:
    val = x - mid
    if val > 0: total += val
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)