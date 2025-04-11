# 문제: 대충 만든 자판
# 플랫폼: 프로그래머스
# LV: 1
# 유형: 구현, 문자열, 해시맵
# 난이도: 하
# 풀이 요약:
#   - keymap 리스트에 있는 문자열들에서 각 문자별 최소 입력 타수를 기록함
#   - targets의 각 문자열에 대해, 각 문자를 입력하는 데 걸리는 최소 타수의 합을 구함
#   - 만약 keymap에 없는 문자가 포함되어 있다면 해당 target은 -1로 처리
# 시간복잡도: O(K + T * L)
#   - K: keymap 전체 길이 (모든 문자의 위치 기록)
#   - T: target의 개수
#   - L: 각 target의 평균 길이


def get_min_keymap_positions(keymap):
    key_pos = dict()

    for key in keymap:
        for idx, ch in enumerate(key):
            # 타수는 1-based
            pos = idx + 1
            if ch not in key_pos:
                key_pos[ch] = pos
            else:
                key_pos[ch] = min(key_pos[ch], pos)
    return key_pos

def solution(keymap, targets):
    answer = []
    # keymap
    key = get_min_keymap_positions(keymap)
    
    for target in targets:
        cnt = 0
        for t in target:
            if t not in key:
                cnt = -1
                break
            cnt += key[t]
        answer.append(cnt)
    
    return answer