# 문제: [PCCP 기출문제] 1번 / 붕대 감기
# 유형: 시뮬레이션, 구현
# 풀이 요약: 매 초마다 공격 여부 확인 → 없으면 회복 진행. 연속 성공 시 추가 회복. 체력은 최대치 초과 불가.
# 시간복잡도: O(T) – T는 마지막 공격 시간

def solution(bandage, health, attacks):
    combo_cnt = 0 # 연속 성공 cnt
    hp = health # 캐릭터의 현재 체력
    event_map = {start: value for start, value in attacks}

    # 마지막 공격 시간 attacks[-1][0]
    final_attack = attacks[-1][0]

    for time in range(final_attack+1):
        # 몬스터의 공격 확인
        if time in event_map:
            hp -= event_map[time]
            combo_cnt = 0
            # 만약 몬스터의 공격을 받고 캐릭터의 체력이 0 이하가 되어 죽는다면 -1을 return 
            if hp <= 0: return -1
            # 공격 받으면 회복 없음
            continue

        # bandage[1] -> 초당 회복량
        hp = hp + bandage[1]
        combo_cnt += 1
        if combo_cnt % bandage[0] == 0:
            hp = hp + bandage[2] # 연속 성공 시 bandage[2]만큼 추가 회복
            combo_cnt = 0
        # hp는 최대치를 넘길 수 없음
        hp = min(hp, health)

    return hp