# 테스트 케이스
T = int(input())

for _ in range(T):
  # 지원자 숫자
  N = int(input())
  candidates = [tuple(map(int, input().split())) for _ in range(N)]
  
  candidates.sort()

  selected = 0
  min_interview = float('inf')  # 가장 높은 순위를 가진 면접 점수

  for paper, interview in candidates:
    if interview < min_interview:
        selected += 1       # 이전보다 면접 순위가 높으면 선발
        min_interview = interview

  print(selected)