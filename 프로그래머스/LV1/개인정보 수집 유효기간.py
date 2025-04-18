# 문제: 개인정보 수집 유효기간
# 플랫폼: 프로그래머스 (2023 KAKAO 기출)
# 레벨: 1
# 유형: 구현, 날짜 처리, 시뮬레이션
# 풀이 요약:
#   - 모든 날짜는 'YYYY.MM.DD' 형식이며, 달은 28일까지 고정됨
#   - 날짜를 총 일수로 변환하여 today와 만료일을 직접 비교
#   - terms 정보를 딕셔너리로 구성한 뒤, privacies마다 약관에 따라 유효기간을 계산
#   - 유효기간이 지난 항목의 인덱스(i + 1)를 answer에 추가
# 시간복잡도: O(n)


def to_days(year, month, day):
    return year * 12 * 28 + month * 28 + day
    
def solution(today, terms, privacies):
    answer = []
    # 모든 달은 28일까지 있다고 가정
    today_days = to_days(*map(int, today.split('.')))
    
    t = {key: int(val) for key, val in (term.split() for term in terms)}
    
    for i, privacy in enumerate(privacies):
        date, key = privacy.split()
        PY, PM, PD = map(int, date.split('.'))
        
        # 보관 유효기간 더하기
        PM += t[key]
        PY += (PM - 1) // 12
        PM = (PM - 1) % 12 + 1
        
        # 보관 만료일
        expire_days = to_days(PY, PM, PD - 1)
        
        # 만료일이 today보다 이전이면 파기 대상
        if expire_days < today_days:
            answer.append(i + 1)
    
    return answer