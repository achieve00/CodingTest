# 한 번호가 다른 번호의 접두어인 경우가 없어야 한다

#  테스트 케이스의 개수 t
t = int(input()) 

for _ in range(t):
  n = int(input())
  numbers = []
  for _ in range(n):
    number = input()
    numbers.append(number)

  flag = False
  for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i == j:
            continue
        if numbers[j].startswith(numbers[i]):
          flag = True
    
  if flag:
    print("NO")
  else:
    print("YES")

# 시간 초과
##############################################################

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = [input().strip() for _ in range(n)]

    numbers.sort()

    flag = False
    for i in range(n - 1):
        if numbers[i + 1].startswith(numbers[i]):
            flag = True
            break

    print("NO" if flag else "YES")
