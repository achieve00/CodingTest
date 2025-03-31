# 문제: 성적이 낮은 순서로 학생 출력하기
# 유형: 정렬
# 난이도: 하
# 풀이 요약: (이름, 점수) 형태로 입력받은 뒤, 점수를 기준으로 오름차순 정렬하여 이름만 출력
# 시간복잡도: O(n log n) – sorted 함수 사용

n = int(input())
array = []

for i in range(n):
  input_data = input().split()
  name = input_data[0]
  grade = int(input_data[1])
  
  array.append((name, grade))

array = sorted(array, key=lambda x: x[1])

for i in array:
  print(i[0], end=' ')