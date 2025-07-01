# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램
exp = input()
# 식을 split
groups = exp.split('-')

sums = []
for group in groups:
    nums = map(int, group.split('+'))
    sums.append(sum(nums))

# 첫 번째 그룹은 그대로, 나머지는 전부 빼줌
result = sums[0]
for s in sums[1:]:
    result -= s

print(result)