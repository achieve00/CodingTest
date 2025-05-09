def hourToMin(time):
    H, M = time.split(':')
    H, M = int(H), int(M)
    times = H * 60 + M
    return times
    
def solution(plans):
    answer = []
    hold_plan = []  # [과목, 남은 시간]

    # 시간을 분 단위로 변환
    for i in range(len(plans)):
        subject, time, duration = plans[i]
        plans[i] = [subject, hourToMin(time), int(duration)]

    # 시작 시간을 기준으로 정렬
    plans.sort(key=lambda x: x[1])

    now = plans[0][1]

    for i in range(len(plans) - 1):
        current = plans[i]
        next_start = plans[i + 1][1]
        remain = next_start - current[1]

        if remain < current[2]:
            # 다 못하면 멈춤
            hold_plan.append([current[0], current[2] - remain])
        else:
            # 과제 완료
            answer.append(current[0])
            now = current[1] + current[2]
            remain_time = remain - current[2]

            # 멈춰둔 과제 이어하기 (LIFO)
            while remain_time > 0 and hold_plan:
                paused = hold_plan.pop()
                if remain_time >= paused[1]:
                    remain_time -= paused[1]
                    answer.append(paused[0])
                else:
                    hold_plan.append([paused[0], paused[1] - remain_time])
                    break

    # 마지막 과제 처리
    answer.append(plans[-1][0])

    # 멈춰둔 과제들 처리
    while hold_plan:
        paused = hold_plan.pop()
        answer.append(paused[0])

    return answer