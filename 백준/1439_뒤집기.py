# 1439 뒤집기

# 0과 1로만 이루어진 문자열 S
# 다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것

# 연속된 걸 한가지 덩어리라고 생각하고, 덩어리 수가 작은 쪽을 뒤집으면 됨


S = input()

zeros = 0
ones = 0

post = ''

# 연속된 것 확인
for i in S:
  if  i == post:
    continue

  if i == '0':
    zeros += 1
  else:
    ones += 1
  
  post = i


print(min(zeros, ones))