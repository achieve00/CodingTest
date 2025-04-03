# 문제: 연속된 부분 수열의 합
# 유형: 투 포인터, 슬라이딩 윈도우 알고리즘
# 난이도: 중
# 풀이 요약:
#   - 연속된 부분 수열 중 합이 k가 되는 가장 짧은 구간의 시작과 끝 인덱스를 구하는 문제.
#   - 수열이 모두 양의 정수로 이루어져 있으므로 투 포인터(슬라이딩 윈도우) 알고리즘이 가능.
#   - 포인터를 이동시키며 현재 구간의 합이 k보다 작으면 우측 포인터(end)를 확장,
#     크면 좌측 포인터(start)를 이동시켜 줄이면서, 합이 정확히 k인 경우 정답 후보로 저장.
#   - 가장 짧은 구간을 찾는 것이므로 길이를 비교하여 갱신.
# 시간복잡도: O(n) — start와 end 포인터가 각각 최대 n번만 이동하므로 선형 시간에 해결 가능

# 첫번째 풀이는 시간 초과 발생
import numpy as np

def solution(sequence, k):
    for i in range(1, len(sequence)+1):
        # i는 index 얼마만큼 더할 것인가
        # 즉, i == 1; [0:1], [1:2], [2:3] 으로 되도록
        # i == 2: [0:2], [1:3]
        for j in range(len(sequence)):
            # j는 시작 인덱스
            for j in range(len(sequence) - i + 1):
                result = np.sum(sequence[j:j+i])
                if result == k:
                    return [j, j+i-1]

####################################################################

def solution(sequence, k):
    start, end = 0, 0
    result = 0
    min_len = float('inf')
    answer = []

    while end <= len(sequence):
        if result < k:
            if end < len(sequence):
                result += sequence[end]
            end += 1
        elif result > k:
            result -= sequence[start]
            start += 1
        else:
            if end - start < min_len:  # 가장 짧은 구간일 때만 저장
                min_len = end - start
                answer = [start, end - 1]
            # 합이 k일 때도 start 늘려가면서 계속 찾기
            result -= sequence[start]
            start += 1

    return answer