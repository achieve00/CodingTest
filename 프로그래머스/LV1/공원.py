def maximal_square(board):
    if not board:
        return 0

    rows, cols = len(board), len(board[0])
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0
    # dp[i][j]는 (i,j) 셀을 우하단 꼭짓점으로 갖는 정사각형 중 "모두 '-1'"인 정사각형의 최대 한 변 길이를 저장
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "-1":
                if i == 0 or j == 0:
                    dp[i][j] = 1 # 첫 행이나 첫 열이면 1칸만 가능
                else:
                    dp[i][j] = min(
                        dp[i - 1][j], # 위쪽
                        dp[i][j - 1], # 왼쪽
                        dp[i - 1][j - 1] # 좌상단
                    ) + 1
                max_side = max(max_side, dp[i][j]) # 그 중 가장 큰 값 

    return max_side



def solution(mats, park):
    answer = 0
    max_len = maximal_square(park)
    answer = max((x for x in mats if x <= max_len), default=-1)
    
    return answer