# 문제: 데이터 분석
# 플랫폼: 프로그래머스
# 레벨: 1
# 유형: 구현, 리스트 필터링, 정렬
# 풀이 요약:
#   - 주어진 데이터(data)에서 특정 열(ext)의 값이 기준값(val_ext)보다 작은 행만 필터링
#   - 열 이름을 열 인덱스로 매핑하여 코드의 일반성을 유지
#   - 필터링된 행들을 정렬 기준 열(sort_by)의 값을 기준으로 오름차순 정렬
#   - 정렬된 결과를 반환
# 시간복잡도: O(n log n)

def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    column_idx = {name: idx for idx, name in enumerate(["code", "date", "maximum", "remain"])}
    filtered = list(filter(lambda x: x[column_idx[ext]] < val_ext, data))
    
    return sorted(filtered, key=lambda x: x[column_idx[sort_by]])