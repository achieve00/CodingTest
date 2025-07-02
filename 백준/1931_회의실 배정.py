# 1931 회의실 배정
# 회의실을 사용할 수 있는 회의의 최대 개수

N = int(input()) # 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력


times = []
for _ in range(N):
  time = list(map(int, input().split()))
  times.append(time)
times.sort(key=lambda x: (x[1], x[0]))

# 1. 끝나는 시간이 가장 빠른 것 sort -> 추출
# 2. 해당 시간 이후로 시작하는 것 중 끝나는 시간이 가장 빠른 것 
cnt = 0
end_time = 0

for start, end in times:
    if start >= end_time:
        cnt += 1
        end_time = end
print(cnt)