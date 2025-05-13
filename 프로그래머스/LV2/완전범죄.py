def solution(info, n, m):
    answer = -1
    
    # a와 b의 흔적 개수
    A = 0
    B = 0
    
    info.sort(key = lambda x: x[0] - x[1], reverse=True)
    
    # greedy하게 구하는 방법
    for a, b in info:
        # B가 이거 맡으면 m 넘게 될 수 있다면 A에게 맡기자
        if B + b < m:
            B += b
        else:
            A += a

     # 두 도둑 모두 경찰에 붙잡히지 않도록 모든 물건을 훔쳤을 때, A도둑이 남긴 흔적의 누적 개수의 최솟값을 return
    if not (A >= n or B >= m):
        answer = A
    
    return answer


################################################################################################
''' 위 방법으로는 통과는 하지만 [[2, 2], [2, 2], [3, 3]], 10, 4에서 틀린 답이 나옴
DP로 푸는 것이 맞는 것으로 보임'''

def solution(info, n, m):
    L = len(info)
    INF = float('inf')

    dp = [[INF] * m for _ in range(L + 1)]
    dp[0][0] = 0

    for i in range(L):
        a_cost, b_cost = info[i]
        for b in range(m):
            if dp[i][b] == INF:
                continue
            new_a = dp[i][b] + a_cost
            if new_a < n:  
                dp[i + 1][b] = min(dp[i + 1][b], new_a)
            
            new_b = b + b_cost
            if new_b < m:
                dp[i + 1][new_b] = min(dp[i + 1][new_b], dp[i][b])

    ans = min(dp[L])
    return ans if ans != INF else -1