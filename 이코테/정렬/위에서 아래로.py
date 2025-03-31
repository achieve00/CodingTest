# 문제: 위에서 아래로
# 유형: 정렬
# 난이도: 하
# 풀이 요약: 입력받은 수열을 내림차순 정렬하여 출력
# 시간복잡도: O(n log n) – sorted 함수 사용
# 내림차순 정렬
n = int(input())

array = []

for i in range(n):
  array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
  print(i, sep=' ')