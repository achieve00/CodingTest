# 문제: 추억 점수
# 플랫폼: 프로그래머스
# 레벨: LV.1
# 유형: 구현, 딕셔너리 활용
# 풀이 요약:
#   - name과 yearning을 zip으로 묶어 딕셔너리(yearning_dict)를 생성
#   - 각 photo 리스트에 대해 인물 이름이 yearning_dict에 존재하면 점수를 더함
#   - 각 photo 별 총 점수를 answer 리스트에 저장
# 시간복잡도: O(n × m)

def solution(name, yearning, photo):
    answer = []
    yearninig_dict = dict(zip(name,yearning))
    score = 0
        
    for pic in photo:
        for p in pic:
            if p in yearninig_dict:
                score += yearninig_dict[p]
        answer.append(score)
        score = 0
    
    return answer