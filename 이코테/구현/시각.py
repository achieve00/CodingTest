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