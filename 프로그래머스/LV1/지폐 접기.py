# 문제: 지폐 접기기
# 플랫폼: 프로그래머스
# 레벨: LV.1
# 유형: 구현, 시뮬레이션
# 풀이 요약:
#   - 지갑(wallet)의 가로/세로 중 큰 쪽과 지폐(bill)의 큰 쪽을 비교
#   - 지폐가 지갑보다 커서 들어가지 않으면 더 긴 변을 반으로 접음
#   - 접는 횟수를 answer에 저장
#   - 지폐가 들어갈 수 있을 때까지 접는 과정을 반복
# 시간복잡도: O(log(max(bill))) 

def solution(wallet, bill):
    # 1. 지폐를 접은 횟수를 저장할 정수 변수 answer를 만들고 0을 저장합니다.
    answer = 0
    
    while True:
        if wallet[0] >= bill[0] and wallet[1] >= bill[1]:
            return answer
        if wallet[0] >=bill[1] and wallet[1] >= bill[0]:
            return answer
        # 2. 반복문을 이용해 bill의 작은 값이 wallet의 작은 값 보다 크거나 bill의 큰 값이 wallet의 큰 값 보다 큰 동안 아래 과정을 반복합니다.
        # 2-1. bill[0]이 bill[1]보다 크다면, bill[0]을 2로 나누고 나머지는 버립니다.
        if bill[0] > bill[1]: 
            bill[0] = bill[0] // 2
        else:
            # 그렇지 않다면, bill[1]을 2로 나누고 나머지는 버립니다.
            bill[1] = bill[1] // 2
        answer += 1
    