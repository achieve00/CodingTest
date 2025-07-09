# 15903 카드 합체 놀이
# 출력: 첫 번째 줄에 만들 수 있는 가장 작은 점수

# 1. x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
# 2. 계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.

n, m = map(int, input().split()) 
# n: 카드의 개수, m: 합체 횟수

a = list(map(int, input().split()))
# 맨 처음 카드의 상태를 나타내는 n개의 자연수

a.sort()

for _ in range(m):
  a[0] = a[0]+a[1]
  a[1] = a[0]
  a.sort()
  
print(sum(a))