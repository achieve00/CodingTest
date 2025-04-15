# 문제: 선물 주고받기
# 플랫폼: 프로그래머스 (2023 KAKAO 기출)
# 레벨: 1
# 유형: 구현, 2차원 리스트, 시뮬레이션
# 풀이 요약:
#   - friends 간 선물을 주고받은 횟수를 2차원 배열로 저장
#   - 각 친구의 '선물 지수'를 계산 (준 선물 수 - 받은 선물 수)
#   - 모든 친구 쌍(i, j)에 대해 다음 달 누가 선물을 받을지 비교
#     - 선물을 더 많이 준 사람이 받음
#     - 같으면 선물 지수가 높은 사람이 받음
#     - 둘 다 같으면 아무도 받지 않음
#   - 최종적으로 다음 달 선물을 가장 많이 받을 친구의 수를 반환
# 시간복잡도: O(n² + g)


def solution(friends, gifts):
    answer = 0
    scores = [[0] * len(friends) for _ in range(len(friends))]
    friends_dict = {name: idx for idx, name in enumerate(friends)}

    for gift in gifts:
        A, B = gift.split()
        scores[friends_dict[A]][friends_dict[B]] += 1
        
    row_sums = [sum(row) for row in scores] # 준 선물 수
    col_sums = [sum(col) for col in zip(*scores)] # 받은 선물 수
    diff = [r - c for r, c in zip(row_sums, col_sums)] # 선물 지수

    next_mon = [0] * len(friends)
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if i == j:
                continue
            if scores[i][j] > scores[j][i]:
                next_mon[i] += 1
            elif scores[i][j] < scores[j][i]:
                next_mon[j] += 1
            else:
                if diff[i] > diff[j]:
                    next_mon[i] += 1
                elif diff[i] < diff[j]:
                    next_mon[j] += 1
            
    answer = max(next_mon)
    return answer


###############################################################

def solution(friends, gifts):
    n = len(friends)
    scores = [[0] * n for _ in range(n)]
    name_to_idx = {name: idx for idx, name in enumerate(friends)}

    # 선물 주고받은 횟수 기록
    for gift in gifts:
        giver, receiver = gift.split()
        scores[name_to_idx[giver]][name_to_idx[receiver]] += 1

    # 선물 지수 계산 (준 선물 수 - 받은 선물 수)
    sent = [sum(row) for row in scores]
    received = [sum(col) for col in zip(*scores)]
    gift_score = [s - r for s, r in zip(sent, received)]

    # 다음 달 받을 선물 수 계산
    next_month = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if scores[i][j] > scores[j][i]:
                next_month[i] += 1
            elif scores[i][j] < scores[j][i]:
                next_month[j] += 1
            else:
                if gift_score[i] > gift_score[j]:
                    next_month[i] += 1
                elif gift_score[i] < gift_score[j]:
                    next_month[j] += 1
                # 같으면 아무도 못 받음

    return max(next_month)
