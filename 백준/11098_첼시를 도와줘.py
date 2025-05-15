n = int(input())

# n개의 테스트 개수
for i in range(n):
  p = int(input())
  val = 0
  name = ''
  players = []
  # p개의 줄
  for j in range(p):
    sal, player = input().split()
    sal= int(sal)

    if sal > val:
      val = sal
      name = player
  
  print(name)