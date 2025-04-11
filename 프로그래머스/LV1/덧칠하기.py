# 문제: 덧칠하기
# 플랫폼: 프로그래머스
# LV: 1
# 유형: 구현, 그리디
# 난이도: 하
# 풀이 요약:
#   - section 리스트에는 칠해야 하는 구역의 시작점들이 오름차순으로 주어짐
#   - 롤러 한 번으로 m미터까지 칠할 수 있으므로, 현재 구역(s)이 이전 롤러 범위(now) 안에 있으면 건너뜀
#   - 아니면 새로운 롤러를 사용해 s부터 s + m까지 칠하고, 롤러 사용 횟수(answer)를 증가시킴
# 시간복잡도: O(n) — section 리스트를 한 번 순회

def solution(n, m, section):
    answer = 0
    now = section[0]
    
    # 롤러의 길이: m미터
    for s in section:
        if s < now:
            continue
        now = s + m
        answer += 1
    
    return answer