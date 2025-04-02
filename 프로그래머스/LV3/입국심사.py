# 문제: [프로그래머스] 입국심사
# 유형: 이진 탐색
# 난이도: 중~상
# 풀이 요약: 주어진 시간 내에 n명을 심사할 수 있는 최소 시간 탐색
# 시간복잡도: O(log(max_time) * len(times)) 

def binary_search(times, target, start, end):
    if start > end:
        return start

    mid = (start + end) // 2
    cnt = 0 

    for time in times:
        cnt += mid // time

    if cnt >= target:
        return binary_search(times, target, start, mid - 1)
    else:
        return binary_search(times, target, mid + 1, end)

def solution(n, times):
    start = 1
    end = max(times) * n  # 최악의 경우

    return binary_search(times, n, start, end)
