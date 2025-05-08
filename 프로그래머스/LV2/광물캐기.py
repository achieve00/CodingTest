from collections import deque

def check_fatigue(chunk, pick_type):
    table = [
        [1, 1, 1],   # 다이아 곡괭이
        [5, 1, 1],   # 철 곡괭이
        [25, 5, 1]   # 돌 곡괭이
    ]
    return sum(table[pick_type][mineral] for mineral in chunk)

def solution(picks, minerals):
    fatigue = 0
    mapping = {"diamond": 0, "iron": 1, "stone": 2}
    minerals = [mapping[m] for m in minerals]

    # 곡괭이 수로 캘 수 있는 chunk 수 제한
    total_picks = sum(picks)
    chunked = [minerals[i:i+5] for i in range(0, min(len(minerals), total_picks*5), 5)]

    # 각 chunk에 대해 돌 곡괭이로 캤을 때 피로도 기준으로 정렬 (가장 비싼 chunk 먼저)
    chunked.sort(key=lambda c: -check_fatigue(c, 2))

    pick_queue = []

    for i, cnt in enumerate(picks):  # 다이아→철→돌 순으로
        pick_queue.extend([i] * cnt)

    for chunk, pick_type in zip(chunked, pick_queue):
        fatigue += check_fatigue(chunk, pick_type)
    
    return fatigue