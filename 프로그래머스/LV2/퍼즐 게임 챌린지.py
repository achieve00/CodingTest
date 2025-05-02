def can_clear(level, diffs, times, limit):
    total_time = 0
    for i in range(len(diffs)):
        if level >= diffs[i]:
            total_time += times[i]
        else:
            cnt = diffs[i] - level
            time_prev = times[i - 1] if i > 0 else 0
            total_time += cnt * (times[i] + time_prev) + times[i]
        if total_time > limit:
            return False
    return True

def binary_search(diffs, times, limit, start, end):
    answer = end
    while start <= end:
        mid = (start + end) // 2
        if can_clear(mid, diffs, times, limit):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer


def solution(diffs, times, limit):
    max_diff = max(diffs)
    return binary_search(diffs, times, limit, 1, max_diff + limit)