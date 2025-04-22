# 문제: 유연근무제
# 플랫폼: 프로그래머스
# 레벨: 1
# 유형: 구현, 시뮬레이션, 시간 처리
# 풀이 요약:
#   - 각 직원마다 기준 출근 시간(schedules)에 +10분까지 지각 허용
#   - 출근 기록(timelogs) 중 주말(토/일)은 제외하고 평일만 확인
#   - 기준 시간 이전(또는 같게) 출근한 날을 기록
#   - 주 5일 이상 정시 출근한 직원 수를 반환
# 시간복잡도: O(n × d)


def solution(schedules, timelogs, startday):
    answer = 0
    
    # 시작한 요일 startday
    # 1은 월요일, 2는 화요일, 3은 수요일, 4는 목요일, 5는 금요일, 6은 토요일, 7은 일요일
    # 토요일, 일요일은 포함 X
    
    for i in range(len(schedules)):
        schedules[i] = schedules[i] + 10
        tmp = schedules[i] % 100
        if tmp >= 60:
            schedules[i] += 100
            schedules[i] -= 60
    
    people = len(schedules) # 사람들 수
    
    flag = [0] * people 
    
    for i in range(len(timelogs[0])):
        if (i + startday - 1) % 7 + 1 in (6, 7):
            continue
        for j in range(people):
            if timelogs[j][i] <= schedules[j]:
                flag[j] += 1
    
    answer = sum(1 for f in flag if f >= 5)
    
    return answer


    ################################

    def solution(schedules, timelogs, startday):
    # 1. 10분 지각 허용 시간 적용
    for i in range(len(schedules)):
        h, m = divmod(schedules[i], 100)
        m += 10
        if m >= 60:
            h += 1
            m -= 60
        schedules[i] = h * 100 + m

    people = len(schedules)
    days = len(timelogs[0])
    flag = [0] * people

    # 2. 평일만 순회하면서 출근 체크
    for i in range(days):
        weekday = (startday + i - 1) % 7 + 1
        if weekday in (6, 7):  # 토/일 제외
            continue
        for j in range(people):
            if timelogs[j][i] <= schedules[j]:
                flag[j] += 1

    # 3. 주 5일 이상 출근한 사람 수
    return sum(f >= 5 for f in flag)
