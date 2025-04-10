# 문제: 테이블 해시 함수
# 플랫폼: 프로그래머스
# LV: 2
# 유형: 구현, 정렬, 나머지 연산, 비트연산(XOR)
# 난이도: 중
# 풀이 요약:
#   1. 주어진 테이블 데이터를 col번째 컬럼 기준으로 오름차순 정렬하고,
#      동일한 경우 기본키인 첫 번째 컬럼(x[0])을 기준으로 내림차순 정렬한다.
#   2. 정렬된 테이블의 row_begin번째 행부터 row_end번째 행까지의 각 행을 i라 할 때,
#      해당 행의 모든 원소를 i로 나눈 나머지들의 합을 S_i로 정의한다.
#   3. 이 S_i들을 모두 XOR(⊕) 연산하여 최종 결과를 반환한다.
# 시간복잡도: O(n log n + n * m)

import numpy as np

def solution(data, col, row_begin, row_end):
    answer = 0

    # 1. 테이블의 튜플을 col번째 컬럼의 값을 기준으로 오름차순 정렬
    # 2. 만약 그 값이 동일하면 기본키인 첫 번째 컬럼의 값을 기준으로 내림차순 정렬
    data.sort(key=lambda x: (x[col - 1], -x[0])) 
    
    # 3. 정렬된 데이터에서 S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합으로 정의
    for i in range(row_begin, row_end + 1):
        val = np.array(data[i - 1])
        S_i = np.sum(val % i)            # 각 값 % i 한 것의 합
        answer ^= int(S_i)
    
    return answer