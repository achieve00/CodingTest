#  N개의 꽃들 중에서 다음의 두 조건을 만족하는 꽃들을 선택
# 1. 공주가 가장 좋아하는 계절인 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 한다.
# 2. 정원이 넓지 않으므로 정원에 심는 꽃들의 수를 가능한 적게 한다. 
# 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 꽃들을 선택할 때, 선택한 꽃들의 최소 개수를 출력
def date_to_int(date):
    return date[0] * 100 + date[1]

N = int(input())
schedule = []

for _ in range(N):
  b1, b2, f1, f2 = map(int, input().split())
  schedule.append(([b1, b2], [f1, f2]))

# 개화일은 오름차순
# 낙화일은 내림차순
schedule.sort(key=lambda x: (x[0][0], x[0][1], -x[1][0], -x[1][1]))


current = 301
end = 1201  # 12월 1일
idx = 0
count = 0
max_fade = 0

while current < end:
    found = False
    while idx < N and date_to_int(schedule[idx][0]) <= current:
        fade_date = date_to_int(schedule[idx][1])
        if fade_date > max_fade:
            max_fade = fade_date
            found = True
        idx += 1

    if not found:
        break  # 더 이상 이어지는 꽃이 없음

    current = max_fade
    count += 1

print(count if current >= end else 0)