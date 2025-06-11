N, L = map(int, input().split())
loc = list(map(int, input().split()))

loc.sort()

answer = 0
i = 0

while i < N:
    # 현재 위치에서 테이프 설치
    start = loc[i]
    end = start + L - 1  # 테이프 커버 범위는 L길이
    answer += 1

    # 커버 가능한 구멍들은 모두 넘긴다
    while i < N and loc[i] <= end:
        i += 1

print(answer)