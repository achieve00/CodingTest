# 1744 수 묶기

N = int(input()) # N 길이의 수열

# 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능

nums = []
nums = [int(input()) for _ in range(N)]

# 양수와 음수를 나눠서 저장
positive = []
negative = []
ones = 0
zero = 0

for num in nums:
    if num > 1:
        positive.append(num)
    elif num == 1:
        ones += 1  # 1은 무조건 더하는 게 이득
    elif num == 0:
        zero += 1
    else:
        negative.append(num)

# 큰 양수부터 곱
positive.sort(reverse=True)
# 작은 음수부터 곱
negative.sort()

result = 0

# 양수 짝지어 곱
i = 0
while i < len(positive) - 1:
    result += positive[i] * positive[i+1]
    i += 2
if i == len(positive) - 1:
    result += positive[i]  # 남은 수는 그냥 더함

# 음수 짝지어 곱
i = 0
while i < len(negative) - 1:
    result += negative[i] * negative[i+1]
    i += 2
if i == len(negative) - 1:
    # 남은 음수는 0 있으면 무시, 없으면 더함
    if zero == 0:
        result += negative[i]

# 1은 무조건 더하기
result += ones

print(result)