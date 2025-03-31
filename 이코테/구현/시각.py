# 문제: 시각
# 유형: 구현, 완전 탐색
# 난이도: 하
# 풀이 요약: 시/분/초를 문자열로 결합한 뒤, '3'이 포함되어 있으면 카운트
# 시간복잡도: O(N * 60 * 60) → 최대 약 86,400회 연산 (N ≤ 23)

# 정수 N은 0<= N <=23
# 3이 포함된 걸 세기
N = int(input())
cnt = 0

# N시 59분 59초까지 실행
for i in range(N+1): # 시
    for j in range(60): # 분
        for k in range(60): # 초
            if '3' in str(i) + str(j) + str(k):
                cnt +=1
print(cnt)