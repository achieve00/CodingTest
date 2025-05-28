colors = {}
numbers = []

for _ in range(5):
    color, number = input().split()
    number = int(number)

    if color not in colors:
        colors[color] = []
    colors[color].append(number)

    numbers.append(number)

numbers.sort()

# 숫자별 등장 횟수 세기
from collections import Counter

num_counts = Counter(numbers)
counts = sorted(num_counts.items(), key=lambda x: (-x[1], -x[0]))  # 등장 수 내림차순, 숫자 큰 순 우선

# 올플러시 + 스트레이트
if len(set(colors)) == 1:
    if len(set(numbers)) == 5 and max(numbers) - min(numbers) == 4:
        score = 900 + max(numbers)
    else:
        score = 600 + max(numbers)

# 스트레이트만
elif len(set(numbers)) == 5 and max(numbers) - min(numbers) == 4:
    score = 500 + max(numbers)

# 4장 같은 숫자
elif counts[0][1] == 4:
    score = 800 + counts[0][0]

# 3장 + 2장 (풀하우스)
elif counts[0][1] == 3 and counts[1][1] == 2:
    score = 700 + counts[0][0] * 10 + counts[1][0]

# 3장만
elif counts[0][1] == 3:
    score = 400 + counts[0][0]

# 2장 + 2장 (투페어)
elif counts[0][1] == 2 and counts[1][1] == 2:
    score = 300 + max(counts[0][0], counts[1][0]) * 10 + min(counts[0][0], counts[1][0])

# 2장만
elif counts[0][1] == 2:
    score = 200 + counts[0][0]

# 그 외
else:
    score = 100 + max(numbers)

print(score)