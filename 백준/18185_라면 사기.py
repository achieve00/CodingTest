# 18185 라면 사기

# 1. i번 공장에서 라면을 하나 구매한다(1 ≤ i ≤ N). 이 경우 비용은 3원이 든다
# 2. i번 공장과 (i+1)번 공장에서 각각 라면을 하나씩 구매한다(1 ≤ i ≤ N-1). 이 경우 비용은 5원이 든다.
# 3. i번 공장과 (i+1)번 공장, (i+2)번 공장에서 각각 라면을 하나씩 구매한다(1 ≤ i ≤ N-2). 이 경우 비용은 7원이 든다.

# 최소의 비용으로 라면을 구매하고자 할 때, 교준이가 필요한 금액을 출력하는 프로그램을 작성

N = int(input()) # 라면 공장의 개수
A = list(map(int, input().split())) # i번 공장에서 정확하게 Ai개의 라면을 구매해야함

# 연속된 쌍 확인 -> 해당 쌍에 맞게 비용 +
# 연속된 쌍에서 -1
# 다시 확인 -> 반복

cost = 0 
i = 0

while i < N:
    # 3개 연속 가능한 경우
    if i + 2 < N and A[i] > 0 and A[i+1] > 0 and A[i+2] > 0:
        m = min(A[i], A[i+1], A[i+2])
        A[i] -= m
        A[i+1] -= m
        A[i+2] -= m
        cost += 7 * m
    # 2개 연속 가능한 경우
    elif i + 1 < N and A[i] > 0 and A[i+1] > 0:
        m = min(A[i], A[i+1])
        A[i] -= m
        A[i+1] -= m
        cost += 5 * m
    # 혼자 남은 경우
    elif A[i] > 0:
        cost += 3 * A[i]
        A[i] = 0
    else:
        i += 1

print(cost)